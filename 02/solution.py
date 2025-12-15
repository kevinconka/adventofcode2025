"""--- Day 2: Gift Shop ---

https://adventofcode.com/2025/day/2
"""

from pathlib import Path
from typing import Generator, Optional


def process_ranges(
    filepath: str, times_repeated: Optional[int] = None
) -> Generator[list[int], None, None]:
    """Return a generator of integers from the input file."""
    with Path(filepath).open("r", encoding="utf-8") as file:
        for line in file:
            for id_range in line.split(","):
                start, stop = id_range.split("-")
                yield [
                    id_
                    for id_ in range(int(start), int(stop) + 1)
                    if is_invalid(id_, times_repeated)
                ]


def is_invalid(id_: int, times_repeated: Optional[int] = None) -> bool:
    """Return True if the ID is invalid, False otherwise."""
    id_repr = str(id_)
    id_len = len(id_repr)

    if times_repeated is not None:
        chunk = id_repr[0 : id_len // times_repeated]
        return chunk * times_repeated == id_repr

    for i in range(1, id_len // 2 + 1):
        chunk = id_repr[0:i]
        if chunk * (id_len // len(chunk)) == id_repr:
            return True
    return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Usage: python solution.py <example.txt | input.txt>")
        sys.exit(1)

    fpath = sys.argv[1]
    answer = sum(
        sum(invalid_ids) for invalid_ids in process_ranges(fpath, times_repeated=2)
    )
    print(f"Part 1: Invalid IDs sum is {answer}")

    answer = sum(sum(invalid_ids) for invalid_ids in process_ranges(fpath))
    print(f"Part 2: Invalid IDs sum is {answer}")
