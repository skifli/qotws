"""
One-liner in `part_1-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.

with open(f"{path}/assets/email.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f][2:]

numbers = []

for line in lines:
    chars, to_find = line.split(" ")
    char_1, char_2, char_3 = to_find
    char_1_count, char_2_count, char_3_count = [0]*3

    for char in chars:
        if char == char_1:
            char_1_count += 1
        elif char == char_2:
            char_2_count += 1
        elif char == char_3:
            char_3_count += 1

    numbers.append(int(f"{char_1_count}{char_2_count}{char_3_count}"))

if __name__ == "__main__":  # if being run directly, since this file is imported in `part_2.py`
    print(numbers)
