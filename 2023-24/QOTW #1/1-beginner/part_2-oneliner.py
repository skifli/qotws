"""
Relative difficuly: Easyish.
"""

# fmt: off

# Python 3.8+ (Walrus Operator Method)
print("Python 3.8+ (Walrus Operator)")

[path := __import__("os").path.split(__file__)[0], print(''.join(chr(int(value, 2)) for value in [byte for line in open(f"{path}/../assets/TOP SECRET.txt", "r", encoding="utf-8").readlines() for byte in line.split(" ")]))]

# Pre-3.8 (Dict Update Method)
print("\nPre-3.8 (Dict Update Method)")

[globals().update({"path": __import__("os").path.split(__file__)[0]}), print(''.join(chr(int(value, 2)) for value in [byte for line in open(f"{path}/../assets/TOP SECRET.txt", "r", encoding="utf-8").readlines() for byte in line.split(" ")]))]
