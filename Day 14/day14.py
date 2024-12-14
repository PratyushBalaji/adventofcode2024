with open(r'adventofcode2024/Day 14/input.txt') as file:
    data = file.readlines()
    
robots = []
for line in data:
    robot = line.strip()[2:].split(' v=')
    startPos = list(map(int, robot[0].split(',')))
    velocity = list(map(int, robot[1].split(',')))
    robots.append((startPos, velocity))

width = 101
height = 103
quadCount = [0, 0, 0, 0] 

def findQuad(position):
    if position[0] < width // 2:
        if position[1] < height // 2:
            return 0
        elif position[1] > height // 2:
            return 2
    elif position[0] > width // 2:
        if position[1] < height // 2:
            return 1
        elif position[1] > height // 2:
            return 3
    return 4

def partOne():
    for robot in robots:
        finalX = (robot[0][0] + robot[1][0] * 100) % width
        finalY = (robot[0][1] + robot[1][1] * 100) % height
        quad = findQuad((finalX, finalY))
        if quad != 4:
            quadCount[quad] += 1
    return quadCount[0] * quadCount[1] * quadCount[2] * quadCount[3]

# print(partOne())

import os, time
def partTwo():
    def tick(robots, seconds):
        newPositions = []
        for robot in robots:
            startPos, velocity = robot
            newX = (startPos[0] + velocity[0] * seconds) % width
            newY = (startPos[1] + velocity[1] * seconds) % height
            newPositions.append((newX, newY))
        return newPositions

    def visualize(positions):
        grid = [['.' for _ in range(width)] for _ in range(height)]
        for x, y in positions:
            grid[y][x] = '█'
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in grid:
            # if row.count('█') >= 31:
            #     input()
            print("".join(row))
            
    def simulateRobots():
        # seconds = 7037 # My answer was close to 7000, so after I missed it the first time i jumped the seconds to find it
        seconds = 0
        while True:
            positions = tick(robots,seconds)
            visualize(positions)
            print(f"Seconds elapsed: {seconds}")
            input("Press Enter to tick (or Ctrl+C to exit)...")
            # time.sleep(0.05)
            seconds += 1

    simulateRobots()
    
partTwo()

# For part two :
# Uncomment the lines in visualise that check if the count is >= 31
# Comment the lines in simulate for input and uncomment the time.sleep line
# This will go through every single tick for a while until it finds the tree's frame. 
# At which point it will break for a user input indicating there are many robots potentially forming the tree pattern

# Tree in my input : 
'''
....█.........................................................................................█......
.....................................................................................................
.....................................█..............█......................█.........................
...................................█...........█.....................................................
........█......................................█.......................█.............................
.....................█...............................................................................
.....................................................................█...█........█..................
................................█....................................................................
...................................................................█.................................
.....................................................................................................
...............█.......................................█.............................................
....................█................................................................................
....█...........................................█....................................................
..█..............................█...................................................................
.................█...................................................................................
...................█...........█........................................................█............
...........█...........█.......................█.....................................................
........█.......................................................................█.█..................
.....................................................................................................
.....................................................................................................
.....................................................................................................
................█....................................................................................
.....................███████████████████████████████.................................................
.....................█.............................█.................................................
............█........█.............................█................................█................
................█....█.............................█.................................................
...........█.........█.............................█.........................█.......................
.....................█..............█..............█..█......................................█.......
.....................█.............███.............█.................................................
.....................█............█████............█............█....................................
.....................█...........███████...........█.................................................
.....................█..........█████████..........█.................................................
.............█.......█............█████............█................█................................
.....................█...........███████...........█.................................................
.....................█..........█████████..........█.......................................█.........
.............█.......█.........███████████.........█........█........................................
.....................█........█████████████........█..............................................█..
.....................█..........█████████..........█...........█...█.....█...........................
.....................█.........███████████.........█.........................█.......................
.....................█........█████████████........█.................................................
............█........█.......███████████████.......█.................................................
...█..............█..█......█████████████████......█..............█..........█........█............█.
...................█.█........█████████████........█.................................................
.....................█.......███████████████.......█......█...............................█..........
............█........█......█████████████████......█.................................................
.....................█.....███████████████████.....█.................................................
.....................█....█████████████████████....█.................................................
.....................█.............███.............█.................................................
.....................█.............███.............█.................................................
█....................█.............███.............█.................................................
.....................█.............................█..█..............................................
.....................█.............................█.............................█...................
.....................█.............................█.........................█.......█...............
....█......█.........█.............................█.................................................
.....................███████████████████████████████........█...............█........................
.....................................................................................................
.....................................................................................................
..........█........................................................................█.................
....█.......................................................................................█........
...............................█.....................................................................
....█..................................................█..................................█..........
.....................................................................................................
.........................................................................█...........................
..................█.█.................................█......█.......................................
......................█...................█..........................................................
.....................................................................................................
.....................................................................................................
........................................█.......................................................█....
.........................█..................................................█.......█................
.................................................█...................................................
.....................................................................................................
......█..............................█...............................................................
........................................................█.................................█..........
..........█...............................................................█..........................
..................................................................█..................................
█.............................................█......................................................
...................................................██................................................
................................................................................................█....
.....................................................................................................
................................................█.█..................................................
.................................................█...................................................
........................................................█...................█.................█......
......................█....................................................█.........................
........█............................................................................................
...........................................................█.........................................
....█....................................................................................█...........
...............................█...........█.........................................................
...............█..........█...█..........................█...........................................
'''