#!/usr/bin/env python
import re
from dataclasses import dataclass


T_POINT = tuple[int, int]

@dataclass
class ClawMachine:
    a: T_POINT
    b: T_POINT
    prize: T_POINT

    def get_min_cost_to_prize(self) -> int:

        min_cost = 0

        max_a_range = min(self.prize[0] // self.a[0] , self.prize[1] // self.a[1], 100)

        for a_pushed in range(max_a_range + 1):
            x_gap_to_fill = self.prize[0] - (a_pushed * self.a[0])
            b_pushed = x_gap_to_fill // self.b[0]
            if b_pushed > 100:
                continue

            new_x = (a_pushed * self.a[0]) + (b_pushed * self.b[0])
            new_y = (a_pushed * self.a[1]) + (b_pushed * self.b[1])
            if (new_x, new_y) == self.prize:
                min_cost = min(min_cost or 1_000, (a_pushed * 3) + b_pushed)

        max_b_range = min(self.prize[0] // self.b[0] , self.prize[1] // self.b[1], 100)

        for b_pushed in range(max_b_range + 1):
            x_gap_to_fill = self.prize[0] - (b_pushed * self.b[0])
            a_pushed = x_gap_to_fill // self.a[0]
            if a_pushed > 100:
                continue

            new_x = (a_pushed * self.a[0]) + (b_pushed * self.b[0])
            new_y = (a_pushed * self.a[1]) + (b_pushed * self.b[1])
            if (new_x, new_y) == self.prize:
                min_cost = min(min_cost or 1_000, (a_pushed * 3) + b_pushed)

        return min_cost


def parse(day_input: str) -> list[ClawMachine]:
    claw_machines = []
    num_regex = re.compile(r"(\d+)")
    for claw_lines in day_input.split("\n\n"):
        a_x, a_y, b_x, b_y, prize_x, prize_y = num_regex.findall(claw_lines)
        claw_machines.append(
            ClawMachine(
                a=(int(a_x), int(a_y)),
                b=(int(b_x), int(b_y)),
                prize=(int(prize_x), int(prize_y)),
            )
        )

    return claw_machines


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    claw_machines = parse(day_input)

    print(sum([cm.get_min_cost_to_prize() for cm in claw_machines]))


if __name__ == "__main__":
    main()
