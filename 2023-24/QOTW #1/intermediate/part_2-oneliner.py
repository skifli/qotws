"""
Relative difficuly: Medium (Luckily didn't take as long as part 1 lol).

NOTE: I did use the method of importing part 1 since that is technically two lines?
"""

# fmt: off

# Python 3.8+ (Walrus Operator)
[numbers := [path := __import__("os").path.split(__file__)[0], lines := [line.rstrip("\n") for line in open(f"{path}/assets/email.txt", "r", encoding="utf-8")][2:], [[temp := line.split(" "), chars := temp[0], to_find := temp[1], temp := to_find, char_1 := temp[0], char_2 := temp[1], char_3 := temp[2], char_1_count := 0, char_2_count := 0, char_3_count := 0, [[char_1_count := char_1_count + (1 if char == char_1 else 0), char_2_count := char_2_count + (1 if char == char_2 else 0), char_3_count := char_3_count + (1 if char == char_3 else 0)] for char in chars], int(f"{char_1_count}{char_2_count}{char_3_count}")][-1] for line in lines]][-1], text := open(f"{path}/assets/How Many.txt", "r", encoding="utf-8").read(), chars := {}, [chars.update({char: (chars[char] + 1) if char in chars else 1}) for char in text], password := [], [password.append(char_and_num[0]) if char_and_num[1] in numbers else "" for char_and_num in chars.items()], print("".join(password))]
