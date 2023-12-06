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


def get_adjacent_digits(file_input: list[str], i: int, j: int) -> list[str]:
    number_list = []
    len_lines = len(file_input)
    len_columns = len(file_input[0])

    if i - 1 >= 0 and file_input[i - 1][j].isdigit():  # Check TOP
        number_list.append(get_line_number(file_input[i - 1], j)[1])

    if i - 1 >= 0 and j - 1 >= 0 and file_input[i - 1][j - 1].isdigit():  # Check TOP LEFT
        number_list.append(get_line_number(file_input[i - 1], j - 1)[1])

    if i - 1 >= 0 and j + 1 < len_columns and file_input[i - 1][j + 1].isdigit():  # Check TOP RIGHT
        number_list.append(get_line_number(file_input[i - 1], j + 1)[1])

    if j - 1 >= 0 and file_input[i][j - 1].isdigit():  # Check LEFT
        number_list.append(get_line_number(file_input[i], j - 1)[1])

    if j + 1 < len_columns and file_input[i][j + 1].isdigit():  # Check RIGHT
        number_list.append(get_line_number(file_input[i], j + 1)[1])

    if i + 1 < len_lines and file_input[i + 1][j].isdigit():  # Check BOTTOM
        number_list.append(get_line_number(file_input[i + 1], j)[1])

    if i + 1 < len_lines and j + 1 < len_columns and file_input[i + 1][j + 1].isdigit():  # Check BOTTOM RIGHT
        number_list.append(get_line_number(file_input[i + 1], j + 1)[1])

    if i + 1 < len_lines and j - 1 >= 0 and file_input[i + 1][j - 1].isdigit():  # Check BOTTOM LEFT
        number_list.append(get_line_number(file_input[i + 1], j - 1)[1])

    return number_list


def get_power_gear(ad_nums: list[str]) -> int:
    power_gear = 1

    for n in ad_nums:
        power_gear = power_gear * int(n)

    return power_gear


def get_adjacent_numbers(file_input: list[str]) -> list[int]:
    ad_numbers_list = []

    for i, line in enumerate(file_input):
        for j, column in enumerate(line):
            if column == "*":
                ad_nums = get_adjacent_digits(file_input, i, j)
                ad_nums = list(set(ad_nums))
                if len(ad_nums) >= 2:
                    power_gear = get_power_gear(ad_nums)
                    ad_numbers_list.append(power_gear)

    return ad_numbers_list


if __name__ == "__main__":
    input_ = open("input").read().strip()
    ad_numbers = get_adjacent_numbers(input_.split("\n"))
    print(sum(ad_numbers))
