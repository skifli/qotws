"""
Relative difficuly: Easy - just copied the code and made it a one-liner.
"""

# fmt: off

[grid := [[char for char in line if char != "\n"] for line in open(f"{__import__('os').path.split(__file__)[0]}/../assets/grid.txt","r",encoding="utf-8",).readlines()], calculate_distance := lambda corner_flag: [index := ((0, 0) if corner_flag == "TOP_LEFT" else (0, len(grid[0]) - 1) if corner_flag == "TOP_RIGHT" else (len(grid) - 1, len(grid[0]) - 1) if corner_flag == "BOTTOM_RIGHT" else (len(grid) - 1, 0)), l_indexes := [], [[l_indexes.append((y_index, x_index)) if (grid[y_index][x_index] == "L") else 0 for x_index in range(len(grid[y_index]))] for y_index in range(len(grid))], l_indexes_distances := [], [l_indexes_distances.append((l_index[0] - 0 if "LEFT" in corner_flag else len(grid) - 1 - l_index[0]) + (l_index[1] - 0 if "TOP" in corner_flag else len(grid[0]) - 1 - l_index[1])) for l_index in l_indexes], sorted(l_indexes_distances)[0]][-1], print(sum([calculate_distance(corner_flag) for corner_flag in ("TOP_LEFT", "TOP_RIGHT", "BOTTOM_RIGHT", "BOTTOM_LEFT")]))]
