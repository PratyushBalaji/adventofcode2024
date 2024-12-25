with open(r'adventofcode2024//Day 25//input.txt') as file:
    data = file.readlines()
    
things = []
currentThing = []
for i in data:
    if i == '\n':
        things.append(currentThing)
        currentThing = []
    else:
        currentThing.append(i.strip())

def heights(thing):
    height = [0]*5
    for i in range(5):
        for j in range(5):
           if thing[1:6][j][i] == '#':
               height[i]+=1
    return height
        
keys = []
locks = []

for thing in things:
    if '#' in thing[0]:
        locks.append(heights(thing))
    else:
        keys.append(heights(thing))
        
# print(locks)
# print(keys)

def fits(lock,key):
    for i in range(5):
        if lock[i] + key[i] > 5:
            return False
    return True

# input file must end with two newlines for the code to work
def partOne():
    count = 0
    for lock in locks:
        for key in keys:
            if fits(lock,key):
                count+=1
                
    return count

print(partOne())