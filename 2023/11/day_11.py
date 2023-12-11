#!/usr/bin/env python

from itertools import combinations


class Galaxy:
    def __init__(self, id_: int, i: int, j: int):
        self.id = id_
        self.i = i
        self.j = j

    def __repr__(self):
        return f"{self.id}"

    def distance(self, other: "Galaxy") -> int:
        dist_i = abs(self.i - other.i)
        dist_j = abs(self.j - other.j)
        return dist_i + dist_j


def parse(day_input: str) -> list[list[str]]:
    map_ = [[c for c in line] for line in day_input.split("\n")]

    # Expand Map
    j_to_expand = [
        j
        for j in range(len(map_[0]))
        if all([map_[i][j] == "." for i in range(len(map_))])
    ]
    for j in reversed(j_to_expand):
        for i in range(len(map_)):
            map_[i].insert(j, ".")

    i_to_expand = [
        i
        for i in range(len(map_))
        if all([c == "." for c in map_[i]])
    ]
    line_dot = map_[i_to_expand[0]].copy()
    for i in reversed(i_to_expand):
        map_.insert(i, line_dot)

    return map_


def create_galaxies(map_: list[list[str]]) -> dict[int, Galaxy]:
    counter = 1
    table = {}

    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] == "#":
                table[counter] = Galaxy(counter, i, j)
                counter += 1

    return table


def combinations_distance_sum(table: dict[int, Galaxy]) -> int:
    distances = [
        g_1.distance(g_2)
        for g_1, g_2 in combinations(table.values(), r=2)
    ]
    return sum(distances)


def print_map(map_: list[list[str]]):
    for line in map_:
        for c in line:
            print(c, end="")
        print("")


if __name__ == "__main__":
    with open("input") as f:
        input_ = f.read().strip()

    galaxy_map = parse(input_)
    galaxy_table = create_galaxies(galaxy_map)
    # print_map(galaxy_map)
    print(combinations_distance_sum(galaxy_table))

    print(0)
