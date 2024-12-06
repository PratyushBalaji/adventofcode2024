with open(r'adventofcode2024\Day 6\input.txt', 'r') as file:
    data = file.readlines()
    
# bounds
boundRight = len(data[0].strip())
boundLeft = 0
boundUp = 0
boundDown = len(data)

# keeps track of locations
obstacles = set()
visitedLocs = set()
    
# current guard position
currPos = (0,0)

orientations = ['up','right','down','left']
currOr = 0
orientation = orientations[currOr%4]

# fill in obstacles
for i in range(len(data)):
    for j in range(len(data[i].strip())):
        if data[i][j] == '#':
            obstacles.add((i,j))
        if data[i][j] == '^':
            visitedLocs.add((i,j))
            currPos = (i,j)

def notInBounds(guard):
    return guard[0] < boundUp or guard[0] >= boundDown or guard[1] < boundLeft or guard[1] >= boundRight

def partOne():
    global data,obstacles,orientation,orientations,currOr,visitedLocs
    currPos = (0,0)
    flag = False
    for i in range(len(data)):
        for j in range(len(data[i].strip())):
            if data[i][j] == '^':
                currPos = (i,j)
                flag = True
                break
        if flag:break
        
    while not notInBounds(currPos):
        nextPos = currPos
        if orientation == 'up':
            nextPos = (currPos[0]-1, currPos[1])
        elif orientation == 'down':
            nextPos = (currPos[0]+1, currPos[1])
        elif orientation == 'left':
            nextPos = (currPos[0], currPos[1]-1)
        elif orientation == 'right':
            nextPos = (currPos[0], currPos[1]+1)
        
        if nextPos in obstacles:
            currOr+=1
            orientation = orientations[currOr%4]
            continue
        
        if not notInBounds(nextPos):
            visitedLocs.add(nextPos)
        
        currPos = nextPos
            
    return len(visitedLocs)

# for i in visitedLocs:
#     data[i[0]] = "".join(list(data[i[0]][:i[1]] + 'X' + data[i[0]][i[1]+1:]))

# for j in data:
#     print(j,end='')
    

def partTwo():
    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    directions = ['up', 'right', 'down', 'left']

    def createsLoop(newObstacle, startPos, startDir, obstacles):
        visitedStates = set()
        currPos = startPos
        currDir = directions.index(startDir)

        while (currPos, currDir) not in visitedStates:
            visitedStates.add((currPos, currDir))
            
            # Calculate next position based on the current direction
            move = moves[directions[currDir]]
            nextPos = (currPos[0] + move[0], currPos[1] + move[1])
            
            # Check if out of bounds
            if notInBounds(nextPos):
                return False  # No loop, the guard leaves the map
            
            # If the next position is an obstacle, turn right
            if nextPos in obstacles or nextPos == newObstacle:
                currDir = (currDir + 1) % 4  # Turn right
            else:
                currPos = nextPos  # Move forward

        return True  # Loop detected

    def findLoopPositions(startPos, startDir, obstacles, bounds):
        loopPositions = set()

        for row in range(bounds[0], bounds[1]):
            for col in range(bounds[2], bounds[3]):
                candidatePos = (row, col)
                
                # Skip if the position is already an obstacle or the starting position
                if candidatePos in obstacles or candidatePos == startPos:
                    continue
                
                # Test if placing an obstacle here causes a loop
                if createsLoop(candidatePos, startPos, startDir, obstacles):
                    loopPositions.add(candidatePos)
        
        return loopPositions

    # Define the bounds of the grid
    bounds = (boundUp, boundDown, boundLeft, boundRight)

    # Find all valid positions that cause a loop
    loopPositions = findLoopPositions(currPos, 'up', obstacles, bounds)

    return len(loopPositions)

print(partOne())
print(partTwo())