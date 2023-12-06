#!/usr/bin/env python


NUMBER = {
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


def get_line_number(line_input: str) -> int:
    digits = []
    prev = ""
    for c in line_input:
        if c.isdigit():
            digits.append(c)

        prev = f"{prev}{c}"
        for nb_str, digit_str in NUMBER.items():
            if prev.endswith(nb_str):
                digits.append(digit_str)

    if not digits:
        return 0
    return int(f"{digits[0]}{digits[-1]}")


if __name__ == "__main__":
    input_ = open("input").read().strip()
    num = sum(get_line_number(line) for line in input_.split('\n'))
    print(num)  # 54875
