#!/usr/bin/env python
import numpy as np
import shapely
import shapely.ops


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



def find_corners(coords):
    # Remove duplicate ending point
    coords = coords[:-1]

    corners = []
    for i in range(len(coords)):
        # Get the three points: previous, current, and next
        prev_point = coords[i - 1]
        curr_point = coords[i]
        next_point = coords[(i + 1) % len(coords)]

        # Calculate vectors
        vec1 = np.array([curr_point[0] - prev_point[0], curr_point[1] - prev_point[1]])
        vec2 = np.array([next_point[0] - curr_point[0], next_point[1] - curr_point[1]])

        # Check if the direction changes (dot product != ±1 or cross product != 0)
        if not np.allclose(np.cross(vec1, vec2), 0) or not np.allclose(np.dot(vec1, vec2),
                                                                       np.linalg.norm(vec1) * np.linalg.norm(vec2)):
            corners.append(curr_point)

    return corners


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    grid = parse(day_input)

    regions = get_regions(grid)

    sum_cost = 0
    for region in regions:
        area = len(region)
        new_poly = shapely.ops.unary_union(
            [
                shapely.Polygon([(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1), (x, y)])
                for x, y in region
            ]
        )
        corners = len(find_corners(list(new_poly.exterior.coords)))
        for interior in new_poly.interiors:
            corners += len(find_corners(list(interior.coords)))

        sum_cost += corners * area

    print(sum_cost)

if __name__ == "__main__":
    main()
