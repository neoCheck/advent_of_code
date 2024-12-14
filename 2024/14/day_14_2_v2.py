#!/usr/bin/env python
from dataclasses import dataclass


T_POINT = tuple[int, int]

X_LEN = 101
Y_LEN = 103

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


def get_max_successive_robots_in_grid(robot_list: list[Robot]) -> int:
    max_count = 1

    for y in range(Y_LEN):
        current_count = 1
        robot_line = [r for r in robot_list if r.position[1] == y]
        x_list = sorted(list(set([r.position[0] for r in robot_line])))
        for i in range(1, len(x_list)):
            if x_list[i] == (x_list[i - 1] + 1):
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

    return max_count


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    robot_list = parse(day_input)

    for i in range(1, X_LEN * Y_LEN + 1):
        for robot in robot_list:
            robot.move(1)

        max_count = get_max_successive_robots_in_grid(robot_list)
        if max_count > 20:
            print(i)
            return


if __name__ == "__main__":
    main()

