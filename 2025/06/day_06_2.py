#!/usr/bin/env python


def parse(day_input: str) -> list[tuple[str, list[int]]]:
    lines = [line for line in day_input.split("\n")]

    new_lines = []
    for _ in range(len(lines[0])):
        new_lines.append([])

    for line in lines:
        for i in range(len(line)):
            new_lines[i].append(line[i])

    new_lines = ["".join(line).strip() for line in new_lines]

    to_be_parsed = "\n".join(new_lines)
    calculations_list = to_be_parsed.split("\n\n")

    parsed_lines: list[tuple[str, list[int]]] = []
    for line in calculations_list:
        numbers: list[int] = []

        numbers_list = line.split("\n")
        first_number_str = numbers_list.pop(0)
        operation = first_number_str[-1]
        numbers.append(int(first_number_str[:-1].strip()))
        numbers += [int(n_str.strip()) for n_str in numbers_list]

        parsed_lines.append((operation, numbers))

    return parsed_lines


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

    parsed_lines = parse(day_input)

    counter = 0
    for operation, numbers in parsed_lines:
        counter += do_operation(operation, numbers)

    print(counter)

if __name__ == "__main__":
    main()
