#!/usr/bin/env python


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

    def mark_enclosure(self) -> None:
        current_node = self
        previous_node = None

        while current_node:
            current_node.part_of_loop = True
            next_nodes = [current_node.north, current_node.south, current_node.east, current_node.west]
            next_nodes = [n for n in next_nodes if n and n not in (self, current_node, previous_node)]
            previous_node = current_node
            current_node = next_nodes[0] if next_nodes else None

    @property
    def inside_of_loop(self) -> bool:
        times_met_enclosure = 0
        for j in range(self.j, len(self.map[self.i])):
            node = self.map[self.i][j]
            if node.part_of_loop and node.pipe in ["J", "L", "S", "|"]:
                times_met_enclosure += 1

        return bool(times_met_enclosure % 2)


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


def print_map(map_: list[list[Node]]):
    counter = 0
    for node_list in map_:
        for node in node_list:
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
    s.mark_enclosure()

    print_map(s.map)
