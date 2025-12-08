#!/usr/bin/env python
from dataclasses import dataclass
from itertools import combinations


@dataclass
class JunctionBox:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash((self.x, self.y, self.z))


def calculate_distance(j1: JunctionBox, j2: JunctionBox) -> int:
    return ((j1.x - j2.x) ** 2) + ((j1.y - j2.y) ** 2) + ((j1.z - j2.z) ** 2)


def parse(day_input: str) -> list[JunctionBox]:
    junction_box_list: list[JunctionBox] = []
    for line in day_input.split("\n"):
        x_str, y_str, z_str = line.split(",")
        junction_box_list.append(JunctionBox(x=int(x_str), y=int(y_str), z=int(z_str)))

    return junction_box_list


def find_junction_box_in_circuits(junction_box: JunctionBox, circuits: list[set[JunctionBox]]) -> int:
    for i, circuit in enumerate(circuits):
        if junction_box in circuit:
            return i

    return -1


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    junction_box_list = parse(day_input)
    len_junction_box_list = len(junction_box_list)

    distances_junction_box: list[tuple[int, list[JunctionBox]]] = sorted([
        (calculate_distance(j1, j2), [j1, j2])
        for j1, j2 in combinations(junction_box_list, 2)
    ])

    circuits: list[set[JunctionBox]] = []
    for _ in range(len(distances_junction_box)):
        distance, j_boxes = distances_junction_box.pop(0)
        j1 = j_boxes[0]
        j2 = j_boxes[1]

        index_circuit_for_j1 = find_junction_box_in_circuits(j1, circuits)
        index_circuit_for_j2 = find_junction_box_in_circuits(j2, circuits)

        if index_circuit_for_j1 == index_circuit_for_j2 == -1:
            circuits.append({j1, j2})
        elif index_circuit_for_j1 == index_circuit_for_j2:
            continue
        elif index_circuit_for_j1 == -1:
            circuits[index_circuit_for_j2].add(j1)
        elif index_circuit_for_j2 == -1:
            circuits[index_circuit_for_j1].add(j2)
        else:
            circuit_1 = circuits[index_circuit_for_j1]
            circuit_2 = circuits[index_circuit_for_j2]
            circuits[index_circuit_for_j1] = circuit_1 | circuit_2
            circuits.pop(index_circuit_for_j2)

        if len(circuits[0]) == len_junction_box_list:
            print(j1.x * j2.x)
            break



if __name__ == "__main__":
    main()
