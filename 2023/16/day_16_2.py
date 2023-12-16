#!/usr/bin/env python
from enum import Enum


class BeamDirection(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Beam:

    def __init__(
            self,
            contraption_layout: list[list[str]],
            start_i: int,
            start_j: int,
            direction: BeamDirection,
            beam_cache: list[tuple[int, int, BeamDirection]]
    ) -> None:
        self.contraption_layout = contraption_layout
        self.i = start_i
        self.j = start_j
        self.direction = direction
        self.beam_cache = beam_cache

    def get_next_position(self) -> tuple[int, int]:
        if self.direction == BeamDirection.RIGHT:
            return self.i, self.j + 1
        elif self.direction == BeamDirection.LEFT:
            return self.i, self.j - 1
        elif self.direction == BeamDirection.UP:
            return self.i - 1, self.j
        elif self.direction == BeamDirection.DOWN:
            return self.i + 1, self.j

        raise ValueError("Bad Value")

    def get_new_direction(self):
        case = self.contraption_layout[self.i][self.j]
        if case == "/":
            if self.direction == BeamDirection.RIGHT:
                self.direction = BeamDirection.UP
            elif self.direction == BeamDirection.LEFT:
                self.direction = BeamDirection.DOWN
            elif self.direction == BeamDirection.UP:
                self.direction = BeamDirection.RIGHT
            elif self.direction == BeamDirection.DOWN:
                self.direction = BeamDirection.LEFT
            else:
                raise ValueError("Bad Value")
        elif case == "\\":
            if self.direction == BeamDirection.RIGHT:
                self.direction = BeamDirection.DOWN
            elif self.direction == BeamDirection.LEFT:
                self.direction = BeamDirection.UP
            elif self.direction == BeamDirection.UP:
                self.direction = BeamDirection.LEFT
            elif self.direction == BeamDirection.DOWN:
                self.direction = BeamDirection.RIGHT
            else:
                raise ValueError("Bad Value")

    def split_beams(self) -> list["Beam"]:
        new_beams = []
        case = self.contraption_layout[self.i][self.j]
        if case == "|" and self.direction in [BeamDirection.RIGHT, BeamDirection.LEFT]:
            new_beams += [
                Beam(self.contraption_layout, self.i - 1, self.j, BeamDirection.UP, self.beam_cache),
                Beam(self.contraption_layout, self.i + 1, self.j, BeamDirection.DOWN, self.beam_cache),
            ]
        elif case == "-" and self.direction in [BeamDirection.UP, BeamDirection.DOWN]:
            new_beams += [
                Beam(self.contraption_layout, self.i, self.j + 1, BeamDirection.RIGHT, self.beam_cache),
                Beam(self.contraption_layout, self.i, self.j - 1, BeamDirection.LEFT, self.beam_cache),
            ]

        return new_beams

    def go(self) -> tuple[list[tuple[int, int]], list["Beam"]]:
        beam_course = []

        while 0 <= self.i < len(self.contraption_layout) and 0 <= self.j < len(self.contraption_layout[0]):
            beam_course.append((self.i, self.j))

            beam_key_cache = (self.i, self.j, self.direction)
            if beam_key_cache in self.beam_cache:
                return beam_course, []
            else:
                self.beam_cache.append(beam_key_cache)

            new_beams = self.split_beams()
            if new_beams:
                return beam_course, new_beams

            self.get_new_direction()

            self.i, self.j = self.get_next_position()

        return beam_course, []


def run_beam(start_beam: Beam) -> list[tuple[int, int]]:
    beam_course = []
    new_beams = [start_beam]

    while new_beams:
        beam = new_beams.pop(0)
        res_beam_course, res_new_beams = beam.go()

        beam_course += res_beam_course
        new_beams += res_new_beams

    return beam_course


def parse(day_input: str) -> list[list[str]]:
    return [
        [c for c in line]
        for line in day_input.split("\n")
    ]


def main():
    with open("input") as f:
        day_input = f.read().strip()

    contraption_layout = parse(day_input)

    result_list = []
    print("i")
    for i in range(len(contraption_layout)):
        print(i)
        j = 0
        beam_course = run_beam(Beam(contraption_layout, i, j, BeamDirection.RIGHT, beam_cache=[]))
        result_list.append(len(set(beam_course)))

        j = len(contraption_layout[0]) - 1
        beam_course = run_beam(Beam(contraption_layout, i, j, BeamDirection.LEFT, beam_cache=[]))
        result_list.append(len(set(beam_course)))

    print("j")
    for j in range(len(contraption_layout[0])):
        print(j)
        i = 0
        beam_course = run_beam(Beam(contraption_layout, i, j, BeamDirection.DOWN, beam_cache=[]))
        result_list.append(len(set(beam_course)))

        i = len(contraption_layout) - 1
        beam_course = run_beam(Beam(contraption_layout, i, j, BeamDirection.UP, beam_cache=[]))
        result_list.append(len(set(beam_course)))

    print(max(result_list))


if __name__ == "__main__":
    main()
