#!/usr/bin/env python
from collections import OrderedDict


def parse(day_input: str) -> list[str]:
    return [line for line in day_input.split(",")]


def get_hash_result(string: str) -> int:
    current_value = 0
    for c in string:
        ascii_code = ord(c)
        current_value += ascii_code
        current_value *= 17
        current_value = current_value % 256

    return current_value


def main():
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    boxes = [OrderedDict() for _ in range(256)]

    for string in parsed_input:
        if "=" in string:
            operation = "="
            label, focal_length = string.split("=")
        else:
            operation = "-"
            label = string.replace("-", "")
            focal_length = None

        box_number = get_hash_result(label)
        box = boxes[box_number]

        if operation == "=":
            box[label] = focal_length
        elif operation == "-":
            box.pop(label, None)

    count = 0
    for box_i, box in enumerate(boxes):
        for slot_i, (label, focal_length) in enumerate(box.items()):
            count += (box_i + 1) * (slot_i + 1) * int(focal_length)

    print(count)


if __name__ == "__main__":
    main()
