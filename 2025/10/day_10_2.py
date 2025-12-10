#!/usr/bin/env python
from dataclasses import dataclass
# pip install z3-solver
import z3


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


def get_fewest_wiring_press_to_joltage_requirements(machine: Machine) -> int:
    z3_optimizer = z3.Optimize()

    z3_variables = [z3.Int(f"Wiring{i}") for i in range(len(machine.wiring_schematics))]

    z3_optimizer.minimize(sum(z3_variables))
    for variable in z3_variables:
        z3_optimizer.add(variable >= 0)

    for i, joltage in enumerate(machine.joltage_requirements):
        terms = [
            z3_variables[j]
            for j, wiring in enumerate(machine.wiring_schematics)
            if i in wiring
        ]
        z3_optimizer.add(sum(terms) == joltage)

    assert z3_optimizer.check()
    z3_model = z3_optimizer.model()

    sum_pressed = 0
    for variable in z3_variables:
        num_press = z3_model[variable].as_long()
        sum_pressed += num_press
        # print(f"{variable}: {num_press}")

    return sum_pressed

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    machine_list = parse(day_input)

    counter = 0
    for machine in machine_list:
        # print(machine)
        counter += get_fewest_wiring_press_to_joltage_requirements(machine)

    print(counter)


if __name__ == "__main__":
    main()
