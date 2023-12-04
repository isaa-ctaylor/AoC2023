import aoc_helper as aoc
import math
import re

d = aoc.get_input(2023, 4)

total = 0

NUMBERS = re.compile(r"\d+")

for l in d.splitlines():
    nums = l.split(":")[-1].strip()
    winners, actual = [s.strip() for s in nums.split("|")]

    total += math.floor(2**(len(set(NUMBERS.findall(winners)).intersection(set(NUMBERS.findall(actual))))-1))

print(total)