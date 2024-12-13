from typing import TypeAlias
from collections import defaultdict

Plot: TypeAlias = tuple[int, int]
GardenArea: TypeAlias = set[Plot]

def get_plot_area(current_plot: Plot, plots: GardenArea, visited_plots: GardenArea) -> GardenArea:
    for connected_plot in get_connected_plots(current_plot):
        if connected_plot in plots:
            plots.remove(connected_plot)
            visited_plots.add(connected_plot)
            get_plot_area(connected_plot, plots, visited_plots)
    return visited_plots

def get_connected_plots(plot: Plot) -> GardenArea:
    connected_plots: GardenArea = set()
    x, y = plot
    if y > 0:
        connected_plots.add((x, y - 1))
    if x > 0:
        connected_plots.add((x - 1, y))
    connected_plots.add((x + 1, y))
    connected_plots.add((x, y + 1))
    return connected_plots

def get_areas(data: list[str]) -> list[GardenArea]:
    plant_types: defaultdict[str, GardenArea] = defaultdict(set)
    areas: list[GardenArea] = list()

    for y, row in enumerate(data):
        for x, plant_type in enumerate(list(row)):
            plant_types[plant_type].add((x, y))

    for garden_plots in plant_types.values():
        while len(garden_plots):
            try:
                area: GardenArea = set()
                garden_plot = garden_plots.pop()
                area.add(garden_plot)
                area.update(get_plot_area(garden_plot, garden_plots, set()))
                areas.append(area)
            except KeyError:
                areas.append(area)
                pass

    return areas

def calculate_sides(area: GardenArea) -> int:
    sides = 0

    # Helper function to check if two plots are adjacent (neighbors)
    def _are_neighbours(p1: Plot, p2: Plot) -> bool:
        x1, y1 = p1
        x2, y2 = p2
        return (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1)

    # Iterate over each plot in the given garden area
    for plot in area:
        x, y = plot
        # Print for each plot to see its corners and how sides are calculated
        print(f"Calculating sides for plot: {plot} ({x}, {y})")
        # Define four possible "corners" of a plot; these are positions diagonal from the current plot
        plot_corners = [
            {(x - 1, y), (x - 1, y - 1), (x, y - 1)},
            {(x, y - 1), (x + 1, y - 1), (x + 1, y)},
            {(x - 1, y), (x - 1, y + 1), (x, y + 1)},
            {(x + 1, y), (x + 1, y + 1), (x, y + 1)}
        ]
        
        # For each corner, check if the plot has neighbors
        for corners in plot_corners:
            corner_plots = corners & area  # Get the intersection with the area (plots within the region)
            
            # If no corner plots are in the same region, it contributes to a side
            if len(corner_plots) == 0:
                sides += 1
            # If exactly two corner plots are in the region and are not adjacent, it contributes to a side
            elif len(corner_plots) == 2 and not _are_neighbours(*corner_plots):
                sides += 1
            # If there's exactly one corner plot and it's not adjacent to the current plot, it contributes to a side
            elif len(corner_plots) == 1 and not _are_neighbours(plot, *corner_plots):
                sides += 1
    print(f"Total sides for region: {sides}")
    return sides

def part_2(areas: list[GardenArea]) -> int:
    total_price = 0
    for area in areas:
        sides = calculate_sides(area)
        area_size = len(area)
        region_price = sides * area_size
        total_price += region_price
        print(f"Region of size {area_size} has {sides} sides and costs {region_price}")
    return total_price

if __name__ == '__main__':
    import time

    def read_file(filename: str) -> list[str]:
        with open(filename, "r") as file:
            return file.read().splitlines()

    data = read_file("input_example.txt")
    start_time = time.perf_counter()
    gardening_areas = get_areas(data)
    end_time = time.perf_counter()

    start_time = time.perf_counter()
    answer_part_2 = part_2(gardening_areas)
    end_time = time.perf_counter()
    print(f"Part 2 - {answer_part_2} (Execution Time: {(end_time - start_time) * 1000:.3f} ms)")