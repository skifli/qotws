"""
One-liner in `part_2-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.


def taxicab_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


with open(f"{path}/../assets/grid.txt", "r", encoding="utf-8") as f:
    grid = [[char for char in line if char != "\n"] for line in f.readlines()]

max_distance = 0
max_distance_coords = (0, 0)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "L":
            min_distance_to_s = min(
                taxicab_distance(y, x, x2, y2)
                for x2 in range(len(grid))
                for y2 in range(len(grid[0]))
                if grid[x2][y2] == "S"
            )

            if min_distance_to_s > max_distance:
                max_distance = min_distance_to_s
                max_distance_coords = (y, x)

print(max_distance_coords)
