#!/usr/bin/env python
import re


def parse(day_input: str) -> tuple[str, dict[str, list[str]]]:
    changes_str, molecule = day_input.split("\n\n")

    changes = {}
    for line in changes_str.split("\n"):
        original, new = line.strip().split(" => ")
        changes[original] = changes.get(original, []) + [new]

    return molecule, changes


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    molecule, changes = parse(day_input)

    distinct_new_molecule = set()
    for original, new_list in changes.items():
        for match in re.finditer(original, molecule):
            for new in new_list:
                new_molecule = molecule[:match.start()] + new + molecule[match.end():]
                distinct_new_molecule.add(new_molecule)

    print(len(distinct_new_molecule))


if __name__ == "__main__":
    main()
