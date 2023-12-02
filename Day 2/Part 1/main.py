import aoc_helper as aoc
import re
import dataclasses

d = aoc.get_input(2023, 2)

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

total = 0

for l in d.splitlines():
    game = re.search(r"Game ([\d]+):", l)
    gamen = int(game.group(1))

    sets = l[game.end() + 1 :].split(";")

    allowed = True

    for s in sets:
        if allowed == False:
            continue
        red = re.search(r"(\d+) red", s)
        green = re.search(r"(\d+) green", s)
        blue = re.search(r"(\d+) blue", s)

        if int(red.group(1) if red else 0) > MAX_RED:
            allowed = False
        if int(green.group(1) if green else 0) > MAX_GREEN:
            allowed = False
        if int(blue.group(1) if blue else 0) > MAX_BLUE:
            allowed = False
    
    if allowed: total += gamen

print(total)