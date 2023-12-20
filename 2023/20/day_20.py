#!/usr/bin/env python
from collections import defaultdict
from enum import Enum


class PulseEnum(Enum):
    LOW_PULSE = 1
    HIGH_PULSE = 2


class Module:
    def __init__(self, name: str, outputs: list[str], inputs: list[str]) -> None:
        self.name = name
        self.outputs = outputs
        self.inputs = inputs

    def receive_pulse(self, pulse_origin: str, pulse: PulseEnum) -> list[tuple[str, str, PulseEnum]]:
        raise NotImplemented()


class BroadcasterModule(Module):
    def receive_pulse(self, pulse_origin: str, pulse: PulseEnum) -> list[tuple[str, str, PulseEnum]]:
        return [(self.name, output, PulseEnum.LOW_PULSE) for output in self.outputs]


class NoOutputModule(Module):
    def receive_pulse(self, pulse_origin: str, pulse: PulseEnum) -> list[tuple[str, str, PulseEnum]]:
        return []


class FlipFlopModule(Module):
    def __init__(self, name: str, outputs: list[str], inputs: list[str]) -> None:
        super().__init__(name, outputs, inputs)

        self.is_on = False

    def receive_pulse(self, pulse_origin: str, pulse: PulseEnum) -> list[tuple[str, str, PulseEnum]]:
        if pulse == PulseEnum.LOW_PULSE:
            if self.is_on:
                self.is_on = False
                return [(self.name, output, PulseEnum.LOW_PULSE) for output in self.outputs]
            else:
                self.is_on = True
                return [(self.name, output, PulseEnum.HIGH_PULSE) for output in self.outputs]

        return []


class ConjunctionModule(Module):
    def __init__(self, name: str, outputs: list[str], inputs: list[str]) -> None:
        super().__init__(name, outputs, inputs)

        self.inputs_pulse = {input_: PulseEnum.LOW_PULSE for input_ in inputs}

    def receive_pulse(self, pulse_origin: str, pulse: PulseEnum) -> list[tuple[str, str, PulseEnum]]:
        self.inputs_pulse[pulse_origin] = pulse

        if all([p == PulseEnum.HIGH_PULSE for p in self.inputs_pulse.values()]):
            return [(self.name, output, PulseEnum.LOW_PULSE) for output in self.outputs]
        else:
            return [(self.name, output, PulseEnum.HIGH_PULSE) for output in self.outputs]


def parse(day_input: str) -> dict[str, Module]:
    output_dict = defaultdict(list)
    input_dict = defaultdict(list)
    module_class_map = {}

    for line in day_input.split("\n"):
        source, destinations_str = line.split(" -> ")
        destinations = destinations_str.split(", ")

        if source.startswith("%"):
            source = source[1:]
            module_class_map[source] = FlipFlopModule
        elif source.startswith("&"):
            source = source[1:]
            module_class_map[source] = ConjunctionModule
        else:
            module_class_map[source] = BroadcasterModule

        output_dict[source] += destinations
        for des in destinations:
            input_dict[des] += [source]

    modules = {}

    for module_name, ModuleClass in module_class_map.items():
        modules[module_name] = ModuleClass(module_name, output_dict[module_name], input_dict[module_name])

    no_output_modules = set(input_dict.keys()) - set(output_dict.keys())
    for module_name in no_output_modules:
        modules[module_name] = NoOutputModule(module_name, output_dict[module_name], input_dict[module_name])

    return modules


def press_button(modules: dict[str, Module]) -> tuple[int, int]:
    low_pulse_counter = 0
    high_pulse_counter = 0
    received_pulses = [("button", "broadcaster", PulseEnum.LOW_PULSE)]

    while received_pulses:
        origin_module, module_name, pulse = received_pulses.pop(0)

        if pulse == PulseEnum.LOW_PULSE:
            low_pulse_counter += 1
        else:
            high_pulse_counter += 1
        # print(f"{origin_module} -{ 'low' if pulse == PulseEnum.LOW_PULSE else 'high'}-> {module_name}")

        module = modules[module_name]
        received_pulses += module.receive_pulse(origin_module, pulse)

    return low_pulse_counter, high_pulse_counter


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    modules = parse(day_input)

    low_pulse_counter = 0
    high_pulse_counter = 0

    for _ in range(1_000):
        new_low_pulse, new_high_pulse = press_button(modules)
        low_pulse_counter += new_low_pulse
        high_pulse_counter += new_high_pulse

    print(low_pulse_counter)
    print(high_pulse_counter)
    print(low_pulse_counter * high_pulse_counter)


if __name__ == "__main__":
    main()
