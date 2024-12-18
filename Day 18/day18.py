from collections import deque

with open(r'adventofcode2024//Day 18//input.txt') as file:
    data = file.readlines()
    
firstKB = data[:1024]

# memory has coordinates from 0 to 70 and is 2D square grid
RAM = [['.' for _ in range(71)] for _ in range(71)]
        
start = (0,0)
finish = (70,70)

def shortestPathBFS(start, finish, grid): # breadth first search using deque to find length of shortest path
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == finish:
            return steps
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and (nx, ny) not in visited and grid[ny][nx] != '#':
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    
    return -1 # return -1 if no path found (Useful in Part 2)

# run once for first kilobyte
def partOne():
    grid = [i[:] for i in RAM] # rereference to not overwrite global
    for i in firstKB:
        x,y = map(int,i.strip().split(','))
        grid[y][x] = '#'
    return shortestPathBFS(start, finish, grid)

# run from start and check while path exists
def partTwo():
    grid = [i[:] for i in RAM] # rereference to not overwrite global
    shortestPath = 0
    currLine = -1
    while shortestPath != -1:
        currLine += 1
        x,y = map(int,data[currLine].strip().split(','))
        grid[y][x] = '#'
        shortestPath = shortestPathBFS(start, finish, grid)
    return data[currLine].strip()

# print(partOne())
# print(partTwo())