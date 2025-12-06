#!/usr/bin/env python


DIAL = list(range(100))
START_INDEX = 50

def parse(day_input: str) -> list[tuple[str, int]]:
    return [(line[0], int(line[1:])) for line in day_input.split("\n")]


def move_through_dial(movement: str, distance: int, current_index: int) -> int:
    new_index = 0
    if movement == "L":
        new_index = current_index - distance
    elif movement == "R":
        new_index = current_index + distance

    return new_index % len(DIAL)

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    index = START_INDEX
    counter = 0
    for movement, distance in parsed_input:
        index = move_through_dial(movement, distance, index)
        if DIAL[index] == 0:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
