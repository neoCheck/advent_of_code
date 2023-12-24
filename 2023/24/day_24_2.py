#!/usr/bin/env python
from dataclasses import dataclass
from z3 import Solver, Int


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


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    hailstone_list = parse(day_input)
    x, y, z = Int('x'), Int('y'), Int('z')
    vx, vy, vz = Int('vx'), Int('vy'), Int('vz')
    solver = Solver()
    for i, hs in enumerate(hailstone_list):
        t = Int(f"T{i}")

        solver.add(x + t*vx - hs.px - t*hs.vx == 0)
        solver.add(y + t*vy - hs.py - t*hs.vy == 0)
        solver.add(z + t*vz - hs.pz - t*hs.vz == 0)

    solver.check()
    model = solver.model()
    print(model.eval(x + y + z))  # 557743507346379


if __name__ == "__main__":
    main()
