#!/usr/bin/env python


def parse(day_input: str) -> tuple[list[int], list[int]]:
    list_1: list[int] = []
    list_2: list[int] = []
    for line in day_input.splitlines():
        number_list_1, number_list_2 = line.split("   ")
        list_1.append(int(number_list_1))
        list_2.append(int(number_list_2))
    return list_1, list_2


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    list_1, list_2 = parse(day_input)

    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    sum_distance = 0
    for i in range(len(list_1)):
        distance = abs(list_1[i] - list_2[i])
        sum_distance += distance

    print(sum_distance)


if __name__ == "__main__":
    main()
