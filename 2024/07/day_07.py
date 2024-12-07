#!/usr/bin/env python


def parse(day_input: str) -> list[tuple[int, list[int]]]:
    data_list: list[tuple[int, list[int]]] = []
    for line in day_input.split("\n"):
        expected_result, numbers = line.split(":")
        numbers_list = [int(n) for n in numbers.strip().split(" ")]

        data_list.append((int(expected_result), numbers_list))

    return data_list

def get_combinations(max_combination_len: int) -> dict[int, list[str]]:
    return {
        power: [f"{n:b}".zfill(power).replace("0", "+").replace("1", "*") for n in range(2**power)]
        for power in range(1, max_combination_len + 1)
    }

def is_a_combination_right(expected_result: int, numbers: list[int], combinations: list[str]) -> bool:
    for combination in combinations:
        res = numbers[0]
        for i, operator in enumerate(combination):
            if operator == "*":
                res = res * numbers[i + 1]
            elif operator == "+":
                res = res + numbers[i + 1]

        if expected_result == res:
            return True

    return False

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)
    max_combination_len = max([len(nums) for _, nums in parsed_input]) - 1
    combinations = get_combinations(max_combination_len)

    print(sum(
        [
            expected_result
            for expected_result, numbers in parsed_input
            if is_a_combination_right(expected_result, numbers, combinations[len(numbers) - 1])
        ]
    ))


if __name__ == "__main__":
    main()
