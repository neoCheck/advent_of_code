#!/usr/bin/env python
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Point:
    x: int
    y: int


def parse(day_input: str) -> list[Point]:
    point_list = []
    for line in day_input.split("\n"):
        x_str, y_str = line.split(",")
        point_list.append(Point(int(x_str), int(y_str)))

    return point_list


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    point_list = parse(day_input)

    max_area = 1
    for p1, p2 in combinations(point_list, 2):
        area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
        if area > max_area:
            max_area = area

    print(max_area)


if __name__ == "__main__":
    main()
