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
        b_pushed = (self.prize[0] * self.a[1] - self.a[0] * self.prize[1]) // (self.a[1] * self.b[0] - self.b[1] * self.a[0])
        a_pushed = (self.prize[0] - b_pushed * self.b[0]) // self.a[0]

        new_x = (a_pushed * self.a[0]) + (b_pushed * self.b[0])
        new_y = (a_pushed * self.a[1]) + (b_pushed * self.b[1])
        if (new_x, new_y) == self.prize:
            return (a_pushed * 3) + b_pushed

        return 0


def parse(day_input: str) -> list[ClawMachine]:
    claw_machines = []
    num_regex = re.compile(r"(\d+)")
    for claw_lines in day_input.split("\n\n"):
        a_x, a_y, b_x, b_y, prize_x, prize_y = num_regex.findall(claw_lines)
        claw_machines.append(
            ClawMachine(
                a=(int(a_x), int(a_y)),
                b=(int(b_x), int(b_y)),
                prize=(int(prize_x) + 10_000_000_000_000, int(prize_y) + 10_000_000_000_000),
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
