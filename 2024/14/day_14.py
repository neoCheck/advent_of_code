#!/usr/bin/env python
from dataclasses import dataclass
import math


T_POINT = tuple[int, int]

X_LEN = 101
Y_LEN = 103

# X_LEN = 11
# Y_LEN = 7

QUADRANT_LIST = [
    # (X_START, X_END) (Y_START, Y_END)
    (range(0, X_LEN // 2), range(0, Y_LEN // 2)),
    (range((X_LEN // 2) + 1, X_LEN), range(0, Y_LEN // 2)),
    (range(0, X_LEN // 2), range((Y_LEN // 2) + 1, Y_LEN)),
    (range((X_LEN // 2) + 1, X_LEN), range((Y_LEN // 2) + 1, Y_LEN)),
]


@dataclass
class Robot:
    position: T_POINT
    vector: T_POINT

    def move(self, seconds: int) -> None:
        new_position_x = self.position[0] + seconds * self.vector[0]
        new_position_y = self.position[1] + seconds * self.vector[1]

        if new_position_x < 0:
            fill_x = (new_position_x // (-X_LEN)) + 10
            new_position_x = new_position_x + (fill_x * X_LEN)

        new_position_x = new_position_x % X_LEN

        if new_position_y < 0:
            fill_y = (new_position_y // (-Y_LEN)) + 10
            new_position_y = new_position_y + (fill_y * Y_LEN)

        new_position_y = new_position_y % Y_LEN

        self.position = (new_position_x, new_position_y)


def parse(day_input: str) -> list[Robot]:
    robot_list = []
    for line in day_input.split("\n"):
        p_str, v_str = line.split(" ")
        px, py = map(int, p_str.replace("p=", "").split(","))
        vx, vy = map(int, v_str.replace("v=", "").split(","))
        robot_list.append(
            Robot(position=(px, py), vector=(vx, vy))
        )

    return robot_list


def print_grid(robot_list: list[Robot]) -> None:
    grid = [
        [0 for _ in range(X_LEN)]
        for _ in range(Y_LEN)
    ]
    for robot in robot_list:
        grid[robot.position[1]][robot.position[0]] += 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                print(grid[i][j], end="")
            else:
                print(".", end="")
        print("")

    print("")


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    robot_list = parse(day_input)

    for robot in robot_list:
        robot.move(100)

    quadrant_dict = {
        (x_range, y_range): len([
            robot for robot in robot_list
            if robot.position[0] in x_range and robot.position[1] in y_range
        ])
        for x_range, y_range in QUADRANT_LIST
    }

    print(math.prod(quadrant_dict.values()))


if __name__ == "__main__":
    main()
