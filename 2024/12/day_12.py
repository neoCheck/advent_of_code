#!/usr/bin/env python

T_POINT = tuple[int, int]

def parse(day_input: str) -> list[list[str]]:
    return [
        [c for c in line]
        for line in day_input.split("\n")
    ]

def find_region(available_regions: list[list[T_POINT]], point: T_POINT, x_len: int, y_len: int) -> int:
    neighbor_points: list[T_POINT] = []
    x, y = point
    if x > 0:
        neighbor_points.append((x - 1, y))
    if y > 0:
        neighbor_points.append((x, y - 1))
    if x + 1 < x_len:
        neighbor_points.append((x + 1, y))
    if y + 1 < y_len:
        neighbor_points.append((x, y + 1))

    for i, region in enumerate(available_regions):
        for region_point in region:
            if region_point in neighbor_points:
                return i

    return -1


def find_region_not_in_my_region(available_regions: list[list[T_POINT]], point: T_POINT, x_len: int, y_len: int, my_region_index: int) -> int:
    neighbor_points: list[T_POINT] = []
    x, y = point
    if x > 0:
        neighbor_points.append((x - 1, y))
    if y > 0:
        neighbor_points.append((x, y - 1))
    if x + 1 < x_len:
        neighbor_points.append((x + 1, y))
    if y + 1 < y_len:
        neighbor_points.append((x, y + 1))

    for i, region in enumerate(available_regions):
        if i != my_region_index:
            for region_point in region:
                if region_point in neighbor_points:
                    return i

    return -1


def get_regions(grid: list[list[str]]) -> list[list[T_POINT]]:
    regions: dict[str, list[list[T_POINT]]] = {}

    x_len = len(grid)
    y_len = len(grid[0])
    for x in range(x_len):
        for y in range(y_len):
            plant = grid[x][y]
            point = (x, y)
            if plant not in regions:
                regions[plant] = []

            region_index = find_region(regions[plant], point, x_len, y_len)
            if region_index == -1:
                regions[plant].append([point])
            else:
                regions[plant][region_index].append(point)

    # link_regions
    for letter, available_regions in regions.items():
        current_region_index = 0
        len_available_regions = len(available_regions)
        while current_region_index < len_available_regions and len_available_regions > 1:
            restart_link = False
            for point in available_regions[current_region_index]:
                region_index = find_region_not_in_my_region(available_regions, point, x_len, y_len, current_region_index)
                if region_index != -1:
                    available_regions[current_region_index] += available_regions.pop(region_index)
                    len_available_regions = len(available_regions)
                    restart_link = True
                    break
            if restart_link:
                current_region_index = 0
            else:
                current_region_index += 1

    return [region for available_regions in regions.values() for region in available_regions ]

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    grid = parse(day_input)

    regions = get_regions(grid)

    sum_cost = 0
    for region in regions:
        area = len(region)
        perimeter = 0
        for i, j in region:
            if not (i - 1, j) in region:
                perimeter += 1
            if not (i, j - 1) in region:
                perimeter += 1
            if not (i + 1, j) in region:
                perimeter += 1
            if not (i, j + 1) in region:
                perimeter += 1

        cost = area * perimeter
        sum_cost += cost

    print(sum_cost)

if __name__ == "__main__":
    main()
