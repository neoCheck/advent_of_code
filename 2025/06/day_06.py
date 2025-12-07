#!/usr/bin/env python


def parse(day_input: str) -> tuple[list[list[int]], list[str]]:
    lines = [line.split() for line in day_input.split("\n")]
    operators_list = lines.pop()
    num_list = [
        [int(digit) for digit in line]
        for line in lines
    ]

    return num_list, operators_list


def do_operation(operation: str, numbers: list[int]) -> int:
    result = numbers.pop(0)

    while len(numbers):
        second_number = numbers.pop(0)

        if operation == "+":
            result += second_number
        elif operation == "*":
            result *= second_number

    return result


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    numbers_list, operators_list = parse(day_input)

    counter = 0
    for i in range(len(numbers_list[0])):
        counter += do_operation(operators_list[i], [num_list[i] for num_list in numbers_list])

    print(counter)


if __name__ == "__main__":
    main()
