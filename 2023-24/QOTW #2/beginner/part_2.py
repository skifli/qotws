"""
One-liner in `part_2-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.


def get_adjacent(coords: tuple[int]):
    return [
        [x, y]
        for y in range(coords[1] - 1, coords[1] + 2)
        for x in range(coords[0] - 1, coords[0] + 2)
        if (x != coords[0] or y != coords[1])
    ]


with open(f"{path}/../assets/grid.txt", "r", encoding="utf-8") as f:
    grid = [[char for char in line if char != "\n"] for line in f.readlines()]

coords = [[27, 32], [91, 98], [12, 87], [46, 17]]

adjacent_coords = [[coord] + get_adjacent(coord) for coord in coords]

for adj_coord in adjacent_coords:
    l_num = 0

    for coord in adj_coord[1:]:
        if (
            coord[0] > 0
            and coord[0] < len(grid[0])
            and coord[1] > 0
            and coord[1] < len(grid)
        ):
            l_num += 1 if grid[coord[1]][coord[0]] == "L" else 0

    print(f"{adj_coord[0]}: {l_num}")
