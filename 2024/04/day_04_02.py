#!/usr/bin/env python


def parse(day_input: str) -> list[str]:
    return [line for line in day_input.split("\n")]


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    map_ = parse(day_input)

    len_grid_i = len(map_)
    len_grid_j = len(map_[0])

    xmas_counter = 0

    for i in range(len_grid_i):
        for j in range(len_grid_j):
            if map_[i][j] == "A" and i - 1 >= 0 and j - 1 >= 0 and i + 1 < len_grid_i and j + 1 < len_grid_j:
                if (
                        (
                                (map_[i - 1][j - 1] == "M" and map_[i + 1][j + 1] == "S") or
                                (map_[i - 1][j - 1] == "S" and map_[i + 1][j + 1] == "M")
                        )
                        and
                        (
                                (map_[i - 1][j + 1] == "M" and map_[i + 1][j - 1] == "S") or
                                (map_[i - 1][j + 1] == "S" and map_[i + 1][j - 1] == "M")
                        )
                ):
                    xmas_counter += 1


    print(xmas_counter)


if __name__ == "__main__":
    main()
