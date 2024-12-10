#!/usr/bin/env python
from itertools import permutations


def parse(day_input: str) -> dict[tuple[str, str], int]:
    flights = {}
    for line in day_input.split("\n"):
        flight_str, distance = line.split(" = ")
        point_a, point_b = flight_str.split(" to ")
        flights[point_a, point_b] = int(distance)
        flights[point_b, point_a] = int(distance)

    return flights

def get_distance(towns: list[str], flights: dict[tuple[str, str], int]) -> list[int]:
    distance = 0
    for i in range(len(towns) - 1):
        town_a, town_b = towns[i], towns[i + 1]
        distance += flights[town_a, town_b]

    return distance


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)
    towns = set([a for a, _ in parsed_input.keys()])

    max_distance = None
    for permutation in permutations(towns, len(towns)):
        distance = get_distance(list(permutation), parsed_input)
        if max_distance is None:
            max_distance = distance
        elif distance > max_distance:
            max_distance = distance

    print(max_distance)


if __name__ == "__main__":
    main()
