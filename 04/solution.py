"""--- Day 4: Printing Department ---

https://adventofcode.com/2025/day/4
"""

from pathlib import Path

import cv2
import numpy as np


def load_grid(filepath: str) -> np.ndarray:
    """Load grid and replace all '.' for 0s and '@' for 1s."""
    with Path(filepath).open("rb") as f:
        lines = [
            np.frombuffer(
                line.strip().replace(b".", b"0").replace(b"@", b"1"), dtype=np.uint8
            )
            - ord("0")
            for line in f.readlines()
        ]

    return np.array(lines)


def get_removable_rolls(
    grid: np.ndarray, max_adjacent_rolls: int = 4, max_iters: int | None = None
) -> int:
    """Get rolls to be removed by using convolution to count adjacent rolls."""
    kernel = np.ones((3, 3))
    total = 0

    for _ in range(max_iters or np.iinfo(np.int32).max):
        conv = cv2.filter2D(grid, -1, kernel=kernel, borderType=cv2.BORDER_CONSTANT)
        removable = (grid != 0) & (conv <= max_adjacent_rolls)

        if removable.sum() == 0:
            break

        total += removable.sum()
        grid[removable] = 0

    return total


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Usage: python solution.py <example.txt | input.txt>")
        sys.exit(1)

    input_fpath = sys.argv[1]
    grid = load_grid(input_fpath)

    print("Solution 1:", get_removable_rolls(grid.copy(), max_iters=1))
    print("Solution 2:", get_removable_rolls(grid.copy()))
