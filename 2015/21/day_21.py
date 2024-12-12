#!/usr/bin/env python
from dataclasses import dataclass
import itertools


@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int

    def __repr__(self) -> str:
        return f"{self.name}"

@dataclass
class Character:
    name: str
    hit_points: int
    damage: int
    armor: int

    def __repr__(self) -> str:
        return f"{self.name}"

EMPTY_ITEM = Item(name="EMPTY", cost=0, damage=0, armor=0)

WEAPONS_LIST = [
    Item(name="Dagger", cost=8, damage=4, armor=0),
    Item(name="Shortsword", cost=10, damage=5, armor=0),
    Item(name="Warhammer", cost=25, damage=6, armor=0),
    Item(name="Longsword", cost=40, damage=7, armor=0),
    Item(name="Greataxe", cost=74, damage=8, armor=0),
]

ARMORS_LIST = [
    EMPTY_ITEM,
    Item(name="Leather", cost=13, damage=0, armor=1),
    Item(name="Chainmail", cost=31, damage=0, armor=2),
    Item(name="Splintmail", cost=53, damage=0, armor=3),
    Item(name="Bandedmail", cost=75, damage=0, armor=4),
    Item(name="Platemail", cost=102, damage=0, armor=5),
]

DAMAGE_RINGS_LIST = [
    EMPTY_ITEM,
    Item(name="Damage +1", cost=25, damage=1, armor=0),
    Item(name="Damage +2", cost=50, damage=2, armor=0),
    Item(name="Damage +3", cost=100, damage=3, armor=0),
]

DEFENSE_RINGS_LIST = [
    EMPTY_ITEM,
    Item(name="Defense +1", cost=20, damage=0, armor=1),
    Item(name="Defense +2", cost=40, damage=0, armor=2),
    Item(name="Defense +3", cost=80, damage=0, armor=3),
]


def main() -> None:

    min_cost = 100_000

    for selected_items in itertools.product(WEAPONS_LIST, ARMORS_LIST, DEFENSE_RINGS_LIST, DAMAGE_RINGS_LIST):

        my_damage = sum([item.damage for item in selected_items])
        my_armor = sum([item.armor for item in selected_items])
        cost = sum([item.cost for item in selected_items])
        me = Character(name="ME", hit_points=100, damage=my_damage, armor=my_armor)
        boss = Character(name="BOSS", hit_points=109, damage=8, armor=2)

        my_current_damage = max(0, me.damage - boss.armor)
        boss_current_damage = max(0, boss.damage - me.armor)
        while me.hit_points > 0 and boss.hit_points > 0:
            boss.hit_points -= my_current_damage
            if boss.hit_points < 0:
                break

            me.hit_points -= boss_current_damage

        if me.hit_points > 0:
            min_cost = min(min_cost, cost)

    print(min_cost)


if __name__ == "__main__":
    main()
