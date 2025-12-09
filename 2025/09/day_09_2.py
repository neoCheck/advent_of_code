#!/usr/bin/env python
# pip install shapely
from shapely.geometry import Polygon as ShapelyPolygon
from shapely.geometry import Point as ShapelyPoint
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Point:
    x: int
    y: int

    @property
    def shapely_point(self) -> ShapelyPoint:
        return ShapelyPoint(self.x, self.y)


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
    polygon = ShapelyPolygon([p.shapely_point for p in point_list])

    max_area = 1
    for p1, p2 in combinations(point_list, 2):
        min_x = min(p1.x, p2.x)
        min_y = min(p1.y, p2.y)
        max_x = max(p1.x, p2.x)
        max_y = max(p1.y, p2.y)
        rectangle = ShapelyPolygon([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])

        if polygon.contains(rectangle):
            area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
            if area > max_area:
                max_area = area

    print(max_area)


if __name__ == "__main__":
    main()
