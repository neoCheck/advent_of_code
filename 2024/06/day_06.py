#!/usr/bin/env python


def parse(day_input: str) -> list[list[str]]:
    return [
        [pos for pos in line]
        for line in day_input.split("\n")
    ]


def find_initial_position(map_: list[list[str]]) -> tuple[int, int]:
    for i, line in enumerate(map_):
        for j, pos in enumerate(line):
            if pos == "^":
                return i, j

    raise ValueError("No initial position found")


def move_in_map(map_: list[list[str]], positions: set[tuple[int, int]]) -> None:
    current_x, current_y = find_initial_position(map_)

    positions.add((current_x, current_y))

    while True:
        current_direction = map_[current_x][current_y]
        if current_direction == "^":
            next_x, next_y = current_x - 1, current_y
        elif current_direction == "v":
            next_x, next_y = current_x + 1, current_y
        elif current_direction == "<":
            next_x, next_y = current_x, current_y - 1
        elif current_direction == ">":
            next_x, next_y = current_x, current_y + 1
        else:
            raise ValueError("Weird")

        if next_x < 0 or next_y < 0:
            raise IndexError()

        if map_[next_x][next_y] == ".":
            map_[current_x][current_y] = "."
            map_[next_x][next_y] = current_direction
            current_x, current_y = next_x, next_y
            positions.add((next_x, next_y))
        elif map_[next_x][next_y] == "#":
            if current_direction == "^":
                map_[current_x][current_y] = ">"
            elif current_direction == ">":
                map_[current_x][current_y] = "v"
            elif current_direction == "v":
                map_[current_x][current_y] = "<"
            elif current_direction == "<":
                map_[current_x][current_y] = "^"


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    map_ = parse(day_input)

    positions: set[tuple[int, int]] = set()

    try:
        move_in_map(map_, positions)
    except IndexError:
        pass

    print(len(positions))


if __name__ == "__main__":
    main()
