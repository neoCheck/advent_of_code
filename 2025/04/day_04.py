#!/usr/bin/env python


def parse(day_input: str) -> list[list[int]]:
    return [
        [0 if c == '.' else 1 for c in line]
        for line in day_input.split("\n")
    ]

def get_number_surrounding_paper(diagram: list[list[int]], row: int, col: int) -> int:
    paper_count = 0

    if row > 0 and col > 0:
        paper_count += diagram[row-1][col-1]
    if row > 0:
        paper_count += diagram[row-1][col]
    if row > 0 and col < len(diagram[row-1]) - 1:
        paper_count += diagram[row-1][col+1]

    if col > 0:
        paper_count += diagram[row][col-1]
    if col < len(diagram[row]) - 1:
        paper_count += diagram[row][col+1]

    if row < len(diagram) - 1 and col > 0:
        paper_count += diagram[row+1][col-1]
    if row < len(diagram) - 1:
        paper_count += diagram[row+1][col]
    if row < len(diagram) - 1 and col < len(diagram[row+1]) - 1:
        paper_count += diagram[row+1][col+1]

    return paper_count

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    diagram = parse(day_input)

    counter = 0
    for row in range(len(diagram)):
        for col in range(len(diagram[row])):
            if diagram[row][col] == 1 and get_number_surrounding_paper(diagram, row, col) < 4:
                counter += 1

    print(counter)


if __name__ == "__main__":
    main()
