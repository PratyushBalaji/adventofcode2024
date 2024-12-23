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

memo2 = {}
def possibilities(pattern):
    if pattern in memo2:
        return memo2[pattern]
    
    if pattern == '':
        return 1
    
    ways = 0
    for towel in availablePatterns:
        if pattern.startswith(towel):
            ways += possibilities(pattern[len(towel):])
    
    memo2[pattern] = ways
    return ways

def partTwo():
    totalWays = 0
    for design in requiredPatterns:
        totalWays += possibilities(design)
    return totalWays
    
# print(partOne())
# print(partTwo())