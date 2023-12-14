#!/usr/bin/env python


def calculate_load(platform: list[list[str]]) -> int:
    return sum([
        (len(platform) - i) * len([c for c in line if c == "O"])
        for i, line in enumerate(platform)
    ])


def move_rocks_to_north(platform: list[list[str]]) -> None:
    for j in range(len(platform[0])):

        for i in range(len(platform)):
            p = platform[i][j]

            if p == "O":
                counter = 0
                while i - counter > 0 and platform[i - (counter + 1)][j] == ".":
                    counter += 1

                if counter > 0:
                    platform[i - counter][j] = "O"
                    platform[i][j] = "."


def parse(day_input: str) -> list[list[str]]:
    return [
        [c for c in line]
        for line in day_input.split("\n")
    ]


def print_platform(platform: list[list[str]]):
    for line in platform:
        for c in line:
            print(c, end="")

        print("")


def main():
    with open("input") as f:
        day_input = f.read().strip()

    platform = parse(day_input)
    print_platform(platform)

    move_rocks_to_north(platform)
    print("")
    print_platform(platform)

    load = calculate_load(platform)
    print(load)


if __name__ == "__main__":
    main()
