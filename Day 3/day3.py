import re

with open(r'adventofcode2024\Day 3\input.txt', 'r') as file:
    data = file.read()
    
def partOne():
    valid = []
    
    # using list splitting
    muls = data.split('mul(')
    muls = list(map(lambda x: x[:x.index(')')],filter(lambda x: ')' in x and ',' in x,muls)))
    for j in muls:
        i = j.split(',')
        if isValidInt(i[0]) and isValidInt(i[1]):
            valid.append(int(i[0])*int(i[1]))
    return sum(valid)
        
def isValidInt(num):
    numbers = set([str(i) for i in range(10)])
    for i in num:
        if not i in numbers:
            return False
    return True

def partTwo():
    enabled = True
    total = 0
    
    # using regex instead since we have to deal with multiple patters
    instructions = re.finditer(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))', data)
    # if data looks like "do()" or "don't()" or "mul(int,int)" add it to instructions as a regex obj

    for match in instructions:
        instruction = match.group() # instruction is the string form of the regex obj
        
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:
            if enabled:
                x = int(match.group(2))
                y = int(match.group(3))
                total += x * y
    
    return total
        
print(partTwo())