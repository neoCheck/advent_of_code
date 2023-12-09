#!/usr/bin/env python


def lagrange_interpolation(sequence: list[int], goal: int) -> int:
    # Note : While Lagrange interpolation is straightforward,
    # for larger datasets or higher-degree polynomials, other interpolation methods might be more suitable.

    result = 0
    n = len(sequence)
    y_values = sequence
    x_values = range(n)
    x = goal

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return round(result)


def parse(day_input: str) -> list[list[int]]:
    return [
        [int(n) for n in line.split(" ")]
        for line in day_input.split("\n")
    ]


if __name__ == "__main__":
    input_ = open("input").read().strip()
    list_sequences = parse(input_)
    res_part1 = [lagrange_interpolation(s, len(s)) for s in list_sequences]
    res_part2 = [lagrange_interpolation(s, -1) for s in list_sequences]

    print(sum(res_part1))
    print(sum(res_part2))
