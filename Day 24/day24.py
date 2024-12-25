with open(r'adventofcode2024//Day 24//input.txt') as file:
    data = file.readlines()

wires = {}
ops = []


flag = True
for i in data:
    if i == '\n':
        flag = False
        continue
    if flag:
        wire,val = i.strip().split(':')
        wires[wire] = int(val)
    else:
        ops.append(i.strip())
        

def XOR(a,b):
    return a^b

def AND(a,b):
    return a&b

def OR(a,b):
    return a|b
        
def operate(value):
    if not ' ' in str(value):
        return value
    else:
        regA,func,regB = value.split(' ')
        return eval(f"{func}({operate(wires[regA])},{operate(wires[regB])})")
    
# print(ops)
for i in ops:
    op,target = i.split(' -> ')
    wires[target] = op

for i in wires.keys():
    wires[i] = operate(wires[i])
    
def partOne():
    final = sorted([(i,wires[i]) for i in wires.keys() if i[:1] == 'z'],reverse=True)
    return int(''.join([str(i[1]) for i in final]),2)

print(partOne())