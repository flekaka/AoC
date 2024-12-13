from collections import defaultdict
from typing import TypeAlias

Plot: TypeAlias = tuple[int, int]
GardenArea: TypeAlias = set[Plot]

def calculate_perimeter(area: GardenArea) -> int:
    perimeter = 0
    for plot in area:
        perimeter += (4 - len(get_connected_plots(plot) & area))
    return perimeter

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

def get_plot_area(current_plot: Plot, plots: GardenArea, visited_plots: GardenArea) -> GardenArea:
    for connected_plot in get_connected_plots(current_plot):
        if connected_plot in plots:
            plots.remove(connected_plot)
            visited_plots.add(connected_plot)
            get_plot_area(connected_plot, plots, visited_plots)
    return visited_plots

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

def part_1(areas: list[GardenArea]) -> int:
    return sum([calculate_perimeter(area) * len(area) for area in areas])

def solve_part_1(data: list[str]) -> int:
    gardening_areas = get_areas(data)
    return part_1(gardening_areas)

if __name__ == '__main__':
    import time

    def read_file(filename: str) -> list[str]:
        with open(filename, "r") as file:
            return file.read().splitlines()

    data = read_file("input.txt")

    start_time = time.perf_counter()
    answer_part_1 = solve_part_1(data)
    end_time = time.perf_counter()
    print(f"Part 1 - {answer_part_1} (Execution Time: {(end_time - start_time) * 1000:.3f} ms)")
