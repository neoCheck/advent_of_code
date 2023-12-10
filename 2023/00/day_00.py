#!/usr/bin/env python


def parse(day_input: str) -> list[str]:
    return [line for line in day_input.split("\n")]


if __name__ == "__main__":
    with open("input") as f:
        input_ = f.read().strip()

    print(input_)
