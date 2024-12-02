#!/usr/bin/env python


def parse(day_input: str) -> list[list[int]]:
    return [
        [int(num) for num in line.split(" ")]
        for line in day_input.split("\n")
    ]

def is_safe(list_num: list[int]) -> bool:
    distance_list: list[int] = [list_num[i] - list_num[i + 1] for i in range(len(list_num) - 1)]

    if any(distance == 0 or distance < -3 or distance > 3 for distance in distance_list):
        return False

    if distance_list[0] < 0 and all(distance < 0 for distance in distance_list):
        return True

    if distance_list[0] > 0 and all(distance > 0 for distance in distance_list):
        return True

    return False


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    print(sum(
        1 for list_num in parsed_input
        if is_safe(list_num)
    ))


if __name__ == "__main__":
    main()
