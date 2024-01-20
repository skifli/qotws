from os.path import split

path = split(__file__)[0]  # If terminal cwd is different to program path.


def do_the_process(num: str) -> str:
    prev_chr = ""
    chr_count = 0

    num_runs = []

    for char in num:
        if char == prev_chr:
            chr_count += 1
        else:
            if prev_chr != "":
                num_runs.append([chr_count, prev_chr])

            chr_count = 1

        prev_chr = char

    num_runs.append([chr_count, num[-1]])

    return "".join([f"{count}{char}" for count, char in num_runs])


def part_1() -> str:
    lengths = 0

    for num in numbers[:5]:
        for _ in range(20):
            num = do_the_process(num)

        lengths += len(num)

    return lengths


def part_2() -> str:
    num = numbers[5]
    lengths = []  # count then char

    for char in range(0, len(num), 2):
        lengths.append([num[char], num[char + 1]])

    total_lengths = {}

    for length in lengths:
        if length[-1] not in total_lengths:
            total_lengths[length[-1]] = 0

        total_lengths[length[-1]] += int(length[0])

    total_lengths_sorted = []

    for key in total_lengths:
        total_lengths_sorted.append([total_lengths[key], key])

    total_lengths_sorted.sort(reverse=True)

    return total_lengths_sorted


def part_3() -> str:
    SPECIAL_STR = "11131221131211221321123113213221121321132132211411131221131211132221121113122113121113222114132112111312111213322113"

    for num in numbers[:5]:
        original_num = num

        for _ in range(20):
            num = do_the_process(num)

            if num == SPECIAL_STR:
                return original_num


with open(f"{path}/assets/numbers.txt", "r") as f:
    numbers = [line.strip() for line in f.readlines()]

print(part_1())
print(part_2())
print(part_3())
