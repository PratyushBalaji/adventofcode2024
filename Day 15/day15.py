with open(r'adventofcode2024/Day 15/input.txt') as file:
    data = file.readlines()


# Split into grid and move sequence
grid = [list(line.strip()) for line in data if line.startswith('#')]
moves = "".join(line.strip() for line in data if not line.startswith('#'))

def findRobotAndBoxes(grid):
    robot = None
    boxes = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == '@':
                robot = (r, c)
            elif val == 'O':
                boxes.add((r, c))
    return robot, boxes

def isValidMove(pos, grid, boxes):
    r, c = pos
    return grid[r][c] != '#' and pos not in boxes

def moveRobotAndBoxes(grid, moves):
    robot, boxes = findRobotAndBoxes(grid)
    directions = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

    for move in moves:
        dr, dc = directions[move]
        newRobotPos = (robot[0] + dr, robot[1] + dc)

        if newRobotPos in boxes:
            chain = [newRobotPos]
            while True:
                nextPos = (chain[-1][0] + dr, chain[-1][1] + dc)
                if nextPos in boxes:  # add to chain
                    chain.append(nextPos)
                elif grid[nextPos[0]][nextPos[1]] == '#' or nextPos in boxes:
                    # Blocked by a wall or another box; invalid move
                    chain = None
                    break
                else:
                    # not in boxes, not border => valid
                    break
            
            if chain:  # If push is valid, move all boxes in chain
                # remove in reverse order so push doesnt clash
                for pos in reversed(chain):
                    boxes.remove(pos)
                    nextPos = (pos[0] + dr, pos[1] + dc)
                    boxes.add(nextPos)
                robot = newRobotPos
        elif isValidMove(newRobotPos, grid, boxes):
            # Move robot only
            robot = newRobotPos
        else:
            continue  # Invalid move, robot stays in place

    return boxes

def calculateGPS(boxes):
    return sum(100 * r + c for r, c in boxes)

def partOne():
    boxes = moveRobotAndBoxes(grid, moves)
    return calculateGPS(boxes)

def partTwo():
    ...

# print(partOne())
# print(partTwo())