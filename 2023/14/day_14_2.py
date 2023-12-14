#!/usr/bin/env python


def calculate_load(platform: list[list[str]]) -> int:
    return sum([
        (len(platform) - i) * len([c for c in line if c == "O"])
        for i, line in enumerate(platform)
    ])


def move_rocks_to_north(platform: list[list[str]]) -> list[list[str]]:
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

    return platform


def move_rocks_to_south(platform: list[list[str]]) -> list[list[str]]:
    platform.reverse()
    platform = move_rocks_to_north(platform)
    platform.reverse()

    return platform


def move_rocks_to_west(platform: list[list[str]]) -> list[list[str]]:
    platform = [
        [f"{platform[i][j]}" for i in range(len(platform))]
        for j in range(len(platform[0]))
    ]
    platform = move_rocks_to_north(platform)
    platform = [
        [f"{platform[i][j]}" for i in range(len(platform))]
        for j in range(len(platform[0]))
    ]

    return platform


def move_rocks_to_east(platform: list[list[str]]) -> list[list[str]]:
    platform = list(reversed([
        list(reversed([f"{platform[i][j]}" for i in range(len(platform))]))
        for j in range(len(platform[0]))
    ]))
    platform = move_rocks_to_north(platform)
    platform = list(reversed([
        list(reversed([f"{platform[i][j]}" for i in range(len(platform))]))
        for j in range(len(platform[0]))
    ]))
    return platform


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

    print("\n\n")


def main():
    with open("input") as f:
        day_input = f.read().strip()

    platform = parse(day_input)

    load_list = []

    min_cycle_todo = max(100, len(platform) * 2)

    for i in range(min_cycle_todo):
        platform = move_rocks_to_north(platform)
        platform = move_rocks_to_west(platform)
        platform = move_rocks_to_south(platform)
        platform = move_rocks_to_east(platform)

        load_list.append(calculate_load(platform))

    # Get Cycle
    picked_position = int(min_cycle_todo / 2)
    cycle_start = load_list[picked_position]
    cycle_length = load_list[picked_position + 1:].index(cycle_start) + 1
    cycle = load_list[picked_position: picked_position + cycle_length]

    # Get number in cycle
    num_cycles_to_do = 1_000_000_000
    position_in_cycle = (num_cycles_to_do - picked_position - 1) % cycle_length
    res = cycle[position_in_cycle]
    print(res)


if __name__ == "__main__":
    main()
