#!/usr/bin/env python


def main() -> None:
    with open("input") as f:
        number = f.read().strip()

    for i in range(40):
        new_number = ""
        j = 1
        prev_n = ""
        for c in number:
            if c == prev_n:
                j += 1
            else:
                if prev_n:
                    new_number += f"{j}{prev_n}"
                prev_n = c
                j = 1

        new_number += f"{j}{prev_n}"
        number = new_number

    print(len(number))


if __name__ == "__main__":
    main()
