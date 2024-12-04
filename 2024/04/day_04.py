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
            if map_[i][j] == "X":
                # UP
                if i - 3 >= 0 and map_[i - 1][j] == "M" and map_[i - 2][j] == "A" and map_[i - 3][j] == "S":
                    xmas_counter += 1
                # DOWN
                if i + 3 < len_grid_i and map_[i + 1][j] == "M" and map_[i + 2][j] == "A" and map_[i + 3][j] == "S":
                    xmas_counter += 1
                # LEFT
                if j - 3 >= 0 and map_[i][j - 1] == "M" and map_[i][j - 2] == "A" and map_[i][j - 3] == "S":
                    xmas_counter += 1
                # RIGHT
                if j + 3 < len_grid_j and map_[i][j + 1] == "M" and map_[i][j + 2] == "A" and map_[i][j + 3] == "S":
                    xmas_counter += 1

                # UP LEFT
                if i - 3 >= 0 and j - 3 >= 0 and map_[i - 1][j - 1] == "M" and map_[i - 2][j - 2] == "A" and map_[i - 3][j - 3] == "S":
                    xmas_counter += 1
                # UP RIGHT
                if i - 3 >= 0 and j + 3 < len_grid_j and map_[i - 1][j + 1] == "M" and map_[i - 2][j + 2] == "A" and map_[i - 3][j + 3] == "S":
                    xmas_counter += 1
                # DOWN RIGHT
                if i + 3 < len_grid_i and j + 3 < len_grid_j and map_[i + 1][j + 1] == "M" and map_[i + 2][j + 2] == "A" and map_[i + 3][j + 3] == "S":
                    xmas_counter += 1
                # DOWN LEFT
                if i + 3 < len_grid_i and j - 3 >= 0 and map_[i + 1][j - 1] == "M" and map_[i + 2][j - 2] == "A" and map_[i + 3][j - 3] == "S":
                    xmas_counter += 1


    print(xmas_counter)


if __name__ == "__main__":
    main()
