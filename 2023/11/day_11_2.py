#!/usr/bin/env python

from itertools import combinations

EMPTY_WORTH = 1_000_000


class Galaxy:
    def __init__(self, id_: int, i: int, j: int):
        self.id = id_
        self.i = i
        self.j = j

    def __repr__(self):
        return f"{self.id}"

    def distance(self, other: "Galaxy", i_to_expand: list[int], j_to_expand: list[int]) -> int:
        dist_i = abs(self.i - other.i)
        dist_i += sum([EMPTY_WORTH - 1
                       for i in i_to_expand
                       if i in range(self.i, other.i) or i in range(other.i, self.i)])

        dist_j = abs(self.j - other.j)
        dist_j += sum([EMPTY_WORTH - 1
                       for j in j_to_expand
                       if j in range(self.j, other.j) or j in range(other.j, self.j)])
        return dist_i + dist_j


def parse(day_input: str) -> tuple[list[list[str]], list[int], list[int]]:
    map_ = [[c for c in line] for line in day_input.split("\n")]

    i_to_expand = [
        i
        for i in range(len(map_))
        if all([c == "." for c in map_[i]])
    ]
    j_to_expand = [
        j
        for j in range(len(map_[0]))
        if all([map_[i][j] == "." for i in range(len(map_))])
    ]

    return map_, i_to_expand, j_to_expand


def create_galaxies(map_: list[list[str]]) -> dict[int, Galaxy]:
    counter = 1
    table = {}

    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] == "#":
                table[counter] = Galaxy(counter, i, j)
                counter += 1

    return table


def combinations_distance_sum(table: dict[int, Galaxy], i_to_expand: list[int], j_to_expand: list[int]) -> int:
    distances = [
        g_1.distance(g_2, i_to_expand, j_to_expand)
        for g_1, g_2 in combinations(table.values(), r=2)
    ]
    return sum(distances)


if __name__ == "__main__":
    with open("input") as f:
        input_ = f.read().strip()

    galaxy_map, i_list, j_list = parse(input_)
    galaxy_table = create_galaxies(galaxy_map)
    print(combinations_distance_sum(galaxy_table, i_list, j_list))
