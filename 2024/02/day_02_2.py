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


def is_safe_2(list_num: list[int]) -> bool:
    for i in range(len(list_num)):
        new_list = [num for j, num in enumerate(list_num) if i != j]
        if is_safe(new_list):
            return True

    return False


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    safe_list = [list_num for list_num in parsed_input if is_safe(list_num)]

    not_safe_list = [list_num for list_num in parsed_input if not is_safe(list_num)]

    safe_2_list = [list_num for list_num in not_safe_list if is_safe_2(list_num)]
    print(len(safe_list) + len(safe_2_list))


if __name__ == "__main__":
    main()
