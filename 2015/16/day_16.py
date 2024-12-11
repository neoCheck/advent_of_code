#!/usr/bin/env python


MFCSAM_AUNT_SUE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse(day_input: str) -> dict[int, dict[str, int]]:
    all_sues = {}
    for line in day_input.split("\n"):
        sue_num, _, sue_data_str = line.partition(": ")
        sue_num = int(sue_num.replace("Sue ", ""))

        sue_dict = {}
        for sue_data in sue_data_str.split(", "):
            k, v = sue_data.split(": ")
            sue_dict[k] = int(v)

        all_sues[sue_num] = sue_dict


    return all_sues


def is_the_right_aunt_sue(sue_dict: dict[str, int]) -> bool:
    for k, v in sue_dict.items():
        if MFCSAM_AUNT_SUE[k] != v:
            return False

    return True

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    all_sues = parse(day_input)
    for sue_num, sue_dict in all_sues.items():
        if is_the_right_aunt_sue(sue_dict):
            print(sue_num)



if __name__ == "__main__":
    main()
