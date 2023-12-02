import aoc_helper as aoc
import re

d = aoc.get_input(2023, 2)

total = 0

for l in d.splitlines():
    game = re.search(r"Game ([\d]+):", l)
    gamen = int(game.group(1))

    sets = l[game.end() + 1 :].split(";")

    max_red = 0
    max_green = 0
    max_blue = 0

    for s in sets:
        red = re.search(r"(\d+) red", s)
        green = re.search(r"(\d+) green", s)
        blue = re.search(r"(\d+) blue", s)

        if (red := int(red.group(1) if red else 0)) > max_red:
            max_red = red
        if (green := int(green.group(1) if green else 0)) > max_green:
            max_green = green
        if (blue := int(blue.group(1) if blue else 0)) > max_blue:
            max_blue = blue
    
    total += (max_red * max_green * max_blue)

print(total)