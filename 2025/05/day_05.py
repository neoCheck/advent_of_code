#!/usr/bin/env python


def parse(day_input: str) -> tuple[list[range], list[int]]:
    ranges, ingredients = day_input.split("\n\n")

    range_list: list[range] = []
    for r in ranges.split("\n"):
        start, end = r.split("-")
        range_list.append(range(int(start), int(end) + 1))

    ingredient_list: list[int] = [int(ingredient) for ingredient in ingredients.split("\n")]

    return range_list, ingredient_list


def is_ingredient_fresh(ingredient: int, fresh_ranges: list[range]) -> bool:
    for r in fresh_ranges:
        if ingredient in r:
            return True

    return False

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    range_list, ingredient_list = parse(day_input)

    counter = 0
    for ingredient in ingredient_list:
        if is_ingredient_fresh(ingredient, range_list):
            counter += 1

    print(counter)

if __name__ == "__main__":
    main()
