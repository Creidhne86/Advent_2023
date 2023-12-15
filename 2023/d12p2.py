from functools import cache



input = "d12_input.txt"
#input = "d12_test.txt"

with open(input,"r") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].split()
    data[i][1] = data[i][1].split(",")
    data[i][1] = tuple(int(x) for x in data[i][1])

#print(data)

@cache
def get_combinations(springs, nums, folds = 1):
    springs = '?'.join([springs] * folds)
    nums = nums * folds
    #print(springs, nums)
    total = 0
    
    if len(springs) == 0:
        if len(nums) == 0:
            return 1
        return 0
    
    if len(nums) == 0:
        if "#" in springs:
            return 0
        return 1
    
    if len(springs) < sum(nums) + len(nums) - 1:
        return 0
    
    if springs[0] in ".?":
        total += get_combinations(springs[1:],nums)
    
    n = nums[0]
    if (springs[0] in "#?" and
        "." not in springs[:n] and
        (len(springs) == n or springs[n] in ".?")):
        total += get_combinations(springs[n+1:],nums[1:])

    return total

part1 = 0
for line in data:
    springs, nums = line
    part1 += get_combinations(springs,nums)

part2 = 0
for line in data:
    springs, nums = line
    part2 += get_combinations(springs,nums,5)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")