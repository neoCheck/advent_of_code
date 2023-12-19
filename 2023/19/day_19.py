#!/usr/bin/env python
from dataclasses import dataclass


@dataclass
class Condition:
    category: str
    condition: str
    value: int
    return_workflow: str

    def is_met(self, part: dict[str, int]) -> bool:
        category_value = part[self.category]

        if self.condition == "<" and category_value < self.value:
            return True
        elif self.condition == ">" and category_value > self.value:
            return True

        return False


@dataclass
class Workflow:
    name: str
    condition_list: list[Condition]
    default: str

    def execute_conditions(self, part: dict[str, int]) -> str:
        for condition in self.condition_list:
            if condition.is_met(part):
                return condition.return_workflow

        return self.default


def run_part(workflow_dict: dict[str, Workflow], part: dict[str, int]) -> str:

    current_workflow = "in"

    while current_workflow:
        workflow = workflow_dict[current_workflow]

        current_workflow = workflow.execute_conditions(part)
        if current_workflow in ["A", "R"]:
            return current_workflow

    raise ValueError("Should not do this if data is correct")


def parse(day_input: str) -> tuple[dict[str, Workflow], list[dict[str, int]]]:
    workflow_str, parts_str = day_input.split("\n\n")

    parts_list = []
    for p in parts_str.replace("{", "").replace("}", "").split("\n"):
        part = {}
        for v in p.split(","):
            category, value = v.split("=")
            part[category] = int(value)

        parts_list.append(part)

    workflow_dict = {}

    for w in workflow_str.split("\n"):
        workflow_name, conditions_str = w.split("{")
        conditions_str = conditions_str.replace("}", "")

        conditions = conditions_str.split(",")
        workflow_default = conditions[-1]
        conditions = conditions[:-1]
        condition_list = []

        for c in conditions:
            cc, return_workflow = c.split(":")

            splitter = "<" if "<" in cc else ">"
            category, value = cc.split(splitter)

            condition_list.append(
                Condition(
                    category=category,
                    condition=splitter,
                    value=int(value),
                    return_workflow=return_workflow,
                )
            )

        workflow_dict[workflow_name] = Workflow(
            name=workflow_name,
            condition_list=condition_list,
            default=workflow_default,
        )

    return workflow_dict, parts_list


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    workflow_dict, parts_list = parse(day_input)

    result = 0
    for part in parts_list:
        return_workflow = run_part(workflow_dict, part)

        if return_workflow == "A":
            result += sum(list(part.values()))

    print(result)


if __name__ == "__main__":
    main()
