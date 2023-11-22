"""
One-liner in `part_2-oneliner.py`.
"""

from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.

with open(f"{path}/../assets/numbers.txt", "r", encoding="utf-8") as f:
    numbers = f.read()

char_index = 0
multiplier = 0

char_sum = 0

while True:
    char = numbers[char_index]

    if char == "[":
        multiplier += 1
    elif char == "]":
        multiplier -= 1
    elif char.isdigit():
        number_str = [char]

        while True:
            char_index += 1

            if char_index >= len(numbers):
                break

            char = numbers[char_index]

            if char.isdigit():
                number_str.append(char)
            else:
                char_index -= 1
                break

        char_sum += int("".join(number_str)) * multiplier

    char_index += 1

    if char_index >= len(numbers):
        break

print(char_sum)
