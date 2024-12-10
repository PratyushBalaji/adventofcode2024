with open(r'adventofcode2024\Day 10\input.txt', 'r') as file:
    lines = file.readlines()
    data = []
    for i in lines:
        data.append([int(j) for j in i.strip()])
    
    
        
def startTrail(i, j, visited):
    if data[i][j] == 9:
        return {(i, j)}

    if (i, j) in visited:
        return set()

    visited.add((i, j))

    reachableNines = set()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = i + dx, j + dy
        if (
            0 <= nx < len(data) and
            0 <= ny < len(data[0]) and
            data[nx][ny] - data[i][j] == 1 
        ):
            reachableNines |= startTrail(nx, ny, visited)

    return reachableNines


def partOne():
    total_score = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                visited = set()
                total_score += len(startTrail(i, j, visited))
    return total_score

def countDistinctTrails(i, j, visited, path):
    if data[i][j] == 9: 
        path.add(tuple(visited))
        return

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = i + dx, j + dy
        if (
            0 <= nx < len(data) and  
            0 <= ny < len(data[0]) and 
            (nx, ny) not in visited and 
            data[nx][ny] - data[i][j] == 1  
        ):
            visited.add((nx, ny)) 
            countDistinctTrails(nx, ny, visited, path) 
            visited.remove((nx, ny)) 

def partTwo():
    totalRating = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                path = set() 
                visited = {(i, j)} 
                countDistinctTrails(i, j, visited, path)
                totalRating += len(path) 
    return totalRating

# print(partOne())
# print(partTwo())