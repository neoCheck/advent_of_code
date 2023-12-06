#!/usr/bin/env python


class BoatRaceRecord:
    def __init__(self, time: int, distance: int) -> None:
        self.time = time
        self.distance = distance

    def __str__(self):
        return f"BoatRecord: time {self.time} distance {self.distance}"

    def list_ways(self):
        return [speed * (self.time - speed) for speed in range(0, self.time + 1)]

    def count_ways_to_beat_distance(self):
        return len([w for w in self.list_ways() if w > self.distance])


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
