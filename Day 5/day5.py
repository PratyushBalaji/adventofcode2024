with open(r'adventofcode2024\Day 5\input.txt', 'r') as file:
    data = file.readlines()

rules = {}
updates = []

# setup for problem
# filling in the rules and updates 
setup = True
for line in data:
    if line == '\n': # end of section 1, start of section 2
        setup = False
        continue
    if setup: # section 1
        curr = [int(i) for i in line.strip().split('|')]
        if curr[0] in rules:
            rules[curr[0]].append(curr[1])
        else:
            rules[curr[0]] = [curr[1]]
    else: # section 2
        updates.append([int(i) for i in line.strip().split(',')])
        
        
# is an update valid? 
# helper for part 1
def valid(update):
    global rules
    for i in range(len(update)):
        if update[i] not in rules:
            continue
        for j in rules[update[i]]:
            if j in update[:i]:
                return False
    return True

def partOne():
    global updates
    count = 0
    for i in updates:
        if valid(i):
            count += int(i[len(i)//2])
    return count

# make valid takes an invalid list and returns a valid one
# uses insertion-sort-esque algorithm
# helper for part 2
def makeValid(update):
    global rules
    sortedUpdate = []
    for page in update:
        inserted = False
        for i in range(len(sortedUpdate)):
            if sortedUpdate[i] in rules.get(page, []):
                sortedUpdate.insert(i, page)
                inserted = True
                break
        if not inserted:
            sortedUpdate.append(page)
    return sortedUpdate

def partTwo():
    global updates
    incorrectUpdates = list(filter(lambda x: not valid(x), updates))
    count = 0
    for i in incorrectUpdates:
        count += int(makeValid(i)[len(i)//2])
    return count

# print(partOne())
# print(partTwo())