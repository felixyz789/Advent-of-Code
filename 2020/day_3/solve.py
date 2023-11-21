import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path):
    with open(path) as f:
        return [x.strip() for x in f.readlines()]

def resolve(right,down):
    input_file = get_file(os.path.join(THIS_DIR,"input.txt"))
    solution = 0
    ROW_LEN = len(input_file[0])
    current_position = 0
    for i in range(0,len(input_file),down):
        if input_file[i][current_position%(ROW_LEN)] == "#":
            solution += 1
        current_position += right
    return solution

def main():
    solution_1 = resolve(3,1)
    print(f"Solution at the first problem: {solution_1}")
    solution_2  = resolve(1,1)*resolve(3,1)*resolve(5,1)*resolve(7,1)*resolve(1,2)
    print(f"Solution at the second problem: {solution_2}")

if __name__ == "__main__":
    main()