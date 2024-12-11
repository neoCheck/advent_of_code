#!/usr/bin/env python
import math
from collections import Counter



def parse(day_input: str) -> list[int]:
    return [int(line) for line in day_input.split(" ")]


def calculate(num: int) -> list[int]:
    if num == 0:
        return [1]
    elif (num_digits := int(math.log10(num)) + 1) % 2 == 0:
        middle_divider = 10 ** (num_digits / 2)
        first_half = int(num / middle_divider)
        second_half = int(num % middle_divider)
        return [first_half, second_half]
    else:
        return [num * 2024]


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    num_list = parse(day_input)
    counts = Counter(num_list)

    for i in range(75):
        new_counts = {}
        for num, occurrences in counts.items():
            for new_num in calculate(num):
                new_counts[new_num] = new_counts.get(new_num, 0) + occurrences

        counts = new_counts

    print(sum(counts.values()))


if __name__ == "__main__":
    main()
