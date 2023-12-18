#!/usr/bin/env python


def get_corners_and_perimeter(directions_input: list[tuple[str, int]]) -> tuple[list[tuple[int, int]], int]:
    i = 0
    j = 0
    corners = [(i, j)]
    perimeter = 0

    for direction, blocks in directions_input:
        perimeter += blocks

        if direction == "R":
            j += blocks
        elif direction == "L":
            j -= blocks
        elif direction == "U":
            i -= blocks
        elif direction == "D":
            i += blocks

        corners.append((i, j))

    return corners, perimeter


def shoelace_formula(corners: list[tuple[int, int]]):
    n = len(corners)

    # Ensure the list has at least 3 corners to form a polygon
    if n < 3:
        raise ValueError("At least 3 corners are required to form a polygon.")

    # Initialize variables for the summation
    area = 0.0
    j = n - 1

    # Calculate the sum using the Shoelace Formula
    for i in range(n):
        area += (corners[j][0] + corners[i][0]) * (corners[j][1] - corners[i][1])
        j = i

    # Take the absolute value and divide by 2 to get the area
    area = abs(area) / 2.0

    return area


def parse(day_input: str) -> list[tuple[str, int]]:
    parsed_list = []
    direction_mapping = {
        "0": "R",
        "1": "D",
        "2": "L",
        "3": "U",
    }
    for line in day_input.split("\n"):
        *_, color = line.split(" ")

        hex_color = color[2:-1]
        blocks = int(hex_color[:-1], 16)
        direction = direction_mapping[hex_color[-1]]

        parsed_list.append((direction, blocks))

    return parsed_list


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)
    corners, perimeter = get_corners_and_perimeter(parsed_input)
    area = shoelace_formula(corners)
    print(area + (perimeter // 2) + 1)


if __name__ == "__main__":
    main()
