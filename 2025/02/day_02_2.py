#!/usr/bin/env python


def parse(day_input: str) -> list[range]:
    list_id_range: list[range] = []
    for line in day_input.split(","):
        start, end = line.split("-")
        list_id_range += [range(int(start), int(end) + 1)]

    return list_id_range


def chunks_string(string: str, length: int) -> list[str]:
    return [string[i:i + length] for i in range(0, len(string), length)]


def check_list_has_same_number(number_list: list[str]) -> bool:
    if len(number_list) < 2:
        return False

    for i in range(1, len(number_list)):
        if number_list[i] != number_list[i - 1]:
            return False

    return True

def check_invalid_number(number: int) -> bool:
    number_str = str(number)

    for chunk_size in range(1, (len(number_str) // 2) + 1):
        number_list = chunks_string(number_str, chunk_size)
        if check_list_has_same_number(number_list):
            return True

    return False


def count_invalid_ids(id_range: range) -> list[int]:
    invalid_id_list = []

    for number in id_range:
        if check_invalid_number(number):
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
