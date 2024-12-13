from collections import defaultdict
from typing import TypeAlias

# Define type aliases for better code readability
Plot: TypeAlias = tuple[int, int]
GardenArea: TypeAlias = set[Plot]

def calculate_perimeter(area: GardenArea) -> int:
    """
    Calculate the perimeter of a given garden area.
    Perimeter is determined by the number of sides not shared with other plots in the same area.
    """
    perimeter = 0
    for plot in area:
        # Calculate the number of sides not connected to another plot in the same area
        connected = get_connected_plots(plot) & area
        perimeter += (4 - len(connected))
        print(f"Plot {plot}: Connected to {connected}, Perimeter contribution = {4 - len(connected)}")
    return perimeter

def get_connected_plots(plot: Plot) -> GardenArea:
    """
    Get all plots that are directly adjacent to a given plot.
    Adjacency is defined as sharing a horizontal or vertical side.
    """
    connected_plots: GardenArea = set()
    x, y = plot
    # Add adjacent plots considering boundary conditions
    if y > 0:
        connected_plots.add((x, y - 1))  # Above
    if x > 0:
        connected_plots.add((x - 1, y))  # Left
    connected_plots.add((x + 1, y))      # Right
    connected_plots.add((x, y + 1))      # Below
    print(f"Plot {plot}: Adjacent plots = {connected_plots}")
    return connected_plots

def get_plot_area(current_plot: Plot, plots: GardenArea, visited_plots: GardenArea) -> GardenArea:
    """
    Recursively find all connected plots of the same type starting from a given plot.
    """
    for connected_plot in get_connected_plots(current_plot):
        if connected_plot in plots:
            # Mark the plot as visited and remove it from the remaining plots
            plots.remove(connected_plot)
            visited_plots.add(connected_plot)
            print(f"Visiting plot {connected_plot}, remaining plots = {plots}")
            # Recursively explore connected plots
            get_plot_area(connected_plot, plots, visited_plots)
    return visited_plots

def get_areas(data: list[str]) -> list[GardenArea]:
    """
    Parse the input data and group plots into distinct garden areas based on plant types.
    """
    plant_types: defaultdict[str, GardenArea] = defaultdict(set)
    areas: list[GardenArea] = list()

    # Group all plots by plant type
    for y, row in enumerate(data):
        for x, plant_type in enumerate(list(row)):
            plant_types[plant_type].add((x, y))
    print(f"Initial grouping by plant types: {plant_types}")

    # Identify distinct areas for each plant type
    for plant_type, garden_plots in plant_types.items():
        print(f"Processing plant type '{plant_type}' with plots {garden_plots}")
        while len(garden_plots):
            try:
                area: GardenArea = set()
                garden_plot = garden_plots.pop()
                area.add(garden_plot)
                print(f"Starting new area with plot {garden_plot}")
                # Find the entire connected area for this plot
                area.update(get_plot_area(garden_plot, garden_plots, set()))
                areas.append(area)
                print(f"Completed area: {area}")
            except KeyError:
                # Handle cases where garden_plots is empty
                areas.append(area)
                pass

    return areas

def part_1(areas: list[GardenArea]) -> int:
    """
    Compute the total cost of fencing all garden areas.
    Cost is calculated as the product of the area size and its perimeter.
    """
    total_cost = 0
    for area in areas:
        area_size = len(area)
        perimeter = calculate_perimeter(area)
        cost = area_size * perimeter
        total_cost += cost
        print(f"Area: {area}, Size: {area_size}, Perimeter: {perimeter}, Cost: {cost}")
    return total_cost

def solve_part_1(data: list[str]) -> int:
    """
    Solve part one of the puzzle by computing the total fencing cost.
    """
    # Parse the input data into garden areas
    gardening_areas = get_areas(data)
    print(f"All garden areas: {gardening_areas}")
    # Calculate the total cost of fencing
    return part_1(gardening_areas)

if __name__ == '__main__':
    import time

    def read_file(filename: str) -> list[str]:
        """
        Read the input file and return its content as a list of strings.
        """
        with open(filename, "r") as file:
            return file.read().splitlines()

    # Load the input data - STEP 1!
    data = read_file("input_example.txt")
    print(f"Input data: {data}")

    # Measure execution time
    start_time = time.perf_counter()
    answer_part_1 = solve_part_1(data)
    end_time = time.perf_counter()

    # Print the result and execution time
    print(f"Part 1 - {answer_part_1} (Execution Time: {(end_time - start_time) * 1000:.3f} ms)")
