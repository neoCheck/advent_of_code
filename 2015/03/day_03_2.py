#!/usr/bin/env python


def get_location_set(instruction: list[str]) -> set[tuple[int, int]]:
    location_set: set[tuple[int, int]] = set()
    i, j = 0, 0
    location_set.add((i, j))

    for c in instruction:
        if c == ">":
            j += 1
        elif c == "<":
            j -= 1
        elif c == "v":
            i += 1
        elif c == "^":
            i -= 1
        location_set.add((i, j))

    return location_set


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    santa_instructions = [c for i, c in enumerate(day_input) if i % 2 == 0]
    robot_santa_instructions = [c for i, c in enumerate(day_input) if i % 2 == 1]

    santa_locations = get_location_set(santa_instructions)
    robot_santa_locations = get_location_set(robot_santa_instructions)

    print(len(santa_locations | robot_santa_locations))


if __name__ == "__main__":
    main()
