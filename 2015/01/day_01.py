#!/usr/bin/env python

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    counter = 0
    for c in day_input:
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1

    print(counter)


if __name__ == "__main__":
    main()
