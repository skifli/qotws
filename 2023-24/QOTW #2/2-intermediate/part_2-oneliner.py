"""
Relative difficuly: Easy - just copied the code and made it a one-liner.
"""

# fmt: off

[grid := [[char for char in line if char != "\n"] for line in open(f"{__import__('os').path.split(__file__)[0]}/../assets/grid.txt","r",encoding="utf-8",).readlines()], get_adjacent := lambda coords: [[x, y] for y in range(coords[1] - 1, coords[1] + 2) for x in range(coords[0] - 1, coords[0] + 2) if not ((x == coords[0] and y == coords[1]) or (x == coords[0] - 1 and y == coords[1] - 1) or (x == coords[0] - 1 and y == coords[1] + 1) or (x == coords[0] + 1 and y == coords[1] - 1) or (x == coords[0] + 1 and y == coords[1] + 1))],check_coord := lambda coord: (coord[0] > 0 and coord[0] < len(grid[0]) and coord[1] > 0 and coord[1] < len(grid)), coords := [[x, y] for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "L"], l_which_dont_border_s := 0, [[adjacent_coords := get_adjacent(coord), failed := False, [[failed := True if grid[coord[1]][coord[0]] == "S" else failed] if check_coord(coord) else 0 for coord in adjacent_coords], l_which_dont_border_s := l_which_dont_border_s + (1 if not failed else 0)] for coord in coords], print(l_which_dont_border_s)]
