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

    surface = 0
    for length, width, height in parsed_input:
        surface += (2 * length * width) + (2 * width * height) + (2 * height * length)
        surface += min((length * width), (width * height), (height * length))

    print(surface)


if __name__ == "__main__":
    main()
