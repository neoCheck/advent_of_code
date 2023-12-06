#!/usr/bin/env python


def get_card_match(card: str) -> tuple[int, int]:
    card_id, numbers = card.split(":")

    card_id = int(card_id.replace("Card", "").replace(" ", ""))

    winning_numbers, numbers_to_check = numbers.split("|")
    winning_numbers = [int(n) for n in winning_numbers.split(" ") if n.isdigit()]
    numbers_to_check = [int(n) for n in numbers_to_check.split(" ") if n.isdigit()]

    numbers_matched = [n for n in winning_numbers if n in numbers_to_check]

    return card_id, len(numbers_matched)


def duplicate_cards(card_list: list[tuple[int, int]]) -> dict[int, int]:
    card_map = {card_id: len_numbers_matched for card_id, len_numbers_matched in card_list}
    card_found = {card_id: 1 for card_id, _ in card_list}

    for card_id, len_numbers_matched in card_map.items():

        for i in range(card_id + 1, card_id + 1 + len_numbers_matched):
            if i in card_found:
                card_found[i] += card_found[card_id]

    return card_found


if __name__ == "__main__":
    input_ = open("input").read().strip()
    card_match = [get_card_match(c) for c in input_.split("\n")]
    duplicated_cards = duplicate_cards(card_match)

    print(sum(duplicated_cards.values()))
    