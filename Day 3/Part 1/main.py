import aoc_helper as aoc
import re

d = aoc.get_input(2023, 3)

symbols = []
nums = []

lines = d.splitlines()

for lindex, l in enumerate(lines):
    syms = re.finditer(r"[@/+%#*&$=-]", l)
    for s in syms:
        pos = (s.start(), lindex)
        symbols.append(pos)

for s in symbols:
    for pos in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        if lines[(y := s[1] + pos[1])][(x := s[0] + pos[0])].isdigit():
            while lines[y][x].isdigit():
                x -= 1
            nums.append((y, x + 1))

total = 0

for n in set(nums):
    num = ""
    x, y = n[0], n[1]
    try:
        while (d := lines[x][y]).isdigit():
            num += d
            y += 1
    except IndexError:
        pass

    total += int(num)

print(total)
