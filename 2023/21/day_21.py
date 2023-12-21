#!/usr/bin/env python


def get_new_plots(garden_map: list[list[str]], current_position: tuple[int, int]) -> list[tuple[int, int]]:
    new_plots = []
    i, j = current_position

    # Go North
    if i > 0 and garden_map[i - 1][j] == ".":
        new_plots.append((i - 1, j))
    # Go South
    if i + 1 < len(garden_map) and garden_map[i + 1][j] == ".":
        new_plots.append((i + 1, j))
    # Go east
    if j + 1 < len(garden_map[0]) and garden_map[i][j + 1] == ".":
        new_plots.append((i, j + 1))
    # Go west
    if j > 0 and garden_map[i][j - 1] == ".":
        new_plots.append((i, j - 1))

    return new_plots


def run_steps(garden_map: list[list[str]], start_point: tuple[int, int], num_steps: int) -> list[tuple[int, int]]:
    plots = [start_point]

    for _ in range(num_steps):
        new_plots = []

        while plots:
            current_position = plots.pop(0)
            new_plots += get_new_plots(garden_map, current_position)

        plots = list(set(new_plots))

    return plots


def get_start_point(garden_map: list[list[str]]) -> tuple[int, int]:
    for i, line in enumerate(garden_map):
        for j, c in enumerate(line):
            if c == "S":
                garden_map[i][j] = "."
                return i, j

    raise ValueError("Start Not Found")


def parse(day_input: str) -> list[list[str]]:
    return [
        [c for c in line]
        for line in day_input.split("\n")
    ]


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    garden_map = parse(day_input)

    start_point = get_start_point(garden_map)

    result = run_steps(garden_map, start_point, 64)

    print(len(result))


if __name__ == "__main__":
    main()
