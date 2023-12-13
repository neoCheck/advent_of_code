#!/usr/bin/env python


def parse(day_input: str) -> list[str]:
    return [line for line in day_input.split("\n")]


def main():
    with open("input") as f:
        day_input = f.read().strip()

    print(day_input)


if __name__ == "__main__":
    main()
