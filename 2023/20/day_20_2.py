#!/usr/bin/env python
from collections import defaultdict
from enum import Enum
from math import lcm


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


def press_button(modules: dict[str, Module], rx_parent: str, rx_parent_input_cycles: dict[str, int], button_pressed_counter: int) -> None:
    received_pulses = [("button", "broadcaster", PulseEnum.LOW_PULSE)]

    while received_pulses:
        origin_module, module_name, pulse = received_pulses.pop(0)

        if module_name == rx_parent and pulse == PulseEnum.HIGH_PULSE:
            if origin_module not in rx_parent_input_cycles:
                rx_parent_input_cycles[origin_module] = button_pressed_counter

        module = modules[module_name]
        received_pulses += module.receive_pulse(origin_module, pulse)


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    modules = parse(day_input)

    rx_parent = modules["rx"].inputs[0]
    rx_parent_input_cycles = {}

    i = 0
    while True:
        i += 1
        press_button(modules, rx_parent, rx_parent_input_cycles, i)

        if len(modules[rx_parent].inputs) == len(rx_parent_input_cycles.keys()):
            print(lcm(*list(rx_parent_input_cycles.values())))
            return


if __name__ == "__main__":
    main()
