"""
One-liner in `part_2-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.


def get_adjacent(coords: tuple[int], sub=[]):
    if not coords:
        return [sub]
    else:
        result = []

        for index in range(coords[0] - 1, coords[0] + 2):
            result.extend(get_adjacent(coords[1:], sub + [index]))

        if len(coords) == 2:
            result.remove(coords)

        return result


with open(f"{path}/assets/grid.txt", "r", encoding="utf-8") as f:
    grid = [[char for char in line if char != "\n"] for line in f.readlines()]

coords = [
    int(element)
    for element in input("Enter coordinates (x, y): ")
    .replace("(", "")
    .replace(")", "")
    .strip()
    .split(",")
]
adjacent_coords = get_adjacent(coords)

l_num = 0

for coord in adjacent_coords:
    if (
        coord[0] > 0
        and coord[0] < len(grid[0])
        and coord[1] > 0
        and coord[1] < len(grid)
    ):
        l_num += 1 if grid[coord[1]][coord[0]] == "L" else 0

print(l_num)
