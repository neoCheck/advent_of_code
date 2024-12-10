#!/usr/bin/env python

TRAIL_HEAD = 0
MAX_HEIGHT = 9
T_POS = tuple[int, int]

def parse(day_input: str) -> list[list[int]]:
    return [
        [int(c) for c in line]
        for line in day_input.split("\n")
    ]

def look_for_reachable_max_height(grid: list[list[int]], path_walk: list[T_POS]) -> list[list[T_POS]]:
    i, j = path_walk[-1]
    next_positions: list[T_POS] = []
    height = grid[i][j]

    if height == MAX_HEIGHT:
        return [path_walk]

    if i - 1 >= 0 and grid[i - 1][j] == height + 1:
        next_positions.append((i - 1, j))
    if i + 1 < len(grid) and grid[i + 1][j] == height + 1:
        next_positions.append((i + 1, j))
    if j - 1 >= 0 and grid[i][j - 1] == height + 1:
        next_positions.append((i, j - 1))
    if j + 1 < len(grid[0]) and grid[i][j + 1] == height + 1:
        next_positions.append((i, j + 1))

    potential_paths = [
        path_walk + [pos]
        for pos in next_positions
        if pos not in path_walk
    ]

    paths = []
    for potential_path in potential_paths:
        paths += look_for_reachable_max_height(grid, potential_path)

    return paths


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    grid = parse(day_input)

    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == TRAIL_HEAD:
                paths = look_for_reachable_max_height(grid, [(i, j)])
                score += len(paths)

    print(score)


if __name__ == "__main__":
    main()
