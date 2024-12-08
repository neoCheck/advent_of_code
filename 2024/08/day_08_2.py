#!/usr/bin/env python
from itertools import combinations


class AntennaMap:
    raw_map: list[list[str]]
    size_i: int
    size_j: int
    antennas: dict[str, list[tuple[int, int]]]
    anti_nodes: set[tuple[int, int]]

    def __init__(self, raw_map: list[list[str]]) -> None:
        self.raw_map = raw_map
        self.size_i = len(raw_map)
        self.size_j = len(raw_map[0])
        self.init_antennas()
        self.init_anti_nodes()

    def init_antennas(self) -> None:
        self.antennas = {}

        for i, row in enumerate(self.raw_map):
            for j, antenna in enumerate(row):
                if antenna not in self.antennas:
                    self.antennas[antenna] = []
                self.antennas[antenna].append((i, j))

        self.antennas.pop(".", None)

    def init_anti_nodes(self) -> None:
        self.anti_nodes = set()
        for antenna, positions in self.antennas.items():
            raw_vectors = list(combinations(positions, 2))
            for a, b in raw_vectors:
                v_i = a[0] - b[0]
                v_j = a[1] - b[1]

                for i in range(max(self.size_i, self.size_j)):
                    new_v_i = v_i * i
                    new_v_j = v_j * i
                    self.anti_nodes.add((a[0] + new_v_i, a[1] + new_v_j))
                    self.anti_nodes.add((b[0] - new_v_i, b[1] - new_v_j))

        # Clean
        self.anti_nodes = set([
            (i, j)
            for i, j in self.anti_nodes
            if self.size_i > i >= 0 and self.size_j > j >= 0
        ])


def parse(day_input: str) -> list[list[str]]:
    return [
        [c for c in line]
        for line in day_input.split("\n")
    ]


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    a_map = AntennaMap(parsed_input)

    print(len(a_map.anti_nodes))


if __name__ == "__main__":
    main()
