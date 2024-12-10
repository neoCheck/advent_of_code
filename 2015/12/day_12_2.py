#!/usr/bin/env python
from typing import Any
import json

def extract_numbers(data: Any) -> list[int]:
    numbers = []
    if isinstance(data, int):
        numbers.append(data)
    elif isinstance(data, dict) and "red" not in data.values():
        for d in data.values():
            numbers += extract_numbers(d)
    elif isinstance(data, list):
        for d in data:
            numbers += extract_numbers(d)
    return numbers


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    data = json.loads(day_input)

    numbers = extract_numbers(data)

    print(sum(numbers))


if __name__ == "__main__":
    main()
