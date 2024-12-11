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

memo = {}

def blink(stones):
    # global memo
    ret = []
    for i in stones:
        x = digitCount(i)
        # x = len(str(i))//2
        # if i in memo:
            # ret+=memo[i]
        if i == 0:
            ret.append(1)
            # memo[i] = [1]
        elif x % 2 == 0:
            power = x // 2
            ret.append(i//powersOf10[power])
            ret.append(i%powersOf10[power])
            # memo[i] = [i//powersOf10[power], i%powersOf10[power]]
        else:
            ret.append(2024*i)
            # memo[i] = [2024*i]
    
    return ret

def blinkelem(stone):
    if stone == 0: return [1]
    x = digitCount(stone)
    if x % 2 == 0:
        power = x // 2
        return [stone//powersOf10[power],stone%powersOf10[power]]
    return [2024*stone]

def partOne():
    x = [int(i) for i in data.split(' ')]
    print(x)
    for _ in range(25):
        x = blink(x)
    return len(x)

from itertools import chain
def partTwo():
    x = [int(i) for i in data.split(' ')]
    for i in range(75):
        x = blink(x)
        if i%10 == 0:
            print(i)
        # x = list(chain.from_iterable(list(map(blinkelem,x))))
    return len(x)

# print(partOne())
print(partTwo())