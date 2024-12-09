#!/usr/bin/env python

EMPTY_SPOT = -1

def get_available_space_index(disk: list[int], needed_length: int) -> int:
    counter = 0
    for i, spot in enumerate(disk):
        if spot == EMPTY_SPOT:
            counter += 1
        else:
            counter = 0

        if counter == needed_length:
            return i - (needed_length - 1)

    return -1


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    disk = []
    index = 0
    for i, num in enumerate(day_input):
        n = int(num)
        if i % 2 == 0:
            disk += [index for _ in range(n)]
            index += 1
        else:
            disk += [EMPTY_SPOT for _ in range(n)]

    while disk[-1] == EMPTY_SPOT:
        disk.pop()

    i = len(disk) - 1
    while i >= 0:
        j = i
        while j >= 0 and disk[j] != EMPTY_SPOT and disk[j] == disk[i]:
            j -= 1

        spots_to_move = disk[j + 1:i + 1]
        needed_length = len(spots_to_move)
        available_space = get_available_space_index(disk, needed_length)
        if available_space != -1 and available_space < j:
            for spots_i, disk_i in enumerate(range(available_space, available_space + needed_length)):
                disk[disk_i] = spots_to_move[spots_i]

            disk[j + 1:i + 1] = [EMPTY_SPOT for _ in range(needed_length)]

        i = j
        while disk[i] == EMPTY_SPOT:
            i -= 1

    checksum = 0
    for i, spot in enumerate(disk):
        if spot == EMPTY_SPOT:
            continue
        checksum += i * spot

    print(checksum)


if __name__ == "__main__":
    main()
