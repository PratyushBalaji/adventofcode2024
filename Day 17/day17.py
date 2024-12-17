with open(r'adventofcode2024//Day 17//input.txt') as file:
    data = file.readlines()

# combos : 
# 0,1,2,3 - literal 0,1,2,3
# 4 - [A]
# 5 - [B]
# 6 - [C]
# 7 - reserved (not in valid programs)

# opcodes : 
# 0 - division A (adv) : [A] = int([A] // 2^combo)
# 1 - bitwise XOR (bxl) : [B] = [B] ^ combo (combo must be a literal)
# 2 - modulo 8 (bst) : [B] = combo % 8
# 3 - jump if not zero (jnz) : if [A] != 0 : PC += combo (combo must be a literal)
# 4 - bitwise XOR B C (bxc) : [B] = [B] ^ [C] (ignores operand)
# 5 - output (out) : output (combo % 8)
# 6 - division B (bdv) : [B] = int([A] // 2^combo)
# 7 - division C (cdv) : [C] = int([A] // 2^combo)

A = int(data[0].strip().split(':')[1])
B = int(data[1].strip().split(':')[1])
C = int(data[2].strip().split(':')[1])
progLiteral = [int(i) for i in data[4].strip().split(':')[1].split(',')]

PC = 0

prog = {}

output = []

# setup 
count = 0
for i in range(0,len(progLiteral),2):
    prog[count] = (progLiteral[i],progLiteral[i+1])
    count += 1

# print(prog)

def adv(combo):
    global A,PC
    if combo == 4:
        A = (A // (2 ** A))
    elif combo == 5:
        A = (A // (2 ** B))
    elif combo == 6:
        A = (A // (2 ** C))
    else:
        A = (A // (2 ** combo))
    PC+=1

def bxl(combo):
    global B,PC
    if combo <= 3:
        B = B ^ combo
    PC += 1
    
def bst(combo):
    global B, PC
    if combo == 4:
        B = A % 8
    elif combo == 5:
        B = B % 8
    elif combo == 6:
        B = C % 8
    else:
        B = combo % 8
    PC+=1

def jnz(combo):
    global PC
    if A != 0:
        PC = combo
    else:
        PC +=1

def bxc(combo):
    global B, C, PC
    B = B ^ C
    PC += 1

def out(combo):
    global output, PC
    value = 0
    if combo == 4:
        value = A % 8
    elif combo == 5:
        value = B % 8
    elif combo == 6:
        value = C % 8
    else:
        value = combo % 8
    output.append(str(value))
    PC += 1

def bdv(combo):
    global B, PC
    if combo == 4:
        B = (A // (2 ** A))
    elif combo == 5:
        B = (A // (2 ** B))
    elif combo == 6:
        B = (A // (2 ** C))
    else:
        B = (A // (2 ** combo))
    PC += 1

def cdv(combo):
    global C, PC
    if combo == 4:
        C = (A // (2 ** A))
    elif combo == 5:
        C = (A // (2 ** B))
    elif combo == 6:
        C = (A // (2 ** C))
    else:
        C = (A // (2 ** combo))
    PC += 1

funcs = [adv,bxl,bst,jnz,bxc,out,bdv,cdv]

while PC < len(prog):
    funcs[prog[PC][0]](prog[PC][1])
    
print(",".join(output))