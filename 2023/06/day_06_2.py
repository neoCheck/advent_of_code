#!/usr/bin/env python

DAY_6_INPUT = """Time:        54     94     65     92
Distance:   302   1476   1029   1404"""


class BoatRaceRecord:
    def __init__(self, time: int, distance: int) -> None:
        self.time = time
        self.distance = distance

    def __str__(self):
        return f"BoatRecord: time {self.time} distance {self.distance}"

    def count_ways_to_beat_distance(self):
        counter = 0
        for speed in range(0, self.time + 1):
            d = speed * (self.time - speed)

            if d > self.distance:
                counter += 1

        return counter


def parse(day_input: str) -> list[BoatRaceRecord]:
    time_str, distance_str = day_input.split("\n")
    time_str = time_str.replace("Time:", "").replace(" ", "")
    distance_str = distance_str.replace("Distance:", "").replace(" ", "")

    time_list = [int(s) for s in time_str.split(" ") if s.isdigit()]
    distance_list = [int(s) for s in distance_str.split(" ") if s.isdigit()]

    time_distance_list = zip(time_list, distance_list)
    return [BoatRaceRecord(time, distance) for time, distance in time_distance_list]


if __name__ == "__main__":
    result = parse(DAY_6_INPUT)

    n_ways = 1
    for r in result:
        n_ways = n_ways * r.count_ways_to_beat_distance()

    print(n_ways)
