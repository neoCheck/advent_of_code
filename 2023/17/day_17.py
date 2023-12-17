#!/usr/bin/env python
import heapq


def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    start = (0, 0)
    destination = (rows - 1, cols - 1)

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Priority queue to store (heat loss, position, direction, consecutive_blocks) tuples
    pq = [(0, start, 0, 0)]

    # Dictionary to store the minimum heat loss for each position and direction
    heat_loss_dict = {(start, 0, 0): 0}

    while pq:
        heat_loss, current, direction, consecutive_blocks = heapq.heappop(pq)

        if current == destination:
            return heat_loss

        for new_direction, new_direction_pos in enumerate(directions):
            new_consecutive_blocks = consecutive_blocks + 1 if new_direction == direction else 1

            is_reverse = ((new_direction + 2) % 4 == direction)
            if is_reverse:
                continue  # Skip going backwards
            if new_consecutive_blocks > 3:
                continue  # Skip if moving more than three consecutive blocks in the same direction

            next_pos = (current[0] + new_direction_pos[0], current[1] + new_direction_pos[1])
            next_state = (next_pos, new_direction, new_consecutive_blocks)
            if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols:
                new_heat_loss = heat_loss + grid[next_pos[0]][next_pos[1]]

                if new_heat_loss < heat_loss_dict.get(next_state, float('inf')):
                    heat_loss_dict[next_state] = new_heat_loss
                    heapq.heappush(pq, (new_heat_loss, next_pos, new_direction, new_consecutive_blocks))

    return float('inf')  # If no path is found


def parse(day_input: str) -> list[list[int]]:
    return [
        [int(c) for c in line]
        for line in day_input.split("\n")
    ]


def main():
    with open("input") as f:
        day_input = f.read().strip()

    grid = parse(day_input)
    result = dijkstra(grid)
    print(result)


if __name__ == "__main__":
    main()
