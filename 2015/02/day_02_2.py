#!/usr/bin/env python


def parse(day_input: str) -> list[list[int]]:
    return [
        [int(n) for n in line.split("x")]
        for line in day_input.split("\n")
    ]


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    ribbon = 0
    for length, width, height in parsed_input:
        smallest, second_smallest = sorted([length, width, height])[:2]
        ribbon += smallest + smallest + second_smallest + second_smallest
        ribbon += length * width * height

    print(ribbon)


if __name__ == "__main__":
    main()
