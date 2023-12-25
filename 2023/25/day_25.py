#!/usr/bin/env python
from collections import defaultdict
import networkx as nx


def parse(day_input: str) -> dict[str, set[str]]:
    node_dict = defaultdict(set)
    for line in day_input.split("\n"):
        source_name, destinations_name_str = line.split(": ")
        for destination_name in destinations_name_str.split(" "):
            node_dict[source_name].add(destination_name)
            node_dict[destination_name].add(source_name)

    return node_dict


def create_graph(node_dict: dict[str, set[str]]) -> nx.DiGraph:
    # https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.minimum_cut.html
    graph = nx.DiGraph()
    for node, linked_nodes in node_dict.items():
        for ln in linked_nodes:
            graph.add_edge(node, ln, capacity=1.0)
            graph.add_edge(ln, node, capacity=1.0)

    return graph


def solve(node_dict: dict[str, set[str]], graph: nx.DiGraph) -> int:
    for node_1, nodes in node_dict.items():
        for node_2 in nodes:
            cut_value, partition = nx.minimum_cut(graph, node_1, node_2)
            if cut_value == 3:
                return len(partition[0]) * len(partition[1])

    raise ValueError("No solution")


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    node_dict = parse(day_input)
    graph = create_graph(node_dict)
    result = solve(node_dict, graph)

    print(result)


if __name__ == "__main__":
    main()
