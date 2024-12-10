#!/usr/bin/env python


def parse(day_input: str) -> list[str]:
    return [line for line in day_input.split("\n")]


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    parsed_input = parse(day_input)

    score = 0
    for source_line in parsed_input:
        evaluated_line = eval(source_line)
        line_score = len(source_line) - len(evaluated_line)
        score += line_score

    print(score)


if __name__ == "__main__":
    main()
