from collections import deque


T_GRID = list[list[str]]
T_VERTEX = tuple[int, int]
T_EDGE = dict[T_VERTEX, list[tuple[T_VERTEX, int]]]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def parse(day_input: str) -> T_GRID:
    return [
        [c for c in line]
        for line in day_input.split("\n")
    ]


def build_graph(grid: T_GRID, rows: int, cols: int) -> tuple[T_VERTEX, T_VERTEX, T_EDGE]:
    """
     - Identifies vertices in the grid based on certain conditions (not being '#', having more than 2 neighbors).
     - Initializes a set of vertices and finds the start and end vertices.
     - Builds a graph represented as a dictionary of edges for each vertex.
    """
    vertices = set()

    for row_idx, grid_row in enumerate(grid):
        for col_idx, cell in enumerate(grid_row):
            if cell != "#":
                neighbors_count = sum(
                    1 for dr, dc in DIRECTIONS
                    if 0 <= row_idx + dr < rows and 0 <= col_idx + dc < cols and grid[row_idx + dr][col_idx + dc] != '#'
                )

                if neighbors_count > 2:
                    vertices.add((row_idx, col_idx))

    start, end = None, None
    for col_idx, cell in enumerate(grid[0]):
        if cell == '.':
            vertices.add((0, col_idx))
            start = (0, col_idx)
        if grid[rows - 1][col_idx] == '.':
            vertices.add((rows - 1, col_idx))
            end = (rows - 1, col_idx)

    edges = {}
    for vertex in vertices:
        edges[vertex] = []
        queue = deque([(vertex[0], vertex[1], 0)])
        seen = set()

        while queue:
            current_row, current_col, distance = queue.popleft()

            if (current_row, current_col) in seen:
                continue
            seen.add((current_row, current_col))

            if (current_row, current_col) in vertices and (current_row, current_col) != vertex:
                edges[vertex].append(((current_row, current_col), distance))
                continue

            for dr, dc in DIRECTIONS:
                next_row, next_col = current_row + dr, current_col + dc
                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] != '#':
                    queue.append((next_row, next_col, distance + 1))

    return start, end, edges


def depth_first_search(
        vertex: T_VERTEX,
        distance: int,
        seen: list[list[bool]],
        edges: T_EDGE,
        rows: int,
        count: int,
        max_distance: int
) -> tuple[int, int]:
    """
    - Recursively explores paths in a grid-based graph.
    - Counts valid paths and determines the maximum distance.
    - Utilizes backtracking to traverse vertices efficiently.
    - Marks and unmarks visited vertices during exploration.
    - Specifically designed for grid-based graph traversal.
    - Tracks the count and maximum distance as it explores.
    - Returns the final count and maximum distance achieved.
    """
    row, col = vertex

    if seen[row][col]:
        return count, max_distance

    seen[row][col] = True

    if row == rows - 1:
        count += 1
        max_distance = max(max_distance, distance)

    for (neighbor, neighbor_distance) in edges[vertex]:
        count, max_distance = depth_first_search(neighbor, distance + neighbor_distance, seen, edges, rows, count,
                                                 max_distance)

    seen[row][col] = False
    return count, max_distance


def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    grid = parse(day_input)
    rows, cols = len(grid), len(grid[0])

    start_vertex, end_vertex, graph_edges = build_graph(grid, rows, cols)

    seen_vertices = [[False for _ in range(cols)] for _ in range(rows)]
    count, max_distance = depth_first_search(start_vertex, 0, seen_vertices, graph_edges, rows, 0, 0)

    print(max_distance)


if __name__ == "__main__":
    main()
