"""
Relative difficuly: Ez dubs.
"""

# fmt: off

print(open(f"{__import__('os').path.split(__file__)[0]}/assets/grid.txt").read().count("L"))
