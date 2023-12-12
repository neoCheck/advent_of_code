#!/usr/bin/env python

# Using dynamic programming
def calculate_valid_combinations(row: str, group_sizes: list[int], cached_info: dict, row_index: int, group_index: int, current_group_size: int):
    """
    Calculate the number of valid arrangements for a given row of springs and its contiguous groups of damaged springs.

    Parameters:
    - row: The row of springs (operational, damaged, or unknown).
    - group_sizes: The list of contiguous groups of damaged springs.
    - cached_info: Dictionary for memoization to store previously computed results.
    - row_index: Current index in the row of springs.
    - group_index: Current index in the list of contiguous groups.
    - current_group_size: Current size of the contiguous group.

    Returns:
    - The count of valid arrangements for the given state.
    """

    # Create a cache key based on the current indices and state
    cache_key = (row_index, group_index, current_group_size)

    # Check if the result for the current state is already in the cache
    if cache_key in cached_info:
        return cached_info[cache_key]

    # Base case: If we have reached the end of the row, check if all groups have been considered.
    if row_index == len(row):
        return 1 if ((group_index == len(group_sizes) and current_group_size == 0) or
                     (group_index == (len(group_sizes) - 1) and group_sizes[group_index] == current_group_size)) else 0

    # Initialize the result count for the current state
    res = 0

    # Explore possibilities when the current spring is operational or unknown
    if row[row_index] in ["?", "."]:
        if current_group_size == 0:
            # If the current contiguous group is empty, move to the next spring
            res += calculate_valid_combinations(row, group_sizes, cached_info, row_index + 1, group_index, 0)
        elif current_group_size > 0 and group_index < len(group_sizes) and group_sizes[group_index] == current_group_size:
            # If the current contiguous group is non-empty and matches the size, move to the next group
            res += calculate_valid_combinations(row, group_sizes, cached_info, row_index + 1, group_index + 1, 0)

    # Explore possibilities when the current spring is damaged or unknown
    if row[row_index] in ["?", "#"]:
        # Move to the next spring and increment the size of the current contiguous group
        res += calculate_valid_combinations(row, group_sizes, cached_info, row_index + 1, group_index, current_group_size + 1)

    # Cache the result for the current state
    cached_info[cache_key] = res

    return res


def parse_input(input_string: str) -> list[tuple[str, list[int]]]:
    """
    Parse the input string to obtain a list of rows and contiguous groups.

    Parameters:
    - input_string: The input string containing rows and contiguous groups.

    Returns:
    - A list of tuples, where each tuple contains a row of springs and a list of contiguous groups.
    """

    parsed_lines = []
    for line in input_string.split("\n"):
        row, group_sizes = line.split(" ")
        # Multiply each group size by 5 to unfold the records
        group_sizes = [int(size) for size in group_sizes.split(",")] * 5
        # Unfold the row of springs by adding '?' between each original spring
        row = f"{'?'.join([row] * 5)}"

        parsed_lines.append((row, group_sizes))

    return parsed_lines


def main():
    # Read the input from a file (consider making the file name a command-line argument)
    with open("input") as file:
        input_data = file.read().strip()

    # Parse the input to obtain a list of rows and contiguous groups
    parsed_data = parse_input(input_data)

    # Calculate and print the sum of valid combinations for all rows
    total_combinations = sum([calculate_valid_combinations(row, group_sizes, {}, 0, 0, 0) for row, group_sizes in parsed_data])
    print(total_combinations)


if __name__ == "__main__":
    main()
