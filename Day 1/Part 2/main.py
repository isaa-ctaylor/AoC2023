with open("input.txt", "r") as f:
    d = f.read()

numd = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def replace_first_word_num(l: str):
    nums = [0 for _ in range(10)]
    
    for index, k in enumerate(numd.keys()):
        nums[index] = l.find(k)
    
    lowest = (None, len(l))
    for index, i in enumerate(nums):
        if i >= 0 and i < lowest[1]:
            lowest = (index, i)
            
    if lowest[0] == None:
        print(l)
        return l
            
    return l.replace(list(numd.keys())[lowest[0]], list(numd.values())[lowest[0]], 1)

total = 0
for l in d.splitlines():
    print(l)
    before = l
    
    while True:
        l = replace_first_word_num(l)
        if l == before:
            break
        before = l
    
    nums = list(filter(lambda i: i in "1234567890", l))
    print(int(f"{nums[0]}{nums[-1]}"))
    total += int(f"{nums[0]}{nums[-1]}")

print(total)
