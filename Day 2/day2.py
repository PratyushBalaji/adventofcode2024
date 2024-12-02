with open(r'adventofcode2024\Day 2\input.txt', 'r') as file:
    lines = file.readlines()
    
def isSafe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    increasing = True
    decreasing = True
    for i in differences:
        if i <= 0 or i > 3:
            increasing = False
        if i < -3 or i>=0:
            decreasing = False
    return increasing or decreasing

def partOne():
    safe_count = 0
    for line in lines:
        report = list(map(int, line.split()))
        if isSafe(report):
            safe_count += 1

    return safe_count

def partTwo():
    safeCount = 0
    for line in lines:
        report = list(map(int, line.split()))
        safes = []
        for i in range(len(report)):
            safes.append(isSafe(report[:i]+report[i+1:]))
        if True in safes:
            safeCount += 1
    return safeCount
    
print(partOne())
print(partTwo())