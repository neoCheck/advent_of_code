#!/usr/bin/env python

import re


NUMBER_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_with_actual_digit(number: str) -> str:
    return NUMBER_MAPPING.get(number) or number


def get_line_number(line_input: str) -> int:
    digits = re.findall(r'(?=(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9))', line_input)
    digits = [replace_with_actual_digit(number) for number in digits]

    if not digits:
        return 0
    return int(f"{digits[0]}{digits[-1]}")


if __name__ == "__main__":
    input_ = open("input").read().strip()
    num = sum(get_line_number(line) for line in input_.split('\n'))
    print(num)
