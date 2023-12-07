#!/usr/bin/env python
from collections import defaultdict
from enum import Enum


class RankKind(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_KIND = 5
    FIVE_OF_KIND = 6

    @classmethod
    def get_rank_kind(cls, card_kind: list[int]):
        if card_kind == [1, 1, 1, 1, 1]:
            return cls.HIGH_CARD
        elif card_kind == [1, 1, 1, 2]:
            return cls.ONE_PAIR
        elif card_kind == [1, 2, 2]:
            return cls.TWO_PAIRS
        elif card_kind == [1, 1, 3]:
            return cls.THREE_OF_KIND
        elif card_kind == [2, 3]:
            return cls.FULL_HOUSE
        elif card_kind == [1, 4]:
            return cls.FOUR_OF_KIND
        elif card_kind == [5]:
            return cls.FIVE_OF_KIND
        return cls.HIGH_CARD


class CamelCards:
    CARDS_STRENGTH = "J23456789TQKA"

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = int(bid)

    def get_kind(self) -> int:
        register = defaultdict(int)
        for c in self.cards:
            register[c] += 1

        if "J" in self.cards and len(list(register.keys())) > 1:
            joker_number = register.pop("J")
            power_choice = sorted([(v, self.CARDS_STRENGTH.index(k)) for k, v in register.items()])[-1]
            card_letter = self.CARDS_STRENGTH[power_choice[1]]
            register[card_letter] += joker_number

        card_kind = sorted(list(register.values()))
        rank_kind = RankKind.get_rank_kind(card_kind)
        return rank_kind.value

    def __lt__(self, other):
        self_kind = self.get_kind()
        other_kind = other.get_kind()

        if self_kind != other_kind:
            return self_kind < other_kind

        for i in range(5):
            self_card_index = self.CARDS_STRENGTH.index(self.cards[i])
            other_card_index = self.CARDS_STRENGTH.index(other.cards[i])

            if self_card_index != other_card_index:
                return self_card_index < other_card_index

        return True

    def __repr__(self):
        return f"CC : {self.cards} - {self.bid}"


def parse(day_input: str) -> list[CamelCards]:
    cc = []
    for line_day_input in day_input.split("\n"):
        cards, bid = line_day_input.split(" ")
        cc.append(CamelCards(cards, bid))
    return cc


def get_total_winnings(sorted_camel_cards: list[CamelCards]) -> int:
    total = 0

    for i, camel_card in enumerate(sorted_camel_cards):
        total += (i + 1) * camel_card.bid

    return total


if __name__ == "__main__":
    input_ = open("input").read().strip()
    camel_cards = parse(input_)
    s_camel_cards = sorted(camel_cards)
    total_winnings = get_total_winnings(s_camel_cards)

    print(total_winnings)
