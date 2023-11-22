"""
One-liner in `part_2-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.

with open(f"{path}/../assets/TOP SECRET.txt", "r", encoding="utf-8") as f:
    ascii_text = [byte for line in f.readlines() for byte in line.split(" ")]

DECODED_TEXT = "".join(chr(int(value, 2)) for value in ascii_text)

print(DECODED_TEXT)
