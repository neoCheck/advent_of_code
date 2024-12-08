#!/usr/bin/env python


def parse(day_input: str) -> list[str]:
    return [line for line in day_input.split("\n")]


def is_nice(line: str) -> bool:
    has_twice_pair = False
    has_a_mirror_letter = False
    for i in range(len(line)):
        if not has_twice_pair:
            if i > 0 and f"{line[i - 1]}{line[i]}" in line[i + 1:]:
                has_twice_pair = True

        if not has_a_mirror_letter:
            if 0 < i < len(line) - 1 and line[i - 1] == line[i + 1]:
                has_a_mirror_letter = True

        if has_a_mirror_letter and has_twice_pair:
            return True

    return False


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    nice_lines = [line for line in parsed_input if is_nice(line)]

    print(len(nice_lines))


if __name__ == "__main__":
    main()
