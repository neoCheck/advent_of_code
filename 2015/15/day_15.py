#!/usr/bin/env python
from collections import Counter
from dataclasses import dataclass
from itertools import combinations_with_replacement


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __hash__(self) -> int:
        return hash(self.name)


def parse(day_input: str) -> list[Ingredient]:
    ingredients = []

    for line in day_input.split("\n"):
        name, info = line.split(": ")
        capacity_str, durability_str, flavor_str, texture_str, calories_str = info.split(", ")

        ingredients.append(
            Ingredient(
                name=name,
                capacity=int(capacity_str.split(" ")[1]),
                durability=int(durability_str.split(" ")[1]),
                flavor=int(flavor_str.split(" ")[1]),
                texture=int(texture_str.split(" ")[1]),
                calories=int(calories_str.split(" ")[1]),
            )
        )

    return ingredients


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    ingredients = parse(day_input)

    max_score = 0
    for combination in combinations_with_replacement(ingredients, 100):
        capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0

        for ingredient, occurrence in Counter(combination).items():
            capacity += occurrence * ingredient.capacity
            durability += occurrence * ingredient.durability
            flavor += occurrence * ingredient.flavor
            texture += occurrence * ingredient.texture

        capacity = capacity if capacity > 0 else 0
        durability = durability if durability > 0 else 0
        flavor = flavor if flavor > 0 else 0
        texture = texture if texture > 0 else 0

        score = capacity * durability * flavor * texture
        if score > max_score:
            max_score = score

    print(max_score)



if __name__ == "__main__":
    main()
