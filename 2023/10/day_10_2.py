#!/usr/bin/env python

# pip install shapely
from shapely.geometry import Polygon, Point


class Node:

    def __init__(self, pipe: str, i: int, j: int, map_: list[list["Node"]]) -> None:
        self.pipe = pipe
        self.i, self.j = i, j
        self.map = map_

        self.north = None
        self.south = None
        self.east = None
        self.west = None

        self.part_of_loop = False
        self.inside_of_loop = False

    def __repr__(self):
        return self.pipe

    def connect_north(self):
        if self.i > 0 and self.map[self.i - 1][self.j].pipe in ["7", "F", "|", "S"]:
            self.north = self.map[self.i - 1][self.j]

    def connect_south(self):
        if (self.i + 1) < len(self.map) and self.map[self.i + 1][self.j].pipe in ["L", "J", "|", "S"]:
            self.south = self.map[self.i + 1][self.j]

    def connect_east(self):
        if (self.j + 1) < len(self.map[self.i]) and self.map[self.i][self.j + 1].pipe in ["J", "7", "-", "S"]:
            self.east = self.map[self.i][self.j + 1]

    def connect_west(self):
        if self.j > 0 and self.map[self.i][self.j - 1].pipe in ["L", "F", "-", "S"]:
            self.west = self.map[self.i][self.j - 1]

    def link(self):
        if self.pipe in ["L", "J", "|", "S"]:
            self.connect_north()
        if self.pipe in ["7", "F", "|", "S"]:
            self.connect_south()
        if self.pipe in ["L", "F", "-", "S"]:
            self.connect_east()
        if self.pipe in ["J", "7", "-", "S"]:
            self.connect_west()

    def get_polygon_loop(self) -> Polygon:
        current_node = self
        previous_node = None

        points = [(self.i, self.j)]
        while current_node:
            current_node.part_of_loop = True
            next_nodes = [current_node.north, current_node.south, current_node.east, current_node.west]
            next_nodes = [n for n in next_nodes if n and n not in (self, current_node, previous_node)]
            previous_node = current_node
            current_node = next_nodes[0] if next_nodes else None
            if current_node:
                points.append((current_node.i, current_node.j))

        points += [(self.i, self.j)]
        return Polygon(points)


def parse(day_input: str) -> Node:
    map_ = []
    start = None
    for i, pipe_list in enumerate(day_input.split("\n")):
        line = []
        for j, pipe in enumerate(pipe_list):
            node = Node(pipe, i, j, map_)
            line.append(node)
            if pipe == "S":
                start = node
        map_.append(line)

    for node_list in map_:
        for node in node_list:
            node.link()

    return start


def print_map(map_: list[list[Node]], polygon: Polygon):
    counter = 0
    for node_list in map_:
        for node in node_list:
            if not node.part_of_loop:
                point = Point(node.i, node.j)
                node.inside_of_loop = polygon.contains(point)

            if node.part_of_loop:
                print(f"\033[95m{node.pipe}\033[0m", end="")
            elif node.inside_of_loop:
                print(f"\033[92m{node.pipe}\033[0m", end="")
                counter += 1
            else:
                print(node.pipe, end="")

        print("")
    print(counter)


if __name__ == "__main__":
    with open("input") as f:
        input_ = f.read().strip()

    s = parse(input_)
    p = s.get_polygon_loop()

    print_map(s.map, p)

