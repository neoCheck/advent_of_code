#!/usr/bin/env python
from collections import defaultdict


def main() -> None:
    with open("input") as f:
        minimum_sum = int(f.read().strip())

    houses = defaultdict(int)

    for elf in range(1, minimum_sum):
        for house in range(elf, min(elf*50+1, 1_000_000), elf):
            houses[house] += elf*11

        if houses[elf] >= minimum_sum:
            print(elf)
            break


if __name__ == "__main__":
    main()
