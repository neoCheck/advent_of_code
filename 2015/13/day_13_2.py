#!/usr/bin/env python
from itertools import permutations


def parse(day_input: str) -> dict[tuple[str, str], int]:
    sittings = {}
    for line in day_input.split("\n"):
        line = (
            line.replace(".", "")
                .replace("would gain ", "")
                .replace("would lose ", "-")
                .replace("happiness units by sitting next to ", "")
        )
        person_a, happiness, person_b = line.split(" ")
        sittings[(person_a, person_b)] = sittings.get((person_a, person_b), 0) + int(happiness)
        sittings[(person_b, person_a)] = sittings[(person_a, person_b)]

    return sittings


def get_happiness(persons: list[str], sittings: dict[tuple[str, str], int]) -> int:
    happiness = 0
    for i in range(-1, len(persons) - 1):
        happiness += sittings[(persons[i], persons[i + 1])]

    return happiness


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    sittings = parse(day_input)
    persons = set([a for a, _ in sittings.keys()])

    for person in persons:
        sittings[("ME", person)] = 0
        sittings[(person, "ME")] = 0

    persons.add("ME")

    max_happiness = None
    for permutation in permutations(persons, len(persons)):
        happiness = get_happiness(list(permutation), sittings)
        if max_happiness is None or happiness > max_happiness:
            max_happiness = happiness

    print(max_happiness)


if __name__ == "__main__":
    main()
