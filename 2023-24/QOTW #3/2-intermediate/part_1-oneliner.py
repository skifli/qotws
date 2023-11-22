"""
Relative difficuly: Easy.
"""

# fmt: off

[parsed_map := [[char for char in line.strip()] for line in open(f"{__import__('os').path.split(__file__)[0]}/../assets/map.txt", "r", encoding="utf-8") .readlines()], f_function := lambda x, y: sum([int(parsed_map[y + dy][x + dx]) for dy in range(-1, 2) for dx in range(-1, 2)]), print(f"f(f(1, 1), f(98, 98)): {f_function(f_function(1, 1), f_function(98, 98))}")]
