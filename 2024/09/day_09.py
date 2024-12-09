#!/usr/bin/env python


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    empty_spot = -1

    disk = []
    index = 0
    for i, num in enumerate(day_input):
        n = int(num)
        if i % 2 == 0:
            disk += [index for _ in range(n)]
            index += 1
        else:
            disk += [empty_spot for _ in range(n)]

    while disk[-1] == empty_spot:
        disk.pop()

    i = 0
    first_available_spot = 0
    while i < len(disk):
        try:
            first_available_spot = disk.index(empty_spot, first_available_spot)
        except ValueError:
            break
        disk[first_available_spot] = disk.pop()


    checksum = sum(i * spot for i, spot in enumerate(disk))
    print(checksum)


if __name__ == "__main__":
    main()
