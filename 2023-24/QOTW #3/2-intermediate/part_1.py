"""
One-liner in `part_1-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.


def f_function(x, y) -> int:
    """
    Sum of the 9 numbers in a 3x3 around (x, y)."""

    return sum(
        [int(parsed_map[y + dy][x + dx]) for dy in range(-1, 2) for dx in range(-1, 2)]
    )


with open(f"{path}/../assets/map.txt", "r", encoding="utf-8") as f:
    parsed_map = [[char for char in line.strip()] for line in f.readlines()]

print(f"f(f(1, 1), f(98, 98)): {f_function(f_function(1, 1), f_function(98, 98))}")
