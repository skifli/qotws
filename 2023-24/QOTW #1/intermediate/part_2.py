"""
One-liner in `part_2-oneliner.py`.
"""

from part_1 import path, numbers

with open(f"{path}/assets/How Many.txt", "r", encoding="utf-8") as f:
    text = f.read()

chars = {}

for char in text:
    if char not in chars:
        chars[char] = 1
    else:
        chars[char] += 1

password = []

for char_and_num in chars.items():
    if char_and_num[1] in numbers:
        password.append(char_and_num[0])

print("".join(password))
