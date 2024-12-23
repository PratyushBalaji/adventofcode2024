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
    filteredTriangles = filterTriangles(triangles)
    return len(filteredTriangles)

# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X: # if P and X are both empty then
        cliques.append(R) # report R as a maximal clique
        return
    for v in list(P): # for each vertex v in P do
        bron_kerbosch(
            R.union({v}), # R = R ⋃ {v}
            P.intersection(graph[v]), # P = P ⋂ N(v)
            X.intersection(graph[v]), # X = X ⋂ N(v)
            graph,
            cliques)
        P.remove(v) # P := P \ {v}
        X.add(v) # X := X ⋃ {v}

def findLargestClique(graph):
    cliques = []
    nodes = set(graph.keys())
    bron_kerbosch(set(), nodes, set(), graph, cliques)

    largestClique = max(cliques, key=len)
    return largestClique

def partTwo():
    largestClique = findLargestClique(graph)
    password = ",".join(sorted(largestClique))
    return password

# print(partOne())
# print(partTwo())