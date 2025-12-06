#!/usr/bin/env python


def chunks_string(string: str, length: int = 1) -> list[str]:
    return [string[i:i + length] for i in range(0, len(string), length)]


def parse(day_input: str) -> list[list[int]]:
    return [
        [int(digit) for digit in chunks_string(line)]
        for line in day_input.split("\n")
    ]


def get_largest_jolts(banks: list[int]) -> int:
    largest_first_digit = max(banks[:-1])
    index_largest_first_digit = banks.index(largest_first_digit)

    rest_banks = banks[index_largest_first_digit + 1:]
    largest_second_digit = max(rest_banks)

    return int(f"{largest_first_digit}{largest_second_digit}")



def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    banks_list = parse(day_input)

    counter = 0
    for banks in banks_list:
        counter += get_largest_jolts(banks)

    print(counter)


if __name__ == "__main__":
    main()
