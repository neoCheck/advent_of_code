#!/usr/bin/env python


def find_zzz(instructions: str,  nodes_map: dict[str, tuple[str, str]]) -> int:
    step = 0
    current_locations = [loc for loc in nodes_map.keys() if loc.endswith("A")]

    while True:
        for i in instructions:
            for n in range(len(current_locations)):
                cl = current_locations[n]

                if i == "L":
                    cl = nodes_map[cl][0]
                elif i == "R":
                    cl = nodes_map[cl][1]

                current_locations[n] = cl

            step += 1
            cl_z = [loc for loc in current_locations if loc.endswith("Z")]
            if len(cl_z) > 2:
                print(f"{step} - {len(cl_z)} : {current_locations}")
            if len(current_locations) == len(cl_z):
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

    print(num_steps)  # 20_220_305_520_997
