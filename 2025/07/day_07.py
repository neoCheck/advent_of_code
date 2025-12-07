#!/usr/bin/env python


def parse(day_input: str) -> list[list[str]]:
    return [
        [s for s in line]
        for line in day_input.split("\n")
    ]

def set_first_beam(diagram: list[list[str]]) -> list[list[str]]:
    for j in range(len(diagram[0])):
        if diagram[0][j] == "S":
            diagram[0][j] = "|"

    return diagram

def move_beam(diagram: list[list[str]]) -> list[list[str]]:
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] == "|":
                if i < (len(diagram) - 1):
                    if diagram[i+1][j] == "^":
                        if j > 0:
                            diagram[i+1][j-1] = "|"
                        if j < (len(diagram[i+1]) - 1):
                            diagram[i+1][j+1] = "|"
                    else:
                        diagram[i+1][j] = "|"

    return diagram

def count_split_beams(diagram: list[list[str]]) -> int:
    counter = 0

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] == "^" and i > 0 and diagram[i-1][j] == "|":
                counter += 1

    return counter


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    diagram = set_first_beam(diagram=parse(day_input))
    diagram = move_beam(diagram)
    counter = count_split_beams(diagram)
    print(counter)


if __name__ == "__main__":
    main()
