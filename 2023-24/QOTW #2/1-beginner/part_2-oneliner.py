"""
Relative difficuly: Easy - just copied the code and made it a one-liner.
"""

# fmt: off

[grid := [[char for char in line if char != "\n"] for line in open(f"{__import__('os').path.split(__file__)[0]}/../assets/grid.txt","r",encoding="utf-8",).readlines()], get_adjacent := lambda coords: [[x, y] for y in range(coords[1] - 1, coords[1] + 2) for x in range(coords[0] - 1, coords[0] + 2) if (x != coords[0] or y != coords[1])], check_coord := lambda coord: globals().update({"l_num": l_num + (1 if grid[coord[1]][coord[0]] == "L" else 0)}), coords := [[27, 32], [91, 98], [12, 87], [46, 17]], adjacent_coords := [[coord] + get_adjacent(coord) for coord in coords], [[l_num := 0, [check_coord(coord) if (coord[0] > 0 and coord[0] < len(grid[0]) and coord[1] > 0 and coord[1] < len(grid)) else 0 for coord in adj_coord[1:]], print(f"{adj_coord[0]}: {l_num}")] for adj_coord in adjacent_coords]]
