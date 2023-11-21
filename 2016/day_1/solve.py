import os
import math

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(input):
    with open(input) as f:
        a =[i.split(",") for i in f.readlines()]
        return[i.strip() for i in a[0]]

def resolve_1(data):
    dir = "n"
    x = 0
    y = 0
    for i in data:        
        if dir == "n":
            if i[0] == "R":
                x += int(i[1:])
                dir = "e"
                continue
            if i[0] == "L":
                x -= int(i[1:]) 
                dir = "o"
                continue
        if dir == "s":
            if i[0] == "R":
                x -= int(i[1:])
                dir = "o"
                continue
            if i[0] == "L":
                x += int(i[1:])
                dir = "e"
                continue
        if dir == "o":
            if i[0] == "R":
                y += int(i[1:])
                dir = "n"
                continue    
            if i[0] == "L":
                y -= int(i[1:])
                dir = "s"
                continue
        if dir == "e":
            if i[0] == "R":
                y -= int(i[1:])
                dir = "s"
                continue
            if i[0] == "L":
                y += int(i[1:])
                dir = "n"
                continue
    print(f"Solution 1: {abs(x)+abs(y)}")


def resolve_2(data):
    dir = "n"
    x = 0
    y = 0
    start = 0
    positions = []
    for i in data:
        if start == 0:
            positions.append(f"{x},{y}")      
            start = 1
        if dir == "n":
            if i[0] == "R":
                for n in range(x+1,(x+int(i[1:])+1)):
                    if (f"{n},{y}") in positions:
                        return(abs(n)+abs(y))
                    positions.append(f"{n},{y}")
                x += int(i[1:])
                dir = "e"
                continue
            if i[0] == "L":
                for n in range(x-1,(x-int(i[1:])-1),-1):
                    if (f"{n},{y}") in positions:
                        return(abs(n)+abs(y))
                    positions.append(f"{n},{y}")
                x -= int(i[1:]) 
                dir = "o"
                continue
        if dir == "s":
            if i[0] == "R":
                for n in range(x-1,(x-int(i[1:])-1),-1):
                    if (f"{n},{y}") in positions:
                        return(abs(n)+abs(y))
                    positions.append(f"{n},{y}")
                x -= int(i[1:])
                dir = "o"
                continue
            if i[0] == "L":
                for n in range(x+1,(x+int(i[1:])+1)):
                    if (f"{n},{y}") in positions:
                        return(abs(n)+abs(y))
                    positions.append(f"{n},{y}")
                x += int(i[1:])
                dir = "e"
                continue
        if dir == "o":
            if i[0] == "R":
                for n in range(y+1,(y+int(i[1:])+1)):
                    if (f"{x},{n}") in positions:
                        return(abs(x)+abs(n))
                    positions.append(f"{x},{n}")
                y += int(i[1:])
                dir = "n"
                continue    
            if i[0] == "L":
                for n in range(y-1,(y-int(i[1:])-1),-1):
                    if (f"{x},{n}") in positions:
                        return(abs(x)+abs(n))
                    positions.append(f"{x},{n}")
                y -= int(i[1:])
                dir = "s"
                continue
        if dir == "e":
            if i[0] == "R":
                for n in range(y-1,(y-int(i[1:])-1),-1):
                    if (f"{x},{n}") in positions:
                        return(abs(x)+abs(n))
                    positions.append(f"{x},{n}")
                y -= int(i[1:])
                dir = "s"
                continue
            if i[0] == "L":
                for n in range(y+1,(y+int(i[1:])+1)):
                    if (f"{x},{n}") in positions:
                        return(abs(x)+abs(n))                    
                    positions.append(f"{x},{n}")
                y += int(i[1:])
                dir = "n"
                continue

def solve_1():
    data = get_file(os.path.join(THIS_DIR, "input.txt"))
    resolve_1(data)

def solve_2():
    data = get_file(os.path.join(THIS_DIR, "input.txt"))
    result = resolve_2(data)
    print(f"Solution 2: {result}")
    
def main():
    solve_1()
    solve_2()

if __name__ == "__main__":
    main()