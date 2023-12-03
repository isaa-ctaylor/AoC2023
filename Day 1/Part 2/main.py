import regex as re
import aoc_helper as aoc

d = aoc.get_input(2023, 1)

numd = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def find_word_numbers(l: str):
    return [m if m in "123456789" else numd[m] for m in re.findall(r"(one|two|three|four|five|six|seven|eight|nine|\d)", l, overlapped=True)]

total = 0
for l in d.splitlines():
    nums = find_word_numbers(l)

    total += int(f"{nums[0]}{nums[-1]}")

print(total)
