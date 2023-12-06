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

    def get_destination_ranges(self, source_l: list[range]) -> list[range]:
        range_l = []
        for source_range, destination_range in self.map.items():

            new_range_l = []
            while source_l:
                source = source_l.pop()

                before = range(source.start, min(source.stop, source_range.start))
                inter = range(max(source.start, source_range.start), min(source_range.stop, source.stop))
                after = range(max(source_range.stop, source.start), source.stop)

                if before.stop > before.start:
                    new_range_l.append(before)
                if inter.stop > inter.start:
                    range_l.append(range(
                        inter.start - source_range.start + destination_range.start,
                        inter.stop - source_range.start + destination_range.start
                    ))
                if after.stop > after.start:
                    new_range_l.append(after)

            source_l = new_range_l
        return range_l + source_l


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


def seed_location_range(seed: range, correspondance: dict[tuple[str, str], SourceDestinationMapper]) -> list[range]:
    soil = correspondance["seed", "soil"].get_destination_ranges([seed])
    fertilizer = correspondance["soil", "fertilizer"].get_destination_ranges(soil)
    water = correspondance["fertilizer", "water"].get_destination_ranges(fertilizer)
    light = correspondance["water", "light"].get_destination_ranges(water)
    temperature = correspondance["light", "temperature"].get_destination_ranges(light)
    humidity = correspondance["temperature", "humidity"].get_destination_ranges(temperature)
    location = correspondance["humidity", "location"].get_destination_ranges(humidity)

    return location


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == "__main__":
    input_ = open("input").read().strip()
    seed_list, correspondance_map = parse(input_)
    seed_ranges_list = [range(start, start + length) for start, length in list(chunks(seed_list, 2))]

    locations = []
    for s in seed_ranges_list:
        locations += seed_location_range(s, correspondance_map)

    locations_start = [l.start for l in locations]
    print(min(locations_start))
