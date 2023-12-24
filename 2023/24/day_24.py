#!/usr/bin/env python
from dataclasses import dataclass
from itertools import combinations


AREA = (200_000_000_000_000, 400_000_000_000_000)
# AREA = (7, 27)


@dataclass
class HailStone:
    px: int
    py: int
    pz: int
    vx: int
    vy: int
    vz: int


def parse(day_input: str) -> list[HailStone]:
    hailstone_list = []
    for line in day_input.split("\n"):
        initial_pos_str, velocity_str = line.split(" @ ")
        px, py, pz = [int(s) for s in initial_pos_str.split(", ")]
        vx, vy, vz = [int(s) for s in velocity_str.split(", ")]

        hailstone_list.append(
            HailStone(px, py, pz, vx, vy, vz)
        )

    return hailstone_list


def find_intersection(hs1: HailStone, hs2: HailStone) -> bool:

    den = hs1.vx * hs2.vy - hs1.vy * hs2.vx

    # Check if paths are parallel
    if den == 0:
        return False

    px = ((hs1.px * (hs1.py + hs1.vy) - hs1.py * (hs1.px + hs1.vx)) *
          (hs2.px - (hs2.px + hs2.vx)) - (hs1.px-(hs1.px + hs1.vx)) *
          (hs2.px*(hs2.py + hs2.vy)-hs2.py*(hs2.px + hs2.vx))) / den
    py = ((hs1.px * (hs1.py + hs1.vy) - hs1.py * (hs1.px + hs1.vx)) *
          (hs2.py - (hs2.py + hs2.vy)) - (hs1.py - (hs1.py + hs1.vy)) *
          (hs2.px * (hs2.py + hs2.vy) - hs2.py * (hs2.px + hs2.vx))) / den

    is_valid_hs1 = (px > hs1.px) == ((hs1.px + hs1.vx) > hs1.px)
    is_valid_hs2 = (px > hs2.px) == ((hs2.px + hs2.vx) > hs2.px)

    # Check if intersection point is within the test area
    if AREA[0] <= px <= AREA[1] and AREA[0] <= py <= AREA[1] and is_valid_hs1 and is_valid_hs2:
        return True

    return False


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    hailstone_list = parse(day_input)
    hailstone_combinations = list(combinations(hailstone_list, r=2))

    intersection_count = sum(find_intersection(hs1, hs2) for hs1, hs2 in hailstone_combinations)

    print(intersection_count)  # 17867


if __name__ == "__main__":
    main()
