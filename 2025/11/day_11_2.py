#!/usr/bin/env python


def parse(day_input: str) -> dict[str, set[str]]:
    device_dict: dict[str, set[str]] = {}
    for line in day_input.split("\n"):
        source_name, destinations_name_str = line.split(": ")
        device_dict[source_name] = set(destinations_name_str.split(" "))

    return device_dict


def explore_destinations(
        device_name: str,
        goal: str,
        devices_dict: dict[str, set[str]],
        previous_devices: list[str] | None = None,
        cached_explorations: dict[str, int] | None = None,
) -> int:
    if previous_devices is None:
        previous_devices = []
    if cached_explorations is None:
        cached_explorations = {}

    path_counter = 0
    for destination in devices_dict[device_name]:
        if destination in cached_explorations:
            destination_counter = cached_explorations[destination]
        else:
            if destination == goal:
                destination_counter = 1
            else:
                destination_counter = explore_destinations(
                    device_name=destination,
                    devices_dict=devices_dict,
                    previous_devices=previous_devices + [device_name],
                    cached_explorations=cached_explorations,
                    goal=goal
                )
        path_counter += destination_counter

    cached_explorations[device_name] = path_counter
    return path_counter


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    devices_dict = parse(day_input)
    devices_dict["out"] = set()

    # srv -> fft -> dac -> out
    srv_fft = explore_destinations("svr", "fft", devices_dict)
    fft_dac = explore_destinations("fft", "dac", devices_dict)
    dac_out = explore_destinations("dac", "out", devices_dict)
    first_part = srv_fft * fft_dac * dac_out

    # srv -> dac -> fft -> out
    srv_dac = explore_destinations("svr", "dac", devices_dict)
    dac_fft = explore_destinations("dac", "fft", devices_dict)
    fft_out = explore_destinations("fft", "out", devices_dict)
    second_part = srv_dac * dac_fft * fft_out

    result = first_part + second_part
    print(result)


if __name__ == "__main__":
    main()
