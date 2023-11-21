import os
from collections import deque

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(input):
    data = []
    with open(input) as f:
        for line in f.readlines():
            tmp = line.split("  ")[1:]
            data.append([int(i.strip()) for i in tmp if i != ""])
    return data                

def resolve_1():
    data = get_file(os.path.join(THIS_DIR, "input.txt"))
    result = 0

    for i in data:
        if i[0]+i[1]>i[2] and i[0]+i[2]>i[1] and i[2]+i[1]>i[0]:
            result += 1
    
    print(f"Solution to part 1: {result}")

def resolve_2():
    data = get_file(os.path.join(THIS_DIR, "input.txt") )
    coda = deque()
    result = 0
    for i in range(0,len(data),+3):
        coda.append(data[i])
        coda.append(data[i+1])
        coda.append(data[i+2])

        if  coda[0][0]+coda[1][0]>coda[2][0] and coda[0][0]+coda[2][0]>coda[1][0] and coda[2][0]+coda[1][0]>coda[0][0]:
            result += 1
        if  coda[0][1]+coda[1][1]>coda[2][1] and coda[0][1]+coda[2][1]>coda[1][1] and coda[2][1]+coda[1][1]>coda[0][1]:
            result += 1
        if  coda[0][2]+coda[1][2]>coda[2][2] and coda[0][2]+coda[2][2]>coda[1][2] and coda[2][2]+coda[1][2]>coda[0][2]:    
            result += 1
        coda.clear()

    print(f"Solution to part 2: {result}")

def main():
    resolve_1()
    resolve_2()

if __name__ == "__main__":
    main()