with open(r'adventofcode2024/Day 11/input.txt') as file:
    data = file.readlines()[0]

from math import log10    
def digitCount(n):
    if n < 10:
        return 1
    if n < 100: return 2
    if n < 1000: return 3
    if n < 10000: return 4
    if n < 100000: return 5
    if n < 1000000: return 6
    if n < 10000000: return 7
    if n < 100000000: return 8
    if n < 1000000000: return 9
    if n < 10000000000: return 10
    else: return int(log10(n))+1

powersOf10 = [10 ** i for i in range(20)]

def blink(stones):
    ret = []
    for i in stones:
        x = digitCount(i)
        # x = len(str(i))//2
        if i == 0:
            ret.append(1)
        elif x % 2 == 0:
            power = x // 2
            ret.append(i//powersOf10[power])
            ret.append(i%powersOf10[power])
        else:
            ret.append(2024*i)
    
    return ret

def blinkelem(stone):
    if stone == 0: return [1]
    x = digitCount(stone)
    if x % 2 == 0:
        power = x // 2
        return [stone//powersOf10[power],stone%powersOf10[power]]
    return [2024*stone]

def partOneUnoptimised():
    x = [int(i) for i in data.split(' ')]
    for _ in range(25): # This implementation was extremely slow for part two
        x = blink(x)
    return len(x)

# optimised function that memoises recursive calls
memo = {}
def numStones(seedStone,blinksLeft):
    newBlinksLeft = blinksLeft - 1
    if (seedStone,blinksLeft) in memo:
        return memo[(seedStone,blinksLeft)]
    if blinksLeft == 0:
        return 1
    if seedStone == '0':
        return numStones('1',newBlinksLeft)
    if len(seedStone) % 2 == 1:
        return numStones(str(int(seedStone)*2024),newBlinksLeft)
    memo[(seedStone,blinksLeft)] = numStones(seedStone[:len(seedStone)//2],newBlinksLeft) + numStones(seedStone[len(seedStone)//2:],newBlinksLeft)
    return memo[(seedStone,blinksLeft)]

def partOneOptimised():
    x = data.split(' ')
    return sum(map(numStones,x,[25]*len(x)))

def partTwo():
    x = data.split(' ')
    return sum(map(numStones,x,[75]*len(x)))

print(partOneOptimised())
print(partTwo())