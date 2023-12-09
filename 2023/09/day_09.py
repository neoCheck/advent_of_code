#!/usr/bin/env python


def get_deltas(sequence: list[int]) -> list[int]:
    return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]


def extrapolate(sequence: list[int]) -> int:
    if all(x == 0 for x in sequence):
        return 0
    return sequence[-1] + extrapolate(get_deltas(sequence))


def parse(day_input: str) -> list[list[int]]:
    return [
        [int(n) for n in line.split(" ")]
        for line in day_input.split("\n")
    ]


if __name__ == "__main__":
    input_ = open("input").read().strip()
    list_sequences = parse(input_)
    res = [extrapolate(s) for s in list_sequences]
    print(sum(res))
