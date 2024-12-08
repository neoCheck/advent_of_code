#!/usr/bin/env python


def parse(day_input: str) -> list[tuple[int, tuple[int, int], tuple[int, int]]]:
    instructions = []
    for line in day_input.split("\n"):
        if line.startswith("turn on "):
            action = 0
            line = line.replace("turn on ", "")
        elif line.startswith("turn off "):
            action = 1
            line = line.replace("turn off ", "")
        elif line.startswith("toggle "):
            action = 2
            line = line.replace("toggle ", "")
        else:
            raise ValueError(f"Unrecognized instruction: {line}")

        start_str, end_str = line.split(" through ")
        start_i, start_j = [int(n) for n in start_str.split(",")]
        end_i, end_j = [int(n) for n in end_str.split(",")]

        instructions.append((action, (start_i, start_j), (end_i, end_j)))

    return instructions


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    instructions = parse(day_input)

    grid: list[list[bool]] = [
        [False for _ in range(1000)]
        for _ in range(1000)
    ]

    for action, (start_i, start_j), (end_i, end_j) in instructions:
        for i in range(start_i, end_i + 1):
            for j in range(start_j, end_j + 1):
                if action == 0:
                    grid[i][j] = True
                elif action == 1:
                    grid[i][j] = False
                elif action == 2:
                    grid[i][j] = not grid[i][j]

    counter = 0
    for row in grid:
        for light in row:
            if light:
                counter += 1

    print(counter)


if __name__ == "__main__":
    main()
