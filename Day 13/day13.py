with open(r'adventofcode2024/Day 13/input.txt') as file:
    data = file.readlines()

# parse vals in this format : 
# [(buttonAx,buttonAy),(buttonBx,buttonBy),(prizex,prizey)]
machines = []
for i in range(0,len(data),4):
    A = data[i].strip().replace('Button A: X+','').replace(', Y+',' ')
    buttonAx,buttonAy = map(int,A.split(' '))
    B = data[i+1].strip().replace('Button B: X+','').replace(', Y+',' ')
    buttonBx,buttonBy = map(int,B.split(' '))
    C = data[i+2].strip().replace('Prize: X=','').replace(', Y=',' ')
    prizex,prizey = map(int,C.split(' '))
    machines.append([(buttonAx,buttonAy),(buttonBx,buttonBy),(prizex,prizey)])

def ignoreFloatError(val):
    # np linalg sometimes has extremely small float errors.
    # If float error is detected, return intended integer, else return the found non-int for processing
    if val-int(val) <= 1e-9:
        return int(val)
    if int(val)+1-val <= 1e-9:
        return int(val)+1
    else:
        return val

import numpy as np
def possibleSolution(vals):
    # solves simultaneous equation and returns true if it has integer solutions
    A = np.array([[vals[0][0], vals[1][0]],[vals[0][1],vals[1][1]]])
    B = np.array([vals[2][0], vals[2][1]])
    C = np.linalg.solve(A,B)
    
    v1 = ignoreFloatError(C[0])
    v2 = ignoreFloatError(C[1])
    
    # check if values found are ints or not, ignoring float errors
    if v1 == int(v1) and v2 == int(v2):
        return v1,v2
    return False
    
def partOne():
    tokens = []
    for i in machines:
        solution = possibleSolution(i)
        if solution != False:
            tokens.append(3*solution[0] + solution[1])
            
    return sum(tokens)
    
print(partOne())
    
def partTwo():
    ...