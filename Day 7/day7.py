with open(r'adventofcode2024\Day 7\input.txt', 'r') as file:
    data = file.readlines()

pairs = []
for i in data:
    temp = i.strip().split(': ')
    nums = [int(i) for i in temp[1].split(' ')]
    pairs.append((int(temp[0]), nums))

def possibleP1(arr,goal):
    if len(arr) == 2:
        return arr[0]+arr[1] == goal or arr[0]*arr[1] == goal
    
    return possibleP1([sum(arr[:2])]+arr[2:],goal) or possibleP1([arr[0]*arr[1]]+arr[2:],goal)

def partOne():
    global pairs
    validPairs = list(filter(lambda x: possibleP1(x[1],x[0]), pairs))
    return sum(i[0] for i in validPairs)

def concat(num1,num2):
    return int(str(num1)+str(num2))

def possibleP2(arr,goal):
    if len(arr) == 2:
        return arr[0]+arr[1] == goal or arr[0]*arr[1] == goal or concat(arr[0],arr[1]) == goal
    
    return possibleP2([sum(arr[:2])]+arr[2:],goal) or possibleP2([arr[0]*arr[1]]+arr[2:],goal) or possibleP2([concat(arr[0],arr[1])]+arr[2:],goal)

def partTwo():
    global pairs
    validPairs = list(filter(lambda x: possibleP2(x[1],x[0]), pairs))
    return sum(i[0] for i in validPairs)

print(partOne())
print(partTwo())