#!/usr/bin/env python
from dataclasses import dataclass
from PIL import Image
from pathlib import Path


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


def image_grid(robot_list: list[Robot]) -> Image:
    image = Image.new("RGB", (X_LEN, Y_LEN))
    pixels = image.load()

    for robot in robot_list:
        pixels[robot.position[0], robot.position[1]] = (255, 255, 255)

    return image


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    for i in range(((X_LEN * Y_LEN) // 1_000) + 1):
        Path(f"help/{i}").mkdir(parents=True, exist_ok=True)

    robot_list = parse(day_input)

    for i in range(X_LEN * Y_LEN):
        for robot in robot_list:
            robot.move(1)

        image = image_grid(robot_list)
        image.save(f"help/{i // 1_000}/{i + 1}.png")


if __name__ == "__main__":
    main()
