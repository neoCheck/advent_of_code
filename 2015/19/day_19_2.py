#!/usr/bin/env python

def parse(day_input: str) -> str:
    return day_input.split("\n\n")[1]


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    molecule = parse(day_input)

    number_of_elements = sum([int(elem.isupper()) for elem in molecule])

    print(number_of_elements - molecule.count("Ar") - molecule.count("Rn") - molecule.count("Y") * 2 - 1)


if __name__ == "__main__":
    main()
