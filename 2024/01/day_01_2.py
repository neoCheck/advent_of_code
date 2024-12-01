#!/usr/bin/env python
from collections import Counter


def parse(day_input: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    for line in day_input.splitlines():
        number_list_1, number_list_2 = line.split("   ")
        left.append(int(number_list_1))
        right.append(int(number_list_2))
    return left, right


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    left, right = parse(day_input)

    right_counter = Counter(right)

    sum_occurred = 0
    for number in left:
        occurrences = right_counter.get(number) or 0
        sum_occurred += number * occurrences

    print(sum_occurred)


if __name__ == "__main__":
    main()
