#!/usr/bin/env python
import math


def parse(day_input: str) -> list[int]:
    return [int(line) for line in day_input.split(" ")]


def blink(num_list: list[int]) -> list[int]:
    new_list = []
    for num in num_list:
        if num == 0:
            new_list.append(1)
        elif (num_digits := int(math.log10(num)) + 1) % 2 == 0:
            middle_divider = 10**(num_digits/2)
            first_half = int(num / middle_divider)
            second_half = int(num % middle_divider)
            new_list += [first_half, second_half]
        else:
            new_list.append(num * 2024)

    return new_list

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    num_list = parse(day_input)

    for i in range(25):
        num_list = blink(num_list)


    print(len(num_list))


if __name__ == "__main__":
    main()
