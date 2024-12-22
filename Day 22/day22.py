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
    nextNumber %= 16777216
    
    nextNumber ^= (nextNumber >> 5) # secret // 32
    nextNumber %= 16777216
    
    nextNumber ^= (nextNumber << 11) # secret * 2048
    nextNumber %= 16777216 # secret % (2**24)
    
    return nextNumber

def partOne():
    total = 0
    for i in data:
        secret = int(i.strip())
        for _ in range(2000):
            secret = nextSecretNumberBitwise(secret)
        total+=secret
    return total

print(partOne())