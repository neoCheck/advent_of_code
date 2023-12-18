#!/usr/bin/env python


def count_blocks(filled_map: list[list[str]]) -> int:
    count = 0

    for line in filled_map:
        for block in line:
            if block == "#":
                count += 1

    return count


def count_edges(trimmed_map: list[list[str]], block_i: int, block_j: int) -> int:
    i = block_i
    j = block_j
    count = 0
    while j >= 0:
        if trimmed_map[i][j] == "#":
            if trimmed_map[i][j - 1] == "#":
                first_block = j

                while trimmed_map[i][j] == "#":
                    j -=1
                j += 1
                last_block = j

                if ((trimmed_map[i + 1][first_block] == "#" and trimmed_map[i + 1][last_block] == "#") or
                    (trimmed_map[i - 1][first_block] == "#" and trimmed_map[i - 1][last_block] == "#")):
                    count += 1

            else:
                pass

            count += 1
        j -= 1

    return count


def fill_map(trimmed_map: list[list[str]]) -> list[list[str]]:
    fill_list = []

    for i in range(len(trimmed_map)):
        for j in range(len(trimmed_map[0])):
            if trimmed_map[i][j] == ".":
                count = count_edges(trimmed_map, i, j)
                if count % 2 == 1:
                    fill_list.append((i, j))

    for i, j in fill_list:
        trimmed_map[i][j] = "#"

    return trimmed_map


def trim_giant_map(giant_map: list[list[str]]) -> list[list[str]]:
    i_list = []
    j_list = []

    for i, line in enumerate(giant_map):
        for j, block in enumerate(line):
            if block == "#":
                i_list.append(i)
                j_list.append(j)

    min_i = min(i_list)
    min_j = min(j_list)
    max_i = max(i_list)
    max_j = max(j_list)

    return [
        line[min_j - 5: max_j + 5]
        for line in giant_map[min_i - 5: max_i + 5]
    ]


def draw_on_map(empty_map: list[list[str]], directions_input: list[tuple[str, int, str]]) -> list[list[str]]:
    i = 1_000
    j = 1_000

    empty_map[i][j] = "#"
    for direction, blocks, color in directions_input:

        if direction == "R":
            new_j = j + blocks
            while j < new_j:
                j += 1
                empty_map[i][j] = "#"
        elif direction == "L":
            new_j = j - blocks
            while j > new_j:
                j -= 1
                empty_map[i][j] = "#"
        elif direction == "U":
            new_i = i - blocks
            while i > new_i:
                i -= 1
                empty_map[i][j] = "#"
        elif direction == "D":
            new_i = i + blocks
            while i < new_i:
                i += 1
                empty_map[i][j] = "#"

    return empty_map


def print_empty_map(empty_map: list[list[str]]) -> None:

    for line in empty_map:
        for c in line:
            print(c, end="")

        print("")


def generate_giant_map() -> list[list[str]]:
    return [
        ["." for _ in range(2_000)]
        for _ in range(2_000)
    ]


def parse(day_input: str) -> list[tuple[str, int, str]]:
    parsed_list = []
    for line in day_input.split("\n"):
        direction, blocks, color = line.split(" ")
        parsed_list.append((direction, int(blocks), color))

    return parsed_list


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)
    empty_map = generate_giant_map()
    giant_map = draw_on_map(empty_map, parsed_input)
    trimmed_map = trim_giant_map(giant_map)
    filled_map = fill_map(trimmed_map)
    print(count_blocks(filled_map))
    # print_empty_map(filled_map)


if __name__ == "__main__":
    # See part 2, simpler (used Shoelace formula)
    main()
