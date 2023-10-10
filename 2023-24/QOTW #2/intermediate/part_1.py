"""
One-liner in `part_1-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.


def calculate_distance(corner_flag):
    index = (
        (0, 0)
        if corner_flag == "TOP_LEFT"
        else (0, len(grid[0]) - 1)
        if corner_flag == "TOP_RIGHT"
        else (len(grid) - 1, len(grid[0]) - 1)
        if corner_flag == "BOTTOM_RIGHT"
        else (len(grid) - 1, 0)
    )

    l_indexes = []

    for y_index in range(len(grid)):
        for x_index in range(len(grid[y_index])):
            if grid[y_index][x_index] == "L":
                l_indexes.append((y_index, x_index))

    l_indexes_distances = []

    for l_index in l_indexes:
        l_indexes_distances.append(
            (l_index[0] - 0 if "LEFT" in corner_flag else len(grid) - 1 - l_index[0])
            + (
                l_index[1] - 0
                if "TOP" in corner_flag
                else len(grid[0]) - 1 - l_index[1]
            )
        )

    return sorted(l_indexes_distances)[0]


with open(f"{path}/../assets/grid.txt", "r", encoding="utf-8") as f:
    grid = [[char for char in line if char != "\n"] for line in f.readlines()]

if __name__ == "__main__":
    corner_flag = input("Input corner flag: ")

    if corner_flag not in ("TOP_LEFT", "TOP_RIGHT", "BOTTOM_RIGHT", "BOTTOM_LEFT"):
        print(
            "Invalid corner flag - has to be one of `(TOP_LEFT, TOP_RIGHT, BOTTOM_RIGHT, BOTTOM_LEFT)`."
        )
        exit(1)

    print(calculate_distance(corner_flag))
