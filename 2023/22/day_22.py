#!/usr/bin/env python


def parse(day_input: str) -> list[tuple[list[int], list[int]]]:
    values = []
    for line in day_input.split("\n"):
        pos_start_str, pos_end_str = line.split("~")
        pos_start = [int(p) for p in pos_start_str.split(",")]
        pos_end = [int(p) for p in pos_end_str.split(",")]
        values.append((pos_start, pos_end))

    return sorted(values, key=lambda p: p[0][2])  # pos_start z-axis


def can_go_down(bricks: list[tuple[list[int], list[int]]], pos_start: list[int], pos_end: list[int], z_under: int) -> bool:
    bricks_under = [
        (p_start, p_end)
        for p_start, p_end in bricks
        if (p_end[2] == z_under and
            set(range(p_start[0], p_end[0] + 1)).intersection(set(range(pos_start[0], pos_end[0] + 1))) and
            set(range(p_start[1], p_end[1] + 1)).intersection(set(range(pos_start[1], pos_end[1] + 1)))
            )
    ]
    return False if bricks_under else True


def make_them_fall(bricks: list[tuple[list[int], list[int]]]) -> list[tuple[list[int], list[int]]]:

    for pos_start, pos_end in bricks:
        z_start = pos_start[2]
        z_under = z_start - 1
        while z_under > 0:
            if can_go_down(bricks, pos_start, pos_end, z_under):
                z_under -= 1
            else:
                break
        z_delta = z_start - (z_under + 1)
        pos_start[2] -= z_delta
        pos_end[2] -= z_delta

    return bricks


def get_bricks_under(bricks: list[tuple[list[int], list[int]]], pos_start: list[int], pos_end: list[int]) -> list[tuple[list[int], list[int]]]:
    return [
        (p_start, p_end)
        for p_start, p_end in bricks
        if (p_end[2] == pos_start[2] - 1 and
            set(range(p_start[0], p_end[0] + 1)).intersection(set(range(pos_start[0], pos_end[0] + 1))) and
            set(range(p_start[1], p_end[1] + 1)).intersection(set(range(pos_start[1], pos_end[1] + 1)))
            )
    ]


def count_can_be_disintegrated_safely(bricks: list[tuple[list[int], list[int]]]) -> int:
    count = 0

    for pos_start, pos_end in bricks:
        bricks_up = [
            (p_start, p_end)
            for p_start, p_end in bricks
            if (p_start[2] == pos_end[2] + 1 and
                set(range(p_start[0], p_end[0] + 1)).intersection(set(range(pos_start[0], pos_end[0] + 1))) and
                set(range(p_start[1], p_end[1] + 1)).intersection(set(range(pos_start[1], pos_end[1] + 1)))
                )
        ]

        if all([bool(len(get_bricks_under(bricks, p_start, p_end)) >= 2) for p_start, p_end in bricks_up]):
            count += 1

    return count


def main() -> None:
    with open("test_input") as f:
        day_input = f.read().strip()

    bricks = parse(day_input)
    new_bricks = make_them_fall(bricks)
    print(count_can_be_disintegrated_safely(new_bricks))


if __name__ == "__main__":
    main()
