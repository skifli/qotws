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
        if not (
            (x == coords[0] and y == coords[1])
            or (x == coords[0] - 1 and y == coords[1] - 1)
            or (x == coords[0] - 1 and y == coords[1] + 1)
            or (x == coords[0] + 1 and y == coords[1] - 1)
            or (x == coords[0] + 1 and y == coords[1] + 1)
        )
    ]


with open(f"{path}/../assets/grid.txt", "r", encoding="utf-8") as f:
    grid = [[char for char in line if char != "\n"] for line in f.readlines()]

coords = [
    [x, y] for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "L"
]

l_which_dont_border_s = 0

for coord in coords:
    adjacent_coords = get_adjacent(coord)

    failed = False

    for coord in adjacent_coords:
        if (
            coord[0] > 0
            and coord[0] < len(grid[0])
            and coord[1] > 0
            and coord[1] < len(grid)
        ):
            if grid[coord[1]][coord[0]] == "S":
                failed = True
                break

    if not failed:
        l_which_dont_border_s += 1

print(l_which_dont_border_s)
