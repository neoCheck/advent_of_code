#!/usr/bin/env python
import datetime


def is_valid_combination(combination: str, groups: list[int]) -> bool:
    spring_groups = [len(g) for g in combination.split(".") if g]
    return spring_groups == groups


def generate_valid_combinations(prev, nxt, groups):
    i = nxt.find("?")
    if i == -1:
        combination = f"{prev}{nxt}"
        return [combination] if is_valid_combination(combination, groups) else []

    prev = f"{prev}{nxt[:i]}"
    nxt = nxt[i + 1:]

    combinations = []
    combinations += generate_valid_combinations(f"{prev}.", nxt, groups)
    combinations += generate_valid_combinations(f"{prev}#", nxt, groups)

    return combinations


def get_valid_combination(parsed_lines: list[tuple[str, list[int]]]):
    count = 0
    for i, (springs, groups) in enumerate(parsed_lines):
        if i % 100 == 0:
            print(f"{datetime.datetime.now()} progress : {i}/{len(parsed_lines)}")

        combinations = generate_valid_combinations("", springs, groups)
        count += len(combinations)

    print(count)


def parse(day_input: str) -> list[tuple[str, list[int]]]:
    parsed_lines = []
    for line in day_input.split("\n"):
        springs, groups = line.split(" ")
        groups = [int(g) for g in groups.split(",")]

        parsed_lines.append((springs, groups))

    return parsed_lines


if __name__ == "__main__":
    with open("input") as f:
        input_ = f.read().strip()

    p = parse(input_)
    get_valid_combination(p)
