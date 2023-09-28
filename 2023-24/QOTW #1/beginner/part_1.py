"""
One-liner in `part_1-oneliner.py`.
"""

ascii_text = input("Enter the ASCII: ").split(" ")
DECODED_TEXT = ''.join(chr(int(value, 2)) for value in ascii_text)

print(DECODED_TEXT)
