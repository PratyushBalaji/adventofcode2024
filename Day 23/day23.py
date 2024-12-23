with open(r'adventofcode2024//Day 23//input.txt') as file:
    data = file.readlines()
    
from collections import defaultdict

graph = defaultdict(set)
for line in data:
    a, b = line.strip().split("-")
    graph[a].add(b)
    graph[b].add(a)

def findTriangles(graph):
    triangles = set()
    for node in graph:
        for neighbor1 in graph[node]:
            for neighbor2 in graph[neighbor1]:
                if neighbor2 in graph[node] and node < neighbor1 < neighbor2:
                    triangles.add(tuple(sorted([node, neighbor1, neighbor2])))
    return triangles

def filterTriangles(triangles):
    filtered = [triangle for triangle in triangles if any(node.startswith("t") for node in triangle)]
    return filtered

def partOne():
    triangles = findTriangles(graph)
    filtered_triangles = filterTriangles(triangles)
    return len(filtered_triangles)

print(partOne())