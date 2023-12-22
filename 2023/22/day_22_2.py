#!/usr/bin/env python


def parse(day_input: str) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    values = []
    for line in day_input.split("\n"):
        pos_start_str, pos_end_str = line.split("~")
        pos_start = [int(p) for p in pos_start_str.split(",")]
        pos_start = (pos_start[0], pos_start[1], pos_start[2])
        pos_end = [int(p) for p in pos_end_str.split(",")]
        pos_end = (pos_end[0], pos_end[1], pos_end[2])
        values.append((pos_start, pos_end))

    return sorted(values, key=lambda p: p[0][2])  # pos_start z-axis


def can_go_down(
        bricks: list[tuple[tuple[int, int, int], tuple[int, int, int]]],
        pos_start: tuple[int, int, int],
        pos_end: tuple[int, int, int],
        z_under: int
) -> bool:
    bricks_under = [
        (p_start, p_end)
        for p_start, p_end in bricks
        if (p_end[2] == z_under and
            set(range(p_start[0], p_end[0] + 1)).intersection(set(range(pos_start[0], pos_end[0] + 1))) and
            set(range(p_start[1], p_end[1] + 1)).intersection(set(range(pos_start[1], pos_end[1] + 1)))
            )
    ]
    return False if bricks_under else True


def make_them_fall(
        bricks: list[tuple[tuple[int, int, int], tuple[int, int, int]]]
) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:

    for i in range(len(bricks)):
        pos_start, pos_end = bricks[i]

        z_start = pos_start[2]
        z_under = z_start - 1
        while z_under > 0:
            if can_go_down(bricks, pos_start, pos_end, z_under):
                z_under -= 1
            else:
                break
        z_delta = z_start - (z_under + 1)

        new_pos_start = (pos_start[0], pos_start[1], pos_start[2] - z_delta)
        new_pos_end = (pos_end[0], pos_end[1], pos_end[2] - z_delta)

        bricks[i] = (new_pos_start, new_pos_end)

    return bricks


def get_bricks_under(
        bricks_under_cache: dict[tuple[tuple[int, int, int], tuple[int, int, int]], list[tuple[tuple[int, int, int], tuple[int, int, int]]]],
        bricks: list[tuple[tuple[int, int, int], tuple[int, int, int]]],
        pos_start: tuple[int, int, int],
        pos_end: tuple[int, int, int]
) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    bricks_under = [
        (p_start, p_end)
        for p_start, p_end in bricks
        if (p_end[2] == pos_start[2] - 1 and
            set(range(p_start[0], p_end[0] + 1)).intersection(set(range(pos_start[0], pos_end[0] + 1))) and
            set(range(p_start[1], p_end[1] + 1)).intersection(set(range(pos_start[1], pos_end[1] + 1)))
            )
    ]

    key = (pos_start, pos_end)
    bricks_under_cache[key] = bricks_under

    return bricks_under


def get_cannot_be_disintegrated_safely(
        bricks_up_cache: dict[tuple[tuple[int, int, int], tuple[int, int, int]], list[tuple[tuple[int, int, int], tuple[int, int, int]]]],
        bricks_under_cache: dict[tuple[tuple[int, int, int], tuple[int, int, int]], list[tuple[tuple[int, int, int], tuple[int, int, int]]]],
        bricks: list[tuple[tuple[int, int, int], tuple[int, int, int]]]
) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    not_safe_bricks = []

    for pos_start, pos_end in bricks:

        key = (pos_start, pos_end)
        bricks_up = [
            (p_start, p_end)
            for p_start, p_end in bricks
            if (p_start[2] == pos_end[2] + 1 and
                set(range(p_start[0], p_end[0] + 1)).intersection(set(range(pos_start[0], pos_end[0] + 1))) and
                set(range(p_start[1], p_end[1] + 1)).intersection(set(range(pos_start[1], pos_end[1] + 1)))
                )
        ]
        bricks_up_cache[key] = bricks_up

        if not all([bool(len(get_bricks_under(bricks_under_cache, bricks, p_start, p_end)) >= 2) for p_start, p_end in bricks_up]):
            not_safe_bricks.append((pos_start, pos_end))

    return not_safe_bricks


def get_chain_reaction(
        pos: tuple[tuple[int, int, int], tuple[int, int, int]],
        bricks_up_cache: dict[tuple[tuple[int, int, int], tuple[int, int, int]], list[tuple[tuple[int, int, int], tuple[int, int, int]]]],
        bricks_under_cache: dict[tuple[tuple[int, int, int], tuple[int, int, int]], list[tuple[tuple[int, int, int], tuple[int, int, int]]]],
) -> int:
    bricks_up_to_check = [b for b in bricks_up_cache[pos]]

    bricks_up_set = {pos}
    while bricks_up_to_check:
        p = bricks_up_to_check.pop(0)

        bricks_under = bricks_under_cache.get(p) or []
        if len(set(bricks_under) - bricks_up_set) == 0:
            bricks_up_set.add(p)
            bricks_up = bricks_up_cache.get(p) or []
            bricks_up_to_check += [b for b in bricks_up if b not in bricks_up_to_check]

    return len(bricks_up_set - {pos})


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    bricks = parse(day_input)
    new_bricks = make_them_fall(bricks)

    bricks_up_cache = {}
    bricks_under_cache = {}
    not_safe_bricks = get_cannot_be_disintegrated_safely(bricks_up_cache, bricks_under_cache, new_bricks)

    count = 0
    for i, not_safe_pos in enumerate(not_safe_bricks):
        c = get_chain_reaction(not_safe_pos, bricks_up_cache, bricks_under_cache)
        count += c

    print(count)  # 58440


if __name__ == "__main__":
    main()
