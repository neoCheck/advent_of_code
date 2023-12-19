#!/usr/bin/env python
from dataclasses import dataclass


@dataclass
class Condition:
    category: str
    condition: str
    value: int
    return_workflow: str



@dataclass
class Workflow:
    name: str
    condition_list: list[Condition]
    default: str


def run_part(
        current_workflow: str,
        workflow_dict: dict[str, Workflow],
        part_range: dict[str, tuple[int, int]]
) -> list[tuple[str, dict[str, tuple[int, int]]]]:

    workflow_range = []

    workflow = workflow_dict[current_workflow]
    current_part_range = part_range
    for condition in workflow.condition_list:
        category_part_range = current_part_range.pop(condition.category)

        if condition.condition == ">":
            keep_part = {condition.category: (condition.value + 1, category_part_range[1])}
            keep_part.update(part_range)
            workflow_range.append((condition.return_workflow, keep_part))
            current_part_range[condition.category] = (category_part_range[0], condition.value)
        elif condition.condition == "<":
            keep_part = {condition.category: (category_part_range[0], condition.value - 1)}
            keep_part.update(part_range)
            workflow_range.append((condition.return_workflow, keep_part))
            current_part_range[condition.category] = (condition.value, category_part_range[1])

    workflow_range.append((workflow.default, current_part_range))
    return workflow_range


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

    workflow_dict, _ = parse(day_input)

    part_range = {
        "x": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "s": (1, 4000),
    }

    list_to_handle = [("in", part_range)]
    accepted_list = []
    rejected_list = []
    while list_to_handle:
        workflow_name, part_r = list_to_handle.pop(0)
        res = run_part(workflow_name, workflow_dict, part_r)

        to_handle = []
        for w_name, p_range in res:
            if w_name == "A":
                accepted_list.append(p_range)
            elif w_name == "R":
                rejected_list.append(p_range)
            else:
                to_handle.append((w_name, p_range))

        list_to_handle += to_handle

    res = 0
    for a in accepted_list:
        combination = 1
        for _, (min_r, max_r) in a.items():
            combination *= max_r - min_r + 1

        res += combination

    print(res)


if __name__ == "__main__":
    main()
