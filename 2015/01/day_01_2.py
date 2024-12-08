#!/usr/bin/env python

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    counter = 0
    for i, c in enumerate(day_input):
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1

        if counter == -1:
            print(i + 1)
            return


if __name__ == "__main__":
    main()
