"""
One-liner in `part_1-oneliner.py`.
"""

from os.path import split

from itertools import permutations

path = split(__file__)[0]  # If terminal cwd is different to program path.


def is_prime(num: int) -> bool:
    return (
        num > 1
        and (num == 2 or num % 2 != 0)
        and all(num % divisor != 0 for divisor in range(3, int(num**0.5) + 1, 2))
    )


def amount_of_full_length_prime_permutations(limit):
    amount = 0

    for num in range(2, limit):
        if is_prime(num):
            perms = set(
                int("".join(p)) for p in permutations(str(num))
            )  # Get all permutations of the number.

            full_length_primes = [
                p for p in perms if is_prime(p) and len(str(p)) == len(str(num))
            ]  # Get all full-length permutations that are prime.

            if len(full_length_primes) == len(
                perms
            ):  # Check if all permutations are prime.
                amount += len(full_length_primes)

    return amount


wall_numbers = [
    int(num.strip()) for num in input("Enter the wall numbers: ").split(",")
]

print(sum(amount_of_full_length_prime_permutations(num) for num in wall_numbers))
