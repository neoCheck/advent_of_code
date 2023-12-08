#!/usr/bin/env python


def find_zzz(instructions: str,  nodes_map: dict[str, tuple[str, str]]) -> int:
    step = 0
    current_location = "AAA"

    while current_location != "ZZZ":
        for i in instructions:
            if i == "L":
                current_location = nodes_map[current_location][0]
            elif i == "R":
                current_location = nodes_map[current_location][1]

            step += 1
            if current_location == "ZZZ":
                return step

    return -1


def create_map(map_str: str) -> dict[str, tuple[str, str]]:
    nodes_map = {}

    for m in map_str.split("\n"):
        origin, left_right = m.split(" = ")
        left_right = left_right.replace("(", "").replace(")", "").replace(" ", "")
        left, right = left_right.split(",")

        nodes_map[origin] = (left, right)

    return nodes_map


def parse(day_input: str) -> tuple[str, dict[str, tuple[str, str]]]:
    instructions_str, map_str = day_input.split("\n\n")

    instructions: str = instructions_str.strip()

    nodes_map = create_map(map_str)

    return instructions,  nodes_map


if __name__ == "__main__":
    input_ = open("input").read().strip()

    left_right_instructions, map_ = parse(input_)
    num_steps = find_zzz(left_right_instructions, map_)

    print(num_steps)
