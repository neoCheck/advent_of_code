#!/usr/bin/env python
from copy import deepcopy


T_POS = tuple[int, int]
T_GRID = list[list[str]]


def walk(
        grid: T_GRID,
        previous_steps: list[T_POS],
        start: T_POS,
        end: T_POS
) -> tuple[list[list[T_POS]], list[tuple[list[T_POS], T_POS]]]:
    current_pos = start

    next_pos_list: list[T_POS] = []
    previous_steps.append(current_pos)
    while current_pos != end:
        next_pos_list = []
        if grid[current_pos[0]][current_pos[1]] == ".":
            for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
                if (
                        next_pos not in previous_steps and
                        next_pos[0] in range(len(grid)) and
                        next_pos[1] in range(len(grid[0])) and
                        grid[next_pos[0]][next_pos[1]] != "#"
                ):
                    next_pos_list.append(next_pos)
        elif grid[current_pos[0]][current_pos[1]] == ">":
            next_pos = (current_pos[0], current_pos[1] + 1)
            if next_pos not in previous_steps:
                next_pos_list.append(next_pos)
        elif grid[current_pos[0]][current_pos[1]] == "v":
            next_pos = (current_pos[0] + 1, current_pos[1])
            if next_pos not in previous_steps:
                next_pos_list.append(next_pos)
        else:
            raise ValueError("Bad")

        if len(next_pos_list) == 1:
            previous_steps.append(next_pos_list[0])
            current_pos = next_pos_list[0]
        else:
            break

    if len(next_pos_list) >= 2:
        return [], [(deepcopy(previous_steps), nx) for nx in next_pos_list]
    else:
        return [previous_steps], []


def parse(day_input: str) -> T_GRID:
    return [
        [c for c in line]
        for line in day_input.split("\n")
    ]


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    grid = parse(day_input)

    start = (0, 1)
    end = (len(grid) - 1, len(grid[0]) - 2)

    paths = []
    paths_to_walk = [([], start)]
    while paths_to_walk:
        previous_steps, nx = paths_to_walk.pop(0)
        finished, new_paths_to_walk = walk(grid, previous_steps, nx, end)
        paths += finished
        paths_to_walk += new_paths_to_walk

    len_paths = [len(p) - 1 for p in paths if p[-1] == end]
    print(max(len_paths))


if __name__ == "__main__":
    main()
