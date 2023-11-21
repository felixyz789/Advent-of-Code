import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET = 2020

def get_file(input: str) -> list[int]:
    with open (input) as f:
        return[int(x.strip()) for x in f.readlines()]

def solve_1():
    nums_list = get_file(os.path.join(THIS_DIR,"input.txt"))
    set_nums = set(nums_list)
    for n in set_nums:
        if TARGET-n in set_nums:
            print(f'Solution to problem 1: {(TARGET-n) * n}')
            break

def solve_2():
    nums_list = get_file(os.path.join(THIS_DIR,"input.txt"))
    set_nums = set(nums_list)
    for n in set_nums:
        for m in set_nums:
            if TARGET-n-m in set_nums:
                print(f'Solution at the second problem found:{n*m*(TARGET-n-m)}')
                exit()

def main():
    solve_1()
    solve_2()

if __name__ == "__main__":
    main()

