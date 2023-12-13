#!/usr/bin/env python

class Pattern:
    def __init__(self, map_: list[str]) -> None:
        self.map = map_

    def get_left_mirror_size(self, i: int):
        upper_part = self.map[:i]
        upper_part = upper_part[::-1]
        lower_part = self.map[i:]

        size = 0
        for pos in range(min(len(upper_part), len(lower_part))):
            if upper_part[pos] == lower_part[pos]:
                size += 1
            else:
                return 0

        return size

    def get_left_mirror(self) -> int:
        biggest_size = 0
        position = 0
        for i in range(len(self.map)):
            current_size = self.get_left_mirror_size(i)
            if current_size > biggest_size:
                biggest_size = current_size
                position = i

        return position

    def rotate_map(self):
        self.map = [
            "".join([line[j] for line in self.map])
            for j in range(len(self.map[0]))
        ]

    def summarize(self) -> int:
        left_position = self.get_left_mirror()

        self.rotate_map()
        right_position = self.get_left_mirror()

        return (left_position * 100) + right_position


def parse(day_input: str) -> list[Pattern]:
    return [Pattern(line.split("\n")) for line in day_input.split("\n\n")]


def main():
    with open("input") as f:
        day_input = f.read().strip()

    pattern_list = parse(day_input)
    result = sum([p.summarize() for p in pattern_list])
    print(result)  # 36448


if __name__ == "__main__":
    main()
