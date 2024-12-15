#!/usr/bin/env python


EMPTY = 0
WALL = 1
BOX = 2
ROBOT = 3

T_POINT = tuple[int, int]

SPOT_MAPPING: dict[str, int] = {
    ".": EMPTY,
    "#": WALL,
    "O": BOX,
    "@": ROBOT,
}

T_DIRECTION = tuple[int, int]

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTION_MAPPING: dict[str, T_DIRECTION] = {
    "^": UP,
    "v": DOWN,
    "<": LEFT,
    ">": RIGHT,
}


def parse_grid(day_input: str) -> list[list[int]]:
    return [
        [SPOT_MAPPING[c] for c in line]
        for line in day_input.split("\n\n")[0].split("\n")
    ]

def get_robot_position(grid: list[list[int]]) -> T_POINT:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ROBOT:
                return i, j

    raise ValueError("No robot found")


def parse_directions(day_input: str) -> list[T_DIRECTION]:
    return [DIRECTION_MAPPING[c] for line in day_input.split("\n\n")[1].split("\n") for c in line if line]


def can_move_robot_and_boxes(grid: list[list[int]], robot_position: T_POINT, direction: T_DIRECTION) -> tuple[bool, int]:
    for i in range(1, len(grid)):
        next_pos_i = robot_position[0] + (i * direction[0])
        next_pos_j = robot_position[1] + (i * direction[1])
        spot = grid[next_pos_i][next_pos_j]
        if spot == WALL:
            return False, i
        elif spot == EMPTY:
            return True, i

    raise ValueError("No valid spot found")


def move_robot_and_boxes(grid: list[list[int]], robot_position: T_POINT, direction: T_DIRECTION, spots: int) -> T_POINT:
    for i in reversed(range(spots)):
        current_pos_i = robot_position[0] + (i * direction[0])
        current_pos_j = robot_position[1] + (i * direction[1])
        next_pos_i = robot_position[0] + ((i + 1) * direction[0])
        next_pos_j = robot_position[1] + ((i + 1) * direction[1])

        grid[next_pos_i][next_pos_j] = grid[current_pos_i][current_pos_j]
        grid[current_pos_i][current_pos_j] = EMPTY

    return robot_position[0] + direction[0], robot_position[1] + direction[1]


def print_grid(grid: list[list[int]]) -> None:
    for row in grid:
        for c in row:
            show_c = "."
            if c == WALL:
                show_c = "#"
            elif c == BOX:
                show_c = "O"
            elif c == ROBOT:
                show_c = "@"
            print(show_c, end="")
        print("")

    print("\n\n")


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    grid = parse_grid(day_input)
    directions = parse_directions(day_input)
    robot_position = get_robot_position(grid)

    for direction in directions:
        can_move, spots = can_move_robot_and_boxes(grid, robot_position, direction)
        if can_move:
            robot_position = move_robot_and_boxes(grid, robot_position, direction, spots)

    sum_boxes = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == BOX:
                sum_boxes += (100 * i) + j

    print(sum_boxes)

if __name__ == "__main__":
    main()
