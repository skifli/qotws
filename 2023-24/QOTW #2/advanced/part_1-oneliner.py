"""
Relative difficuly: Medium (used a completely different approach, but it gives the same answer lol).
"""

# fmt: off

# Python 3.8+ (Walrus Operator Method)
print("Python 3.8+ (Walrus Operator)")

[
    grid := [
        [char for char in line if char != "\n"]
        for line in open(
            f"{__import__('os').path.split(__file__)[0]}/../assets/grid.txt",
            "r",
            encoding="utf-8",
        ).readlines()
    ],
    taxicab_distance := lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2),
    print(
        sum(
            1
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if grid[i][j] == "S"
            and all(
                grid[x2][y2] != "L" or taxicab_distance(i, j, x2, y2) > 5
                for x2 in range(len(grid))
                for y2 in range(len(grid[0]))
            )
        )
    ),
]


# Pre-3.8 (Dict Update Method)
print("\nPre-3.8 (Dict Update Method)")

[
    globals().update({"grid": [
        [char for char in line if char != "\n"]
        for line in open(
            f"{__import__('os').path.split(__file__)[0]}/../assets/grid.txt",
            "r",
            encoding="utf-8",
        ).readlines()
    ]}),
    globals().update({"taxicab_distance": lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)}),
    print(
        sum(
            1
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if grid[i][j] == "S"
            and all(
                grid[x2][y2] != "L" or taxicab_distance(i, j, x2, y2) > 5
                for x2 in range(len(grid))
                for y2 in range(len(grid[0]))
            )
        )
    ),
]
