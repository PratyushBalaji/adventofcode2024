import heapq

with open(r'adventofcode2024/Day 16/input.txt') as file:
    data = file.readlines()

# directions and their corresponding moves
directions = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}
turns = {
    'E': {'CW': 'S', 'CCW': 'N'},
    'S': {'CW': 'W', 'CCW': 'E'},
    'W': {'CW': 'N', 'CCW': 'S'},
    'N': {'CW': 'E', 'CCW': 'W'}
}

obstacles = set()
visited = {}  # visited state: (row, col, direction) -> best score
start, finish = (0, 0), (0, 0)

# parse grid
for r, row in enumerate(data):
    for c, val in enumerate(row.strip()):
        if val == '#':
            obstacles.add((r, c))
        elif val == 'E':
            finish = (r, c)
        elif val == 'S':
            start = (r, c)
            currPos = (r,c)

def isValid(pos):
    return pos not in obstacles

def partOne():
    # maze solved using breadth first search
    # priority queue for minimum scoring
    # sorry if this is inefficient / whatever, im not very familiar with heaps, any feedback appreciated
    
    pq = []  # priority queue: (score, row, col, direction)
    heapq.heappush(pq, (0, start[0], start[1], 'E'))  # Start facing East
    visited = {}

    while pq:
        score, row, col, direction = heapq.heappop(pq)
        
        if (row, col) == finish:
            return score
        
        # skip if we've already visited this state with a better / equal score
        state = (row, col, direction)
        if state in visited and visited[state] <= score:
            continue
        visited[state] = score
        
        # option 1: continue in same direction
        dr, dc = directions[direction]
        new_row, new_col = row + dr, col + dc
        if isValid((new_row, new_col)):
            heapq.heappush(pq, (score + 1, new_row, new_col, direction))
        
        # option 2: turn 90 degrees
        for turn, new_direction in turns[direction].items():
            heapq.heappush(pq, (score + 1000, row, col, new_direction))
    return float('inf')  # infinity if path doesnt reach finish so this path is definitely at end of queue

print(partOne())