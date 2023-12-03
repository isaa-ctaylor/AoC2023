import aoc_helper as aoc
import re

d = aoc.get_input(2023, 3)

gears = []

lines = d.splitlines()

for lindex, l in enumerate(lines):
    syms = re.finditer(r"\*", l)
    for s in syms:
        pos = (s.start(), lindex)
        gears.append(pos)

total = 0

for s in gears:
    nums = []
    for pos in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        if lines[(y := s[1] + pos[1])][(x := s[0] + pos[0])].isdigit():
            while lines[y][x].isdigit():
                x -= 1
            nums.append((y, x + 1))

    if len((nums := set(nums))) == 2:
        ratio = 1
        for index, n in enumerate(nums):
            num = ""
            x, y = n[0], n[1]
            try:
                while (d := lines[x][y]).isdigit():
                    num += d
                    y += 1
            except IndexError:
                pass

            ratio *= int(num)

        total += ratio

print(total)
