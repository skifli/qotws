"""
One-liner in `part_2-oneliner.py`.
"""

from os.path import split


def return_corner_chars(x, y) -> int:
    """
    Returns the chars in the corners around (x, y)."""

    print(x, y)

    coords = [
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y + 1),
    ]

    coord_chars = []

    for coord in coords:
        if (
            coord[1] < 0
            or coord[0] < 0
            or coord[1] >= len(inscription)
            or coord[0] >= len(inscription[coord[1]])
        ):
            coord_chars.append(" ")
        else:
            coord_chars.append(inscription[coord[1]][coord[0]])

    return coord_chars


path = split(__file__)[0]  # If terminal cwd is different from program path.

with open(f"{path}/../assets/inscription.txt", "r", encoding="utf-8") as f:
    inscription = [[char for char in line.strip()] for line in f.readlines()]

# In how many 3x3 blocks in inscription.txt are at least the corners filled in

print(
    sum(
        [
            all([char != " " for char in return_corner_chars(x, y)])
            for y in range(1, len(inscription))
            for x in range(1, len(inscription[y]))
        ]
    )
)
