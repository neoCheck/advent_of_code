#!/usr/bin/env python


def parse(day_input: str) -> dict[str, set[str]]:
    device_dict: dict[str, set[str]] = {}
    for line in day_input.split("\n"):
        source_name, destinations_name_str = line.split(": ")
        device_dict[source_name] = set(destinations_name_str.split(" "))

    return device_dict


def explore_destinations(
        device_name: str,
        devices_dict: dict[str, set[str]],
        cached_explorations: dict[str, list[str]]
) -> list[str]:
    paths: list[str] = []
    for destination in devices_dict[device_name]:
        if destination in cached_explorations:
            explored_path_list = cached_explorations[destination]
        else:
            if destination == "out":
                explored_path_list = [destination]
            else:
                explored_path_list = explore_destinations(destination, devices_dict, cached_explorations)

            cached_explorations[destination] = explored_path_list

        paths += explored_path_list

    return [f"{device_name}-{p}" for p in paths]


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    devices_dict = parse(day_input)
    cached_explorations = {}

    result = explore_destinations(
        device_name="you",
        devices_dict=devices_dict,
        cached_explorations=cached_explorations,
    )

    print(len(result))


if __name__ == "__main__":
    main()
