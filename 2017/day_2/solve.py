import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(input):
    with open(input) as f:
        ds = [x.strip().split("\n") for x in f.readlines()]
        real = [x.split("\t") for i in ds for x in i ]
        print(real)

def resolve_1():
    data = get_file(os.path.join(THIS_DIR, "input.txt"))
    result = 0
    for i in data:
        maxim = int(i[0])
        minim = int(i[0])
        for n in i:
            if int(n) > maxim:
                maxim = int(n)
            if int(n) < minim:
                minim= int(n)
        result += (maxim-minim)
    print(f"Result to part 1: {result}")

def resolve_2():
    data = get_file(os.path.join(THIS_DIR, "input.txt"))
    result = 0
    for i in data:
        for n in i:
            for b in i:
                if int(b) % int(n) == 0 and int(b) != int(n):                     
                    result += (int(b)//int(n))
    print(f"Solution to part 2: {result}")

def main():
    resolve_1()
    resolve_2()

if __name__ == "__main__":
    main()