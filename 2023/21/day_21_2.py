#!/usr/bin/env python


def run_steps(garden_map: list[list[str]], start_point: tuple[int, int], steps_list: list[int]) -> list[int]:
    plots = [start_point]

    plots_len = []
    v_dict = {start_point: 0}

    for step in range(1, max(steps_list) + 1):
        new_plots = []

        while plots:
            current_position = plots.pop(0)

            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_position = current_position[0] + direction[0], current_position[1] + direction[1]
                garden_position = new_position[0] % len(garden_map), new_position[1] % len(garden_map[0])

                if garden_map[garden_position[0]][garden_position[1]] != "#" and new_position not in v_dict:
                    v_dict[new_position] = step
                    new_plots.append(new_position)

        plots = new_plots
        if step in steps_list:
            plots_len.append(len([x for x in v_dict.values() if x % 2 == step % 2]))

    return plots_len


def get_start_point(garden_map: list[list[str]]) -> tuple[int, int]:
    for i, line in enumerate(garden_map):
        for j, c in enumerate(line):
            if c == "S":
                garden_map[i][j] = "."
                return i, j

    raise ValueError("Start Not Found")


def parse(day_input: str) -> list[list[str]]:
    return [
        [c for c in line]
        for line in day_input.split("\n")
    ]


def f_poly(n: int, a: int, b: int, c: int) -> int:
    return a*n**2 + b*n + c


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    garden_map = parse(day_input)

    start_point = get_start_point(garden_map)

    side = len(garden_map)  # 131
    half = start_point[1]  # 65
    steps_list = [
        half,
        half + side,
        half + (2 * side),
    ]

    # System of equations:
    # f(0) = a*0**2 + b*0 + c = f0, so c = f0
    # f(1) = a*1**2 + b*1 + c = f1, so  a +  b = f1 - f0
    # f(2) = a*2**2 + b*2 + c = f2, so 4a + 2b = f2 - f0
    # Gauss elimination gives:         2a      = f2 - f0 - 2*(f1 - f0) = f2 - 2f1 + f0
    # This gives:                            b = f1 - f0 - a
    f0, f1, f2 = run_steps(garden_map, start_point, steps_list)

    c = f0
    a = (f2 - 2 * f1 + f0) // 2
    b = f1 - f0 - a
    # Quadratic polynomial!
    n = (26501365 - half) // side
    print(f_poly(n, a, b, c))  # 599763113936220


if __name__ == "__main__":
    main()
