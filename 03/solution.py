"""--- Day 3: Lobby ---

https://adventofcode.com/2025/day/3
"""

from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from numpy.typing import NDArray


def maximum_joltage_sum(
    filepath: str, n_batteries: int = 2, verbose: bool = False
) -> int:
    """Maximum joltage sum."""
    with Path(filepath).open("rb") as f:
        return sum(
            get_max_joltage(
                np.frombuffer(bank.strip(), dtype=np.uint8) - ord("0"),
                n_batteries,
                verbose,
            )
            for bank in f.readlines()
        )


def get_max_joltage(
    bank: NDArray[np.integer], n_batteries: int = 2, verbose: bool = False
) -> int:
    """Get the maximum joltage sum."""
    batteries_on = np.zeros((n_batteries,), dtype=np.uint)
    argmax = 0
    for i in range(n_batteries):
        _slice = slice(argmax, len(bank) - n_batteries + i + 1)
        argmax += bank[_slice].argmax().item()
        batteries_on[i] = argmax
        argmax += 1  # skip the battery we just turned on

    if verbose:
        print(f"{batteries_on=}")
    return int("".join(map(str, bank[batteries_on])))


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Usage: python solution.py <example.txt | input.txt>")
        sys.exit(1)

    input_fpath = sys.argv[1]
    print("Solution 1:", maximum_joltage_sum(input_fpath, n_batteries=2))
    print("Solution 2:", maximum_joltage_sum(input_fpath, n_batteries=12))
