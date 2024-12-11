#!/usr/bin/env python
from itertools import combinations


def parse(day_input: str) -> list[int]:
    return [int(line) for line in day_input.split("\n")]



def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    containers = parse(day_input)

    possible_combinations = 0
    for i, _ in enumerate(containers):
        for combination in combinations(containers, i + 1):
            if sum(combination) == 150:
                possible_combinations += 1

    print(possible_combinations)


if __name__ == "__main__":
    main()
