#!/usr/bin/env python
from collections import defaultdict


def get_the_power_of_cubes(cube_sets: dict[str, int]):
    value = 1
    for v in cube_sets.values():
        value = value * v

    return value


def merge_dict_max_value(dict_list: list[dict[str, int]]) -> dict[str, int]:
    data = defaultdict(int)
    for d in dict_list:
        for key, value in d.items():
            data[key] = max(data[key], value)

    return data


def parse_set(game_set: str):
    data = {}
    cubes = game_set.split(", ")

    for c in cubes:
        nb, cube_type = c.split(" ")
        data[cube_type] = int(nb)

    return data


def parse_info(game_input: str):
    game_id, game_sets = game_input.split(": ")
    # game_id = int(game_id.replace("Game ", ""))

    game_sets = [parse_set(game_set) for game_set in game_sets.split("; ")]
    cube_max_values = merge_dict_max_value(game_sets)

    return get_the_power_of_cubes(cube_max_values)


def check_minimum_cubes(info):
    game_id, cube_max_values = info
    minimum = {"red": 12, "green": 13, "blue": 14}

    for cube_type, minimum in minimum.items():
        if cube_max_values[cube_type] > minimum:
            return False

    return True


if __name__ == "__main__":
    input_ = open("input").read().strip()
    info_list = [parse_info(line) for line in input_.split("\n")]

    print(sum(info_list))
    # print(result)
