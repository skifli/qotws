"""
Relative difficuly: Medium (I did spend way too long on this due to a stupid error because of not including brackets though).
"""

# fmt: off

# Python 3.8+ (Walrus Operator)
print("Python 3.8+ (Walrus Operator)")

[path := __import__("os").path.split(__file__)[0], lines := [line.rstrip("\n") for line in open(f"{path}/assets/email.txt", "r", encoding="utf-8")][2:], [print([temp :=line.split(" "), chars := temp[0], to_find := temp[1], temp := to_find, char_1 := temp[0], char_2 := temp[1], char_3 := temp[2], char_1_count := 0, char_2_count := 0,char_3_count := 0, [[char_1_count := char_1_count + (1 if char == char_1 else 0), char_2_count := char_2_count + (1 if char == char_2 else 0), char_3_count := char_3_count + (1 if char == char_3 else 0)] for char in chars], f"{char_1_count}{char_2_count}{char_3_count}"][-1]) for line in lines]]

# Pre-3.8 (Dict Update Method)
print("\nPre-3.8 (Dict Update Method)")

[globals().update({"path": __import__("os").path.split(__file__)[0]}), globals().update({"lines": [line.rstrip("\n") for line in open(f"{path}/assets/email.txt", "r", encoding="utf-8")][2:]}), [print([globals().update({"temp": line.split(" ")}), globals().update({"chars": temp[0]}), globals().update({"to_find": temp[1]}), globals().update({"temp": to_find}),globals().update({"char_1": temp[0]}), globals().update({"char_2": temp[1]}), globals().update({"char_3": temp[2]}), globals().update({"char_1_count": 0}), globals().update({"char_2_count": 0}),globals().update({"char_3_count": 0}), [[globals().update({"char_1_count": char_1_count + (1 if char == char_1 else 0)}), globals().update({"char_2_count": char_2_count + (1 if char == char_2 else 0)}), globals().update({"char_3_count": char_3_count + (1 if char == char_3 else 0)})] for char in chars], f"{char_1_count}{char_2_count}{char_3_count}"][-1]) for line in lines]]
