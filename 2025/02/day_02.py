#!/usr/bin/env python


def parse(day_input: str) -> list[range]:
    list_id_range: list[range] = []
    for line in day_input.split(","):
        start, end = line.split("-")
        list_id_range += [range(int(start), int(end) + 1)]

    return list_id_range


def count_invalid_ids(id_range: range) -> list[int]:
    invalid_id_list = []

    for number in id_range:
        number_str = str(number)
        if len(number_str) % 2 == 0:
            first_half = number_str[:len(number_str) // 2]
            second_half = number_str[len(number_str) // 2:]
            if first_half == second_half:
                invalid_id_list.append(number)

    return invalid_id_list


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    list_id_range = parse(day_input)

    list_invalid_id = []
    for id_range in list_id_range:
        list_invalid_id += count_invalid_ids(id_range)

    print(sum(list_invalid_id))


if __name__ == "__main__":
    main()
