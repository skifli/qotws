"""
Relative difficuly: Easy - just copied the code and made it a one-liner.
"""

# fmt: off

[grid := [[char for char in line if char != "\n"] for line in open(f"{__import__('os').path.split(__file__)[0]}/../assets/grid.txt","r",encoding="utf-8",).readlines()], taxicab_distance := lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2), max_distance := 0, max_distance_coords := (0, 0), [[[min_distance_to_s := min(taxicab_distance(y, x, x2, y2) for x2 in range(len(grid)) for y2 in range(len(grid[0])) if grid[x2][y2] == "S"), [max_distance := min_distance_to_s, max_distance_coords := (y, x)] if min_distance_to_s > max_distance else 0] if grid[y][x] == "L" else 0 for x in range(len(grid[0]))] for y in range(len(grid))], print(max_distance_coords)]