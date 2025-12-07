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

def transform_diagram(diagram: list[list[str]]) -> list[list[int]]:
    new_diagram = []
    for row in diagram:
        new_diagram_row: list[int] = []
        for item in row:
            if item == "^":
                new_diagram_row.append(-1)
            elif item == "|":
                new_diagram_row.append(1)
            else:
                new_diagram_row.append(0)

        new_diagram.append(new_diagram_row)

    return new_diagram


def move_beam(diagram: list[list[int]]) -> list[list[int]]:
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):

            if diagram[i][j] > 0:
                if i < (len(diagram) - 1):
                    if diagram[i+1][j] == -1:
                        if j > 0:
                            diagram[i+1][j-1] += diagram[i][j]
                        if j < (len(diagram[i+1]) - 1):
                            diagram[i+1][j+1] += diagram[i][j]
                    else:
                        diagram[i+1][j] += diagram[i][j]

    return diagram


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    diagram = set_first_beam(diagram=parse(day_input))
    new_diagram = transform_diagram(diagram=diagram)
    new_diagram = move_beam(diagram=new_diagram)
    print(sum(new_diagram[-1]))


if __name__ == "__main__":
    main()
