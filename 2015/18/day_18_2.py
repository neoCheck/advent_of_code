#!/usr/bin/env python


def parse(day_input: str) -> list[list[bool]]:
    return [
        [c == "#" for c in line]
        for line in day_input.split("\n")
    ]

def turn_on_corners(grid: list[list[bool]]) -> list[list[bool]]:
    grid[0][0] = True
    grid[0][-1] = True
    grid[-1][-1] = True
    grid[-1][0] = True
    return grid


def get_neighbour_lights(grid: list[list[bool]], i: int, j: int) -> list[bool]:
    neighbours = []
    if i > 0: # UP
        neighbours.append(grid[i - 1][j])
    if i < len(grid) - 1: # DOWN
        neighbours.append(grid[i + 1][j])
    if j > 0: # LEFT
        neighbours.append(grid[i][j - 1])
    if j < len(grid[i]) - 1: # RIGHT
        neighbours.append(grid[i][j + 1])
    if i > 0 and j > 0: # UP LEFT
        neighbours.append(grid[i - 1][j - 1])
    if i > 0 and (j < len(grid[i]) - 1): # UP RIGHT
        neighbours.append(grid[i - 1][j + 1])
    if (i < len(grid) - 1) and j > 0: # DOWN LEFT
        neighbours.append(grid[i + 1][j - 1])
    if (i < len(grid) - 1) and (j < len(grid[i]) - 1): # DOWN RIGHT
        neighbours.append(grid[i + 1][j + 1])

    return neighbours


def do_one_step(grid: list[list[bool]]) -> list[list[bool]]:
    new_grid = []

    for i in range(len(grid)):
        line = []
        for j in range(len(grid[i])):
            neighbours = get_neighbour_lights(grid, i, j)
            on_lights = len([n for n in neighbours if n])
            if grid[i][j]:
                line.append(on_lights in (2, 3))
            else:
                line.append(on_lights == 3)

        new_grid.append(line)

    return new_grid



def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    grid = parse(day_input)
    grid = turn_on_corners(grid)

    for i in range(100):
        grid = do_one_step(grid)
        grid = turn_on_corners(grid)


    print(sum([len([line for light in line if light]) for line in grid]))


if __name__ == "__main__":
    main()
