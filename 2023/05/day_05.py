#!/usr/bin/env python


class SourceDestinationMapper:
    def __init__(self, source: str, destination: str):
        self.source = source
        self.destination = destination
        self.map: dict[range, range] = {}

    def add_range_correspondance(self, source_range_start: int, destination_range_start: int, range_length: int) -> None:
        source_range = range(source_range_start, source_range_start + range_length)
        destination_range = range(destination_range_start, destination_range_start + range_length)
        self.map[source_range] = destination_range

    def get_destination_from_source(self, source: int) -> int:
        for source_range, destination_range in self.map.items():
            if source in source_range:
                index = source_range.index(source)
                return destination_range.start + index

        return source


def parse_map(map_info: str) -> SourceDestinationMapper:
    src_dst_str, numbers_str = map_info.split(" map:\n")
    source, destination = src_dst_str.split("-to-")

    mapper = SourceDestinationMapper(source, destination)

    numbers_str_list = numbers_str.split("\n")

    for nb_str in numbers_str_list:
        destination_range_start, source_range_start, range_length = nb_str.split(" ")
        mapper.add_range_correspondance(int(source_range_start), int(destination_range_start), int(range_length))

    return mapper


def parse(day_input: str) -> tuple[list[int], dict[tuple[str, str], SourceDestinationMapper]]:
    seeds_str, *info = day_input.split("\n\n")

    _, seeds_str = seeds_str.split(": ")
    seeds = [int(s) for s in seeds_str.split(" ") if s.isdigit()]

    correspondance = {}

    for map_info in info:
        mapper = parse_map(map_info)
        correspondance[mapper.source, mapper.destination] = mapper

    return seeds, correspondance


def seed_location(seed: int, correspondance: dict[tuple[str, str], SourceDestinationMapper]) -> int:
    soil = correspondance["seed", "soil"].get_destination_from_source(seed)
    fertilizer = correspondance["soil", "fertilizer"].get_destination_from_source(soil)
    water = correspondance["fertilizer", "water"].get_destination_from_source(fertilizer)
    light = correspondance["water", "light"].get_destination_from_source(water)
    temperature = correspondance["light", "temperature"].get_destination_from_source(light)
    humidity = correspondance["temperature", "humidity"].get_destination_from_source(temperature)
    location = correspondance["humidity", "location"].get_destination_from_source(humidity)

    return location


if __name__ == "__main__":
    input_ = open("input").read().strip()
    seed_list, correspondance_map = parse(input_)
    location_list = [seed_location(s, correspondance_map) for s in seed_list]
    print(min(location_list))
