#!/usr/bin/env python


def parse(day_input: str) -> list[tuple[int, list[int]]]:
    data_list: list[tuple[int, list[int]]] = []
    for line in day_input.split("\n"):
        expected_result, numbers = line.split(":")
        numbers_list = [int(n) for n in numbers.strip().split(" ")]

        data_list.append((int(expected_result), numbers_list))

    return data_list

def to_custom_base_012(nb: int) -> str:
    if nb == 0:
        return "0"

    digits = []
    base = 3
    while nb > 0:
        digits.append(str(nb % base))
        nb //= base

    return "".join(reversed(digits))


def get_combinations(max_combination_len: int) -> dict[int, list[str]]:
    return {
        power: [f"{n:b}".zfill(power).replace("0", "+").replace("1", "*") for n in range(2**power)]
        for power in range(1, max_combination_len + 1)
    }


def get_combinations_2(max_combination_len: int) -> dict[int, list[str]]:
    comb_2 = {
        power: [
            to_custom_base_012(n).zfill(power).replace("0", "+").replace("1", "*").replace("2", "|")
            for n in range(3**power)
        ]
        for power in range(1, max_combination_len + 1)
    }

    # Remove all combinations that do not have "|"
    return {k: [s for s in v if "|" in s] for k, v in comb_2.items()}


def is_a_combination_right(expected_result: int, numbers: list[int], combinations: list[str]) -> bool:
    for combination in combinations:
        res = numbers[0]
        for i, operator in enumerate(combination):
            if operator == "*":
                res = res * numbers[i + 1]
            elif operator == "+":
                res = res + numbers[i + 1]
            elif operator == "|":
                res = int(f"{res}{numbers[i + 1]}")

        if expected_result == res:
            return True

    return False


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)
    max_combination_len = max([len(nums) for _, nums in parsed_input]) - 1
    combinations = get_combinations(max_combination_len)

    remaining_to_calculate: list[tuple[int, list[int]]] = []
    right_calculation: list[tuple[int, list[int]]] = []

    for expected_result, numbers in parsed_input:
        if is_a_combination_right(expected_result, numbers, combinations[len(numbers) - 1]):
            right_calculation.append((expected_result, numbers))
        else:
            remaining_to_calculate.append((expected_result, numbers))

    print(sum(expected_result for expected_result, numbers in right_calculation))

    combinations_2 = get_combinations_2(max_combination_len)
    remaining_to_calculate = sorted(remaining_to_calculate, key=lambda x: len(x[1]))

    for i, (expected_result, numbers) in enumerate(remaining_to_calculate):
        print(f"{i}/{len(remaining_to_calculate)}")
        if is_a_combination_right(expected_result, numbers, combinations_2[len(numbers) - 1]):
            right_calculation.append((expected_result, numbers))

    print(sum(expected_result for expected_result, numbers in right_calculation))


if __name__ == "__main__":
    main()
