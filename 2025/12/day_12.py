#!/usr/bin/env python


class PresentShape:
    def __init__(self, index: int, shape: list[str]) -> None:
        self.index = index
        self.shape = shape
        self._size = sum([len([1 for c in l if c == "#"]) for l in self.shape])

    @property
    def size(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"PresentShape({self.index}: {self._size})"

class PresentGrid:
    def __init__(self, width: int, height: int, required_quantity: dict[PresentShape, int]) -> None:
        self._width = width
        self._height = height
        self._size = width * height
        self.required_quantity = required_quantity

    @property
    def size(self) -> int:
        return self._size

    def can_fit_required_quantity(self) -> bool:
        presents_size = sum([
            present.size * quantity
            for present, quantity in self.required_quantity.items()
        ])
        return presents_size < self._size

    def __repr__(self) -> str:
        return f"PresentGrid({self._width}x{self._height})"


def parse(day_input: str) -> list[PresentGrid]:
    split_input = day_input.split("\n\n")
    presents_str = split_input[:6]
    grid_str = split_input[6]

    presents = [
        PresentShape(i, present.split("\n")[1:])
        for i, present in enumerate(presents_str)
    ]

    grid_list: list[PresentGrid] = []

    for grid in grid_str.split("\n"):
        size_str, quantity_str = grid.split(": ")
        width_str, height_str = size_str.split("x")

        quantity_list = [int(n) for n in quantity_str.split()]
        required_quantity = {
            presents[i]: quantity
            for i, quantity in enumerate(quantity_list)
        }
        grid_list.append(PresentGrid(int(width_str), int(height_str), required_quantity))

    return grid_list


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    grid_list = parse(day_input)

    counter = 0
    for grid in grid_list:
        if grid.can_fit_required_quantity():
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
