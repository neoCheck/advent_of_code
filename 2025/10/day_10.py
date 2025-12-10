#!/usr/bin/env python
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Machine:
    buttons_requirement: list[bool]
    wiring_schematics: list[list[int]]
    joltage_requirements: list[int]



def parse(day_input: str) -> list[Machine]:
    machine_list: list[Machine] = []
    for line in day_input.split("\n"):
        info_list = line.split(" ")
        buttons_requirement = [bool(b == "#")  for b in info_list[0].split("[")[1].split("]")[0]]
        joltage_requirements = [int(j) for j in info_list[-1].split("{")[1].split("}")[0].split(",")]
        wiring_schematics = [
            [int(b) for b in ws.split("(")[1].split(")")[0].split(",")]
            for ws in info_list[1:-1]
        ]
        machine = Machine(
            buttons_requirement=buttons_requirement,
            wiring_schematics=wiring_schematics,
            joltage_requirements=joltage_requirements,
        )
        machine_list.append(machine)

    return machine_list


def get_fewest_total_presses(machine: Machine) -> int:
    for r in range(1, len(machine.wiring_schematics)):
        for wiring_list in combinations(machine.wiring_schematics, r):
            current_button = [False for _ in range(len(machine.buttons_requirement))]
            for wiring in wiring_list:
                for button_index in wiring:
                    current_button[button_index] = not current_button[button_index]

            if current_button == machine.buttons_requirement:
                return r

    raise ValueError("HUSTON WE HAVE A PROBLEM !")

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    machine_list = parse(day_input)

    counter = 0
    for i, machine in enumerate(machine_list):
        counter += get_fewest_total_presses(machine)

    print(counter)


if __name__ == "__main__":
    main()
