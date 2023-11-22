"""
Requirements for challenge stated this must be a one-liner.
"""

# fmt: off

merge_sort = lambda array: array if len(array) <= 1 else None if (l := merge_sort(array[:len(array) // 2])) and (r := merge_sort(array[len(array) // 2:])) and False else [l.pop(0) if l and r and l[0] <= r[0] else (r.pop(0) if r else l.pop(0)) for _ in range(len(array))]

print(merge_sort([
    int(num.strip()) for num in input("Enter the numbers: ").split(",")
]))
