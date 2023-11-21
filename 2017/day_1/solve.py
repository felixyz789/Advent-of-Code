import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(input):
    with open(input) as f:
        return f.readlines()

def resolve_1():
    data = get_file(os.path.join(THIS_DIR, "input.txt"))
    tmp = []
    tmp.append([data[0][0]])
    for i in range(1,len(data[0])):
        if data[0][i] == tmp[-1][-1]:
            tmp[-1].append(data[0][i])
        else:
            tmp.append([data[0][i]])
        if i == len(data[0])-1:
            if tmp[-1][-1] == tmp[0][-1]:
                for n in tmp[-1]:
                    tmp[0].append(n)
    real = [x for x in tmp if len(x) > 1]
    result = 0
    for l in real:
        if len(l) == 2:
            result += int(l[0])
        else:
            result += (int(l[0]) * (len(l) -1))     
    print(f"Solution to part 1: {result}")

def resolve_2():
    data = get_file(os.path.join(THIS_DIR, "input.txt"))
    result = 0
    str_len = len(data[0]) 
    jumps = str_len // 2
    right = []
    controlled = []

    for i in range(len(data[0])):
        if [i,(i + jumps)%str_len] not in controlled and [(i + jumps)%str_len,i] not in controlled and data[0][i] == (data[0][(i + jumps)%str_len]):
            result += int(data[0][i]) * 2
            controlled.append([i , (i + jumps)%str_len])
        else:
            controlled.append([i , (i + jumps)%str_len])
    
    for i in right:
        for n in i:
            result += int(n)
    print(f"Solution to part 2: {result}")

def main():
    resolve_1()
    resolve_2()

if __name__ == "__main__":
    main()