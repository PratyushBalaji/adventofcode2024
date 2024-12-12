with open(r'adventofcode2024/Day 12/input.txt') as file:
    data = [list(line.strip()) for line in file.readlines()]

def findRegions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def floodFill(r, c, plant_type):
        stack = [(r, c)]
        regionCells = []
        perimeter = 0
        
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            regionCells.append((x, y))
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == plant_type and not visited[nx][ny]:
                        stack.append((nx, ny))
                    elif grid[nx][ny] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1
        
        return len(regionCells), perimeter

    regions = []
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perimeter = floodFill(r, c, grid[r][c])
                regions.append((area, perimeter))
    return regions

def totalCost(regions):
    return sum(area * perimeter for area, perimeter in regions)

def partOne():
    grid = data
    regions = findRegions(grid)
    return totalCost(regions)

# print(partOne())