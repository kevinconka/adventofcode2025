"""--- Day 1: Secret Entrance ---

https://adventofcode.com/2025/day/1
"""

from pathlib import Path
from typing import Generator


def dial_positions_and_zero_crossings(
    filepath: str, starting_position: int = 50, max_value: int = 100
) -> Generator[tuple[int, int], None, None]:
    """Generator of (position, zero_crossings)."""
    position = starting_position % max_value

    with Path(filepath).open("r", encoding="utf-8") as file:
        for line in file:
            sign = -1 if line[0] == "L" else 1
            steps = int(line[1:])

            # Solve for k in: (position + k*sign) % max_value == 0
            k0 = (-position * sign) % max_value

            # avoid counting initial position as a zero crossing (k0 == 0)
            first = max_value if k0 == 0 else k0
            zero_crossings = max(0, 1 + (steps - first) // max_value)

            # advance position
            position = (position + sign * steps) % max_value

            yield position, zero_crossings


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Usage: python solution.py <example.txt | input.txt>")
        sys.exit(1)

    input_fpath = sys.argv[1]
    password = sum(
        val == 0 for val, _ in dial_positions_and_zero_crossings(input_fpath)
    )
    print(f"Part 1: {password=}")

    password = sum(
        zero_xings for _, zero_xings in dial_positions_and_zero_crossings(input_fpath)
    )
    print(f"Part 2: {password=}")
