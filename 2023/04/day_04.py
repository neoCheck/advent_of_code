#!/usr/bin/env python


def get_card_score(card: str) -> int:
    card_id, numbers = card.split(":")

    winning_numbers, numbers_to_check = numbers.split("|")
    winning_numbers = [int(n) for n in winning_numbers.split(" ") if n.isdigit()]
    numbers_to_check = [int(n) for n in numbers_to_check.split(" ") if n.isdigit()]

    numbers_matched = [n for n in winning_numbers if n in numbers_to_check]

    if not numbers_matched:
        return 0
    return pow(2, len(numbers_matched)-1)


if __name__ == "__main__":
    input_ = open("input").read().strip()
    score_list = [get_card_score(c) for c in input_.split("\n")]
    print(sum(score_list))
