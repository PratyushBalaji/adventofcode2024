with open(r'adventofcode2024\Day 4\input.txt', 'r') as file:
    data = file.readlines()

def partOne():
    lines = [list(i.strip()) for i in data]
    
    count = 0
    
    # horizontal
    for i in lines:
        for j in range(len(i) - 3):
            if "".join(i[j:j+4]) in {'XMAS','SAMX'}:
                count += 1
    
    # vertical
    for i in range(len(lines) - 3):
        for j in range(len(lines[i])):
            if lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j] in {'XMAS','SAMX'}:
                count += 1
    
    # positive diagonal
    for i in range(len(lines) - 3):
        for j in range(len(lines[i]) - 3):
            if lines[i+3][j] + lines[i+2][j+1] + lines[i+1][j+2] + lines[i][j+3] in {'XMAS','SAMX'}:
                count += 1
    
    # negative diagonal
    for i in range(len(lines) - 3):
        for j in range(len(lines[i]) - 3):
            if lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] in {'XMAS','SAMX'}:
                count += 1
    
    return count

def partTwo():
    lines = [list(i.strip()) for i in data]
    count = 0
    
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            if ((lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1] in {"MAS", "SAM"}) and
                (lines[i+1][j-1] + lines[i][j] + lines[i-1][j+1] in {"MAS", "SAM"})):
                count += 1
    
    return count

# print(partOne())
# print(partTwo())