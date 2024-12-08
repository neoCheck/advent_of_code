#!/usr/bin/env python


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    location_set: set[tuple[int, int]] = set()
    i, j = 0, 0
    location_set.add((i, j))

    for c in day_input:
        if c == ">":
            j += 1
        elif c == "<":
            j -= 1
        elif c == "v":
            i += 1
        elif c == "^":
            i -= 1
        location_set.add((i, j))

    print(len(location_set))


if __name__ == "__main__":
    main()
