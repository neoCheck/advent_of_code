#!/usr/bin/env python

class Reindeer:
    name: str
    speed: int
    speed_duration: int
    rest_duration: int

    remaining_speed_duration: int
    remaining_rest_duration: int
    distance: int
    score: int

    def __init__(self, name: str, speed: int, speed_duration: int, rest_duration: int) -> None:
        self.name = name
        self.speed = speed
        self.speed_duration = speed_duration
        self.rest_duration = rest_duration

        self.remaining_speed_duration = speed_duration
        self.remaining_rest_duration = 0
        self.distance = 0
        self.score = 0

    def run_for_one_second(self) -> None:
        if self.remaining_rest_duration == 0:
            self.distance += self.speed
            self.remaining_speed_duration -= 1
            if self.remaining_speed_duration == 0:
                self.remaining_rest_duration = self.rest_duration

        elif self.remaining_speed_duration == 0:
            self.remaining_rest_duration -= 1
            if self.remaining_rest_duration == 0:
                self.remaining_speed_duration = self.speed_duration

    def __repr__(self) -> str:
        return f"Reindeer {self.name} : {self.distance} {self.score}"



def parse(day_input: str) -> list[Reindeer]:
    reindeer_list = []
    for line in day_input.split("\n"):
        line = (
            line.replace("can fly ", "")
                .replace("km/s for ", "")
                .replace("seconds, but then must rest for ", "")
                .replace(" seconds.", "")
        )
        name, speed, duration, rest_duration = line.split(" ")
        reindeer_list.append(Reindeer(name, int(speed), int(duration), int(rest_duration)))

    return reindeer_list


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    challenge_duration = 2503

    reindeer_list = parse(day_input)

    for i in range(challenge_duration):

        for reindeer in reindeer_list:
            reindeer.run_for_one_second()

        max_distance = max(r.distance for r in reindeer_list)
        top_reindeer_list = [r for r in reindeer_list if r.distance == max_distance]

        for top_reindeer in top_reindeer_list:
            top_reindeer.score += 1

    top_reindeer = sorted(reindeer_list, key=lambda r: r.score, reverse=True)[0]
    print(top_reindeer.score)

if __name__ == "__main__":
    main()
