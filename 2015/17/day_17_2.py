#!/usr/bin/env python
from itertools import combinations


def parse(day_input: str) -> list[int]:
    return [int(line) for line in day_input.split("\n")]



def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    containers = parse(day_input)

    amount = 150
    minium_containers = 0
    for container in sorted(containers, reverse=True):
        if amount > 0:
            amount -= container
            minium_containers += 1
        else:
            break

    possible_combinations = 0
    for i, _ in enumerate(containers):
        for combination in combinations(containers, i + 1):
            if minium_containers == len(combination) and sum(combination) == 150:
                possible_combinations += 1

    print(possible_combinations)


if __name__ == "__main__":
    main()
