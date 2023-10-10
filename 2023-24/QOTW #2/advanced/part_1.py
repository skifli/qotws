"""
One-liner in `part_1-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.

with open(f"{path}/../assets/grid.txt", "r", encoding="utf-8") as f:
    grid = [[char for char in line if char != "\n"] for line in f.readlines()]

coords = [[x, y] for y in range(len(grid)) for x in range(len(grid[0]))]

deep_s_num = 0

for char_coord in coords:
    if grid[char_coord[1]][char_coord[0]] == "S":
        within_5_taxicab_units = [
            coord
            for coord in coords
            if abs(coord[0] - char_coord[0]) + abs(coord[1] - char_coord[1]) <= 5
        ]

        failed = False

        for coord in within_5_taxicab_units:
            if (
                coord[0] > 0
                and coord[0] < len(grid[0])
                and coord[1] > 0
                and coord[1] < len(grid)
            ):
                if grid[coord[1]][coord[0]] == "L":
                    failed = True
                    break

        if not failed:
            deep_s_num += 1

print(deep_s_num)
