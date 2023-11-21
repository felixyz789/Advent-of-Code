import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_sides(input_file):
    with open(input_file) as f:
        return [line.replace("\n","").split("x") for line in f.readlines()]

def solve_1():
    arr = get_sides(os.path.join(THIS_DIR, "input.txt"))
    total = 0
    for i in arr:
        toint = [int(n) for n in i]
        smallest = sorted(toint)
        pack_surface = 2*toint[0]*toint[1] + 2*toint[2]*toint[1] + 2*toint[0]*toint[2] + smallest[0] * smallest[1]
        total += pack_surface

    print(f'Solution to part 1: {total}')

def solve_2():
    arr = get_sides(os.path.join(THIS_DIR, "input.txt"))
    total = 0
    for i in arr:
        toint = [int(n) for n in i]
        smallest = sorted(toint)
        ribbon = (smallest[0]*2 + smallest[1]*2) + (toint[0]*toint[1]*toint[2])
        total += ribbon
    print(f'Solution to part 2: {total}')

def main():
    solve_1()
    solve_2()

if __name__ == "__main__":
    main()