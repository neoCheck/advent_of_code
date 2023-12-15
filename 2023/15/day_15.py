#!/usr/bin/env python


def parse(day_input: str) -> list[str]:
    return [line for line in day_input.split(",")]


def get_hash_result(string: str) -> int:
    current_value = 0
    for c in string:
        ascii_code = ord(c)
        current_value += ascii_code
        current_value *= 17
        current_value = current_value % 256

    return current_value


def main():
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    print(sum([get_hash_result(string) for string in parsed_input]))


if __name__ == "__main__":
    main()
