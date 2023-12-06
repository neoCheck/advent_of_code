#!/usr/bin/env python

SYMBOLS = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']


def get_line_number(line: str, j: int):
    number_start = j
    len_columns = len(line)

    while number_start >= 0 and line[number_start].isdigit():
        number_start -= 1
    number_start += 1

    number_end = j
    while number_end < len_columns and line[number_end].isdigit():
        number_end += 1
    number_end -= 1

    return number_end, line[number_start:number_end + 1]


def has_a_symbol_adjacent(file_input: list[str], i: int, j: int) -> bool:
    len_lines = len(file_input)
    len_columns = len(file_input[0])
    return ((i - 1 >= 0 and file_input[i - 1][j] in SYMBOLS)  # Check TOP
            or (i - 1 >= 0 and j - 1 >= 0 and file_input[i - 1][j - 1] in SYMBOLS)  # Check TOP LEFT
            or (i - 1 >= 0 and j + 1 < len_columns and file_input[i - 1][j + 1] in SYMBOLS)  # Check TOP RIGHT
            or (j - 1 >= 0 and file_input[i][j - 1] in SYMBOLS)  # Check LEFT
            or (j + 1 < len_columns and file_input[i][j + 1] in SYMBOLS)  # Check RIGHT
            or (i + 1 < len_lines and file_input[i + 1][j] in SYMBOLS)  # Check BOTTOM
            or (i + 1 < len_lines and j + 1 < len_columns and file_input[i + 1][j + 1] in SYMBOLS)  # Check BOTTOM RIGHT
            or (i + 1 < len_lines and j - 1 >= 0 and file_input[i + 1][j - 1] in SYMBOLS)  # Check BOTTOM LEFT
            )


def get_adjacent_numbers(file_input: list[str]) -> list[int]:
    ad_numbers_list = ""
    seperator = ":"

    for i, line in enumerate(file_input):
        j = 0
        len_columns = len(line)
        line_num_list = ""
        while j < len_columns:
            column = line[j]

            if column.isdigit() and has_a_symbol_adjacent(file_input, i, j):
                j, number = get_line_number(line, j)
                line_num_list = f"{line_num_list}{number}{seperator}"
            else:
                if not line_num_list.endswith(seperator):
                    line_num_list = f"{line_num_list}{seperator}"

            j += 1
        ad_numbers_list = f"{ad_numbers_list}{seperator}{line_num_list}"

    return [int(d) for d in ad_numbers_list.split(seperator) if d.isdigit()]


if __name__ == "__main__":
    input_ = open("input").read().strip()
    ad_numbers = get_adjacent_numbers(input_.split("\n"))
    print(sum(ad_numbers))
