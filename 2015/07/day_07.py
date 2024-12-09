#!/usr/bin/env python
import numpy as np


class CalculatedVariable:
    name: str
    statement: str
    required_variables: list[str]
    value: np.uint16 | None = None
    operator: str | None = None

    def __init__(self, name: str, statement: str) -> None:
        self.name = name
        self.statement = statement
        self.required_variables = []

        if self.statement.isdigit():
            self.value = np.uint16(self.statement)
        else:
            if " AND " in self.statement:
                a_name, b_name = self.statement.split(" AND ")
                if not a_name.isdigit():
                    self.required_variables.append(a_name)
                if not b_name.isdigit():
                    self.required_variables.append(b_name)
            elif " OR " in self.statement:
                a_name, b_name = self.statement.split(" OR ")
                if not a_name.isdigit():
                    self.required_variables.append(a_name)
                if not b_name.isdigit():
                    self.required_variables.append(b_name)
            elif self.statement.startswith("NOT "):
                a_name = self.statement[4:]
                if not a_name.isdigit():
                    self.required_variables.append(a_name)
            elif " LSHIFT " in self.statement:
                self.required_variables += [self.statement.split(" LSHIFT ")[0]]
            elif " RSHIFT " in self.statement:
                self.required_variables += [self.statement.split(" RSHIFT ")[0]]
            else:
                self.required_variables.append(self.statement)

    def __repr__(self) -> str:
        if self.value:
            return f"CalculatedVariable('{self.name}') : {self.statement} = {self.value}"
        else:
            return f"CalculatedVariable('{self.name}') : {self.statement}"

    def calculate(self, variables: dict[str, "CalculatedVariable"]) -> np.uint16 | None:
        if self.value is not None:
            return self.value

        if all([variables[v].value is not None for v in self.required_variables]):
            if " AND " in self.statement:
                a_name, b_name = self.statement.split(" AND ")
                a_value = np.uint16(a_name) if a_name.isdigit() else variables[a_name].value
                b_value = np.uint16(b_name) if b_name.isdigit() else variables[b_name].value
                self.value = a_value & b_value
            elif " OR " in self.statement:
                a_name, b_name = self.statement.split(" OR ")
                a_value = np.uint16(a_name) if a_name.isdigit() else variables[a_name].value
                b_value = np.uint16(b_name) if b_name.isdigit() else variables[b_name].value
                self.value = a_value | b_value
            elif self.statement.startswith("NOT "):
                a_name = self.statement[4:]
                a_value = variables[a_name].value
                self.value = ~a_value
            elif " LSHIFT " in self.statement:
                a_name, shift_value_str = self.statement.split(" LSHIFT ")
                a_value = np.uint16(a_name) if a_name.isdigit() else variables[a_name].value
                self.value = a_value << int(shift_value_str)
            elif " RSHIFT " in self.statement:
                a_name, shift_value_str = self.statement.split(" RSHIFT ")
                a_value = np.uint16(a_name) if a_name.isdigit() else variables[a_name].value
                self.value = a_value >> int(shift_value_str)
            else:
                self.value = variables[self.statement].value

        return None


def parse(day_input: str) -> dict[str, CalculatedVariable]:
    res: dict[str, CalculatedVariable] = {}
    for line in day_input.split("\n"):
        statement, variable_name = line.split(" -> ")
        res[variable_name] = CalculatedVariable(variable_name, statement)

    return res


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    while any(v.value is None for k,v in parsed_input.items()):
        for variable_name, variable in parsed_input.items():
            variable.calculate(parsed_input)

    print(parsed_input["a"])


if __name__ == "__main__":
    main()
