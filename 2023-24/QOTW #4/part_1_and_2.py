from os.path import split
from typing import Final, Optional

path = split(__file__)[0]  # If terminal cwd is different to program path.
WORDS: Final[str] = ["RCCA", "GCI", "RMC"]

found_words: dict[str, list[list[int]]] = {}
cookies: list[list[int]] = []

for word in WORDS:
    found_words[word] = []


def find_word(line_index: int, char_index: int, word: str, diagonal: bool) -> list[str]:
    found: list[str] = []
    found_indexes: list[list[int]] = []

    # Right

    if char_index + len(word) <= len(ws[line_index]):
        found_indexes = []

        for i, char in enumerate(word):
            if ws[line_index][char_index + i] != char:
                break

            if char == "C":
                cookies.append([line_index, char_index + i])

            found_indexes.append([line_index, char_index + i])
        else:
            found_words[word].append(found_indexes)

            found.append(word)

    # Left

    if char_index - len(word) >= -1:
        found_indexes = []

        for i, char in enumerate(word):
            if ws[line_index][char_index - i] != char:
                break

            if char == "C":
                cookies.append([line_index, char_index - i])

            found_indexes.append([line_index, char_index - i])
        else:
            found_words[word].append(found_indexes)

            found.append(word)

    # Down

    if line_index + len(word) <= len(ws):
        found_indexes = []

        for i, char in enumerate(word):
            if ws[line_index + i][char_index] != char:
                break

            if char == "C":
                cookies.append([line_index + i, char_index])

            found_indexes.append([line_index + i, char_index])
        else:
            found_words[word].append(found_indexes)

            found.append(word)

    # Up

    if line_index - len(word) >= -1:
        found_indexes = []

        for i, char in enumerate(word):
            if ws[line_index - i][char_index] != char:
                break

            if char == "C":
                cookies.append([line_index - i, char_index])

            found_indexes.append([line_index - i, char_index])
        else:
            found_words[word].append(found_indexes)

            found.append(word)

    if diagonal:
        # Down-right

        if line_index + len(word) <= len(ws) and char_index + len(word) <= len(
            ws[line_index]
        ):
            found_indexes = []

            for i, char in enumerate(word):
                if ws[line_index + i][char_index + i] != char:
                    break

                if char == "C":
                    cookies.append([line_index + i, char_index + i])

                found_indexes.append([line_index + i, char_index + i])
            else:
                found_words[word].append(found_indexes)

                found.append(word)

        # Down-left

        if line_index + len(word) <= len(ws) and char_index - len(word) >= -1:
            found_indexes = []

            for i, char in enumerate(word):
                if ws[line_index + i][char_index - i] != char:
                    break

                if char == "C":
                    cookies.append([line_index + i, char_index - i])

                found_indexes.append([line_index + i, char_index - i])
            else:
                found_words[word].append(found_indexes)

                found.append(word)

        # Up-right

        if line_index - len(word) >= -1 and char_index + len(word) <= len(
            ws[line_index]
        ):
            found_indexes = []

            for i, char in enumerate(word):
                if ws[line_index - i][char_index + i] != char:
                    break

                if char == "C":
                    cookies.append([line_index - i, char_index + i])

                found_indexes.append([line_index - i, char_index + i])
            else:
                found_words[word].append(found_indexes)

                found.append(word)

        # Up-left

        if line_index - len(word) >= -1 and char_index - len(word) >= -1:
            found_indexes = []

            for i, char in enumerate(word):
                if ws[line_index - i][char_index - i] != char:
                    break

                if char == "C":
                    cookies.append([line_index - i, char_index - i])

                found_indexes.append([line_index - i, char_index - i])
            else:
                found_words[word].append(found_indexes)

                found.append(word)

    return found


def find_occurences(diagonal: Optional[bool] = False) -> list[str]:
    global found_words, cookies

    found_words = {}
    occurences = []
    cookies = []

    for word in WORDS:
        found_words[word] = []

    number_of_cookies = 0

    for line_index, line in enumerate(ws):
        for char_index, char in enumerate(line):
            for word in WORDS:
                if char[0] == word[0]:
                    matches = find_word(line_index, char_index, word, diagonal)

                    occurences.extend(matches)

    for occurence in occurences:
        number_of_cookies += occurence.count("C")

    return number_of_cookies


def find_cookie_overlapping_all_words() -> list[int]:
    # PART 3: One cookie is the overlap of an instance of all 3 words. What are its 0-indexed (x, y) co-ords?

    for cookie in cookies:
        for _, coords in found_words.items():
            found = False

            for coord_list in coords:
                if cookie in coord_list:
                    found = True

                    break

            if not found:
                break
        else:
            return cookie

    print(found_words)


with open(f"{path}/assets/ws.txt", "r", encoding="utf-8") as f:
    ws = [[char for char in line.strip()] for line in f.readlines()]

print(find_occurences(False))
print(find_occurences(True))

print(find_cookie_overlapping_all_words())
