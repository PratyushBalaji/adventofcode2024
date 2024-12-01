left_numbers = []
right_numbers = []

# input data
with open(r'adventofcode2024\Day 1\input.txt', 'r') as file:
    for line in file:
        left, right = line.split('   ')

        left_numbers.append(int(left))
        right_numbers.append(int(right))
        
# part 1    
def partOne():
    list1 = sorted(left_numbers)
    list2 = sorted(right_numbers)

    acc = 0
    for i in range(len(list1)):
        acc+= abs(list1[i]-list2[i])

    print(acc)

# part 2
def partTwo():
    # memo to avoid recounting
    memo = {}
    acc = 0
    
    for i in left_numbers:
        if not i in memo:
            memo[i] = right_numbers.count(i)
        acc += i*memo[i]
        
    print(acc)
    
# partOne()
# partTwo()