"""
One-liner in `part_1-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.

with open(f"{path}/../assets/tunnels.txt", "r", encoding="utf-8") as f:
    tunnels = f.read()

print(sum([tunnels.count(vowel) for vowel in "aeiou"]))
