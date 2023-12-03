import aoc_helper as aoc

d = aoc.get_input(2023, 1)
    
total = 0
    
for l in d.splitlines():
    nums = list(filter(lambda i: i in '1234567890', l))
    total += int(f"{nums[0]}{nums[-1]}")
    
print(total)