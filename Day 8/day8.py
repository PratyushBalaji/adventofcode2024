with open(r'adventofcode2024\Day 8\input.txt', 'r') as file:
    data = file.readlines()
    
everyPoint = []
everyAntenna = []
for i in range(len(data)):
    for j in range(len(data[i].strip())):
        everyPoint.append((i,j))
        if data[i][j] != '.':
            everyAntenna.append([data[i][j],(i,j)])
            
def distance_squared(p1, p2):
    """Calculate squared Euclidean distance to avoid floating-point errors."""
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def are_collinear(p1, p2, p3):
    """Check if three points are collinear using cross product."""
    return (p2[1] - p1[1]) * (p3[0] - p1[0]) == (p3[1] - p1[1]) * (p2[0] - p1[0])

def partOne():
    uniqueAntinodes = set()

    # Check every point on the grid
    for point in everyPoint:
        # Group antennas by frequency
        freq_map = {}
        for freq, pos in everyAntenna:
            if freq not in freq_map:
                freq_map[freq] = []
            freq_map[freq].append(pos)

        # For each frequency group, check antenna pairs
        for freq, positions in freq_map.items():
            n = len(positions)
            for i in range(n):
                for j in range(i + 1, n):
                    a1, a2 = positions[i], positions[j]

                    # Check if the point is collinear with a1 and a2
                    if are_collinear(a1, a2, point):
                        # Calculate distances
                        d1 = distance_squared(point, a1)
                        d2 = distance_squared(point, a2)

                        # Check the "twice as far" condition
                        if d1 == 2 * d2 or d2 == 2 * d1:
                            uniqueAntinodes.add(point)

    return len(uniqueAntinodes)

    
def partTwo():
    ...
    
print(partOne())
# print(partTwo())