#!/usr/bin/env python


def parse(day_input: str) -> dict[str, tuple[int, int, int]]:
    reindeer_stats = {}
    for line in day_input.split("\n"):
        line = (
            line.replace("can fly ", "")
                .replace("km/s for ", "")
                .replace("seconds, but then must rest for ", "")
                .replace(" seconds.", "")
        )
        name, speed, duration, rest_duration = line.split(" ")
        reindeer_stats[name] = (int(speed), int(duration), int(rest_duration))

    return reindeer_stats


def calculate_distance(challenge_duration: int, speed: int, duration: int, rest_duration: int) -> int:
    cycle_duration = duration + rest_duration
    cycle_num = int(challenge_duration / cycle_duration)

    distance = (speed * duration) * cycle_num
    remaining_duration = challenge_duration - (cycle_duration * cycle_num)
    distance += (speed * min(remaining_duration, duration))

    return distance

def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    challenge_duration = 2503

    parsed_input = parse(day_input)

    list_distances = []
    for name, (speed, duration, rest_duration) in parsed_input.items():
        distance = calculate_distance(challenge_duration, speed, duration, rest_duration)
        list_distances.append(distance)

    print(max(list_distances))


if __name__ == "__main__":
    main()
