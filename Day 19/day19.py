with open(r'adventofcode2024//Day 19//input.txt') as file:
    data = file.readlines()
    
availablePatterns = data[0].strip().split(', ')
# print(availablePatterns)

# test input : 
# availablePatterns = 'r, wr, b, g, bwu, rb, gb, br'.split(', ')
# Patterns : 
# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu - impossible
# bwurrg
# brgr
# bbrgwb - impossible

requiredPatterns = [i.strip() for i in data[2:]]
# print(requiredPatterns)

# def possible(pattern):
#     contenders = []
#     if pattern == '':
#         return True
#     for i in availablePatterns:
#         if pattern.startswith(i):
#             contenders.append(pattern[len(i):])
#     if not contenders:
#         return False
#     return True in map(possible,contenders)

# def partOne():
#     count = 0
#     index = 0
#     for i in requiredPatterns:
#         if possible(i):
#             count += 1
#         print(index)
#         index += 1
#     return count

memo = {}

def possible(pattern):
    if pattern in memo:
        return memo[pattern]
    if pattern == '':
        return True
    for towel in availablePatterns:
        if pattern.startswith(towel):
            if possible(pattern[len(towel):]):
                memo[pattern] = True
                return True
    memo[pattern] = False
    return False

def partOne():
    count = 0
    for i, design in enumerate(requiredPatterns):
        if possible(design):
            count += 1
        print(f"Checked design {i + 1}/{len(requiredPatterns)}")
    return count

print(partOne())

def partTwo():
    ...