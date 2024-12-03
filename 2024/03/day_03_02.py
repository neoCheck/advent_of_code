#!/usr/bin/env python
import re


def main() -> None:
    regex = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)')

    with open("input") as f:
        day_input = f.read().strip()

    split_do = day_input.split('do()')

    multiplications = []
    for instruction in split_do:
        input_to_read = instruction.split("don't()")[0]
        multiplications += regex.findall(input_to_read)

    sum_mult = 0
    for mult in multiplications:
        num_1, num_2 = mult.replace('mul(', '').replace(')', '').split(',')
        sum_mult += int(num_1) * int(num_2)

    print(sum_mult)


if __name__ == "__main__":
    main()
