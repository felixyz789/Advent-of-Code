import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_par(input_file):
    with open(input_file) as f:
        for line in f:
            close_par = line.count("(")
            open_par = line.count(")")
    return open_par,close_par
                

def solve_1():
    open_par,close_par = get_par(os.path.join(THIS_DIR, "input.txt"))
    print(f'Solution part 1: {close_par-open_par}')

def solve_2():
    input_file = os.path.join(THIS_DIR, "input.txt")
    count = 0
    index = 0
    with open(input_file) as f:
        while count >= 0:
            char = f.read(1)
            if char == ")":
                count -= 1
                index += 1
            if char == "(":
                count += 1
                index += 1

    print(f'Solution part 2: {index} ')

def main():
    solve_1()
    solve_2()

if __name__ == "__main__":
    main()