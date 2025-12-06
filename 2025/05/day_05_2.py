#!/usr/bin/env python


def parse(day_input: str) -> tuple[list[range], list[int]]:
    ranges, ingredients = day_input.split("\n\n")

    range_list: list[range] = []
    for r in ranges.split("\n"):
        start, end = r.split("-")
        range_list.append(range(int(start), int(end) + 1))

    ingredient_list: list[int] = [int(ingredient) for ingredient in ingredients.split("\n")]

    return range_list, ingredient_list


def combine_ranges(range_list: list[range]) -> list[range]:
    new_ranges: list[range] = []

    while len(range_list) > 0:
        first_range = range_list.pop(0)
        found_index = -1

        for i, second_range in enumerate(range_list):
            if found_index == -1 and (
                    first_range.start in second_range
                    or first_range.stop in second_range
                    or second_range.start in first_range
                    or second_range.stop in first_range
            ):
                found_index = i

        if found_index != -1:
            second_range = range_list.pop(found_index)
            new_range = range(min(first_range.start, second_range.start), max(first_range.stop, second_range.stop))
            new_ranges.append(new_range)
        else:
            new_ranges.append(first_range)

    return new_ranges

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    range_list, _ = parse(day_input)

    current_len = 0
    next_len = len(range_list)

    while current_len != next_len:
        current_len = next_len

        range_list = combine_ranges(range_list)

        next_len = len(range_list)

    print(sum([len(r) for r in range_list]))


if __name__ == "__main__":
    main()
