"""
Relative difficuly: Eazy squeezy lemon peazy.
"""

# fmt: off

print(sum([open(f"{__import__('os').path.split(__file__)[0]}/../assets/tunnels.txt").read().count(vowel) for vowel in "aeiou"]))
