with open(r'adventofcode2024//Day 22//input.txt') as file:
    data = file.readlines()
    
def nextSecretNumberNormal(secret):
    nextNumber = secret
    
    # Multiply secret number by 64, then, mix this into secret number, then prune
    nextNumber ^= (secret * 64)
    nextNumber %= 16777216
    
    # Divide secret number by 32 and round down, then, mix this into secret number, then prune
    nextNumber ^= (nextNumber // 32)
    nextNumber %= 16777216
    
    # Multiply secret number by 2048, then, mix this into secret number, then prune
    nextNumber ^= (nextNumber * 2048)
    nextNumber %= 16777216
    
    return nextNumber

def nextSecretNumberBitwise(secret):
    nextNumber = secret
    
    nextNumber ^= (secret << 6) # secret * 64
    nextNumber &= 16777215
    
    nextNumber ^= (nextNumber >> 5) # secret // 32
    nextNumber &= 16777215
    
    nextNumber ^= (nextNumber << 11) # secret * 2048
    nextNumber &= 16777215 # secret % (2**24)
    
    return nextNumber

def partOne():
    total = 0
    for i in data:
        secret = int(i.strip())
        for _ in range(2000):
            secret = nextSecretNumberBitwise(secret)
        total+=secret
    return total

def generatePrices(initial, steps=2000):
    secret = initial
    prices = []
    for _ in range(steps + 1):  # +1 to calculate changes
        prices.append(secret % 10)  # Extract the last digit
        secret = nextSecretNumberBitwise(secret)
    return prices

def generateChanges(prices):
    changes = []
    for i in range(len(prices)-1):
        changes.append(prices[i+1] - prices[i])
    return changes

def partTwo():
    from collections import defaultdict
    priceChangeMemo = defaultdict(int)

    for i in data:
        buyer = int(i.strip())
        prices = generatePrices(buyer)
        changes = generateChanges(prices)
        found = set()
        for j in range(len(changes)-3):
            index = (changes[j],changes[j+1],changes[j+2],changes[j+3])
            if index in found:
                continue
            priceChangeMemo[index] += prices[j+4]
            found.add(index)
    
    return max(priceChangeMemo.values())

# print(partOne())
# print(partTwo())