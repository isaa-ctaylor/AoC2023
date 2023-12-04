import aoc_helper as aoc
import math
import re
import collections

d = aoc.get_input(2023, 4)

NUMBERS = re.compile(r"\d+")

cards = collections.Counter([i for i in range(1, len(d.splitlines()) + 1)])

for l in d.splitlines():
    gamen = int(re.search(r"Card +([\d]+):", l).group(1))
    nums = l.split(":")[-1].strip()
    winners, actual = [s.strip() for s in nums.split("|")]

    win = len(set(NUMBERS.findall(winners)).intersection(set(NUMBERS.findall(actual))))
    for _ in range(cards[gamen]):
        for i in range(win):
            cards[i+gamen+1] += 1
            
print(cards.total())
