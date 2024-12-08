#!/usr/bin/env python


def parse(day_input: str) -> list[str]:
    return [line for line in day_input.split("\n")]


def is_nice(line: str) -> bool:
    if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
        return False

    vowels_counter = 0
    has_double_letters = False
    previous_c = None
    for c in line:
        if c in ["a", "e", "i", "o", "u"]:
            vowels_counter += 1
        if not has_double_letters and previous_c == c:
            has_double_letters = True
        previous_c = c

    return has_double_letters and vowels_counter >= 3


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    nice_lines = [line for line in parsed_input if is_nice(line)]
    print(len(nice_lines))


if __name__ == "__main__":
    main()
