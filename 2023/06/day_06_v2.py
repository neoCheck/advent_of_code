#!/usr/bin/env python

from math import sqrt, ceil


class BoatRaceRecord:
    def __init__(self, time: int, distance: int) -> None:
        self.time = time
        self.distance = distance

    def __str__(self):
        return f"BoatRecord: time {self.time} distance {self.distance}"

    def count_ways_to_beat_distance(self):
        delta = self.time ** 2 - 4 * self.distance
        x_1 = (self.time - sqrt(delta)) / 2
        x_2 = (self.time + sqrt(delta)) / 2

        x_1 = x_1 + 1 if int(x_1) - x_1 == 0 else ceil(x_1)
        x_2 = x_2 - 1 if int(x_2) - x_2 == 0 else int(x_2)

        if x_1 > x_2:
            return 0
        return x_2 - x_1 + 1


def parse(day_input: str) -> list[BoatRaceRecord]:
    time_str, distance_str = day_input.split("\n")
    time_str = time_str.replace("Time:", "")
    distance_str = distance_str.replace("Distance:", "")

    time_list = [int(s) for s in time_str.split(" ") if s.isdigit()]
    distance_list = [int(s) for s in distance_str.split(" ") if s.isdigit()]

    time_distance_list = zip(time_list, distance_list)
    return [BoatRaceRecord(time, distance) for time, distance in time_distance_list]


if __name__ == "__main__":
    input_ = open("input").read().strip()
    result = parse(input_)

    n_ways = 1
    for r in result:
        n_ways = n_ways * r.count_ways_to_beat_distance()

    print(n_ways)
