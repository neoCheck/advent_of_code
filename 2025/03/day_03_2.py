#!/usr/bin/env python


def chunks_string(string: str, length: int = 1) -> list[str]:
    return [string[i:i + length] for i in range(0, len(string), length)]


def parse(day_input: str) -> list[list[int]]:
    return [
        [int(digit) for digit in chunks_string(line)]
        for line in day_input.split("\n")
    ]


def get_largest_jolts(banks: list[int]) -> int:
    highest_jolts: list[int] = []
    remaining_jolts = 12
    index = 0
    banks_selection = banks[index:]
    while remaining_jolts > 0:
        remaining_jolts -= 1
        if remaining_jolts != 0:
            largest_digit = max(banks_selection[:-remaining_jolts])
        else:
            largest_digit = max(banks_selection)

        highest_jolts.append(largest_digit)

        index = banks_selection.index(largest_digit) + 1
        banks_selection = banks_selection[index:]


    return int("".join(map(str, highest_jolts)))


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
