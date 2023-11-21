import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(input):
    ds = []
    with open(input) as f:
        for f in f.readlines():
            checksum = f.split("[")[1].strip()[:-1]
            data = f.split("[")[0].strip()
            id = int(data.split("-")[-1])
            ds.append([data,checksum,id])
    return(ds)

def check(counter,letters):
    test = {}
    test = sorted(counter.items(), key=lambda x: x[1], reverse=True) 
    return(f"{test[0][0]}{test[1][0]}{test[2][0]}{test[3][0]}{test[4][0]}")

def resolve_1():
    data = get_file(os.path.join(THIS_DIR, "input.txt"))
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = 0
    
    for_the_second = []
    for i in data:
        counter = {}
        for l in letters:
            if i[0].count(l) != 0:
                counter[l]=i[0].count(l)
        checksum = check(counter,letters)
        if checksum == i[1]:
            result += i[2]
            for_the_second.append(f"{i[0][:-4]},{i[2]}")

    print(f"Solution to part 1: {result}")
    return[for_the_second[i].split(",") for i in range(len(for_the_second))]

def shift_cy(data):
    letters = "abcdefghijklmnopqrstuvwxyz"
    string = ""   
    for i in data[0]:
        if i == "-":
            string += " "
        else:
            string += letters[((letters.find(i))+int(data[1]))%26]
    return(string)
    
def resolve_2(data):
    TARGET = "northpole"
    for i in data:
        result = shift_cy(i)
        if TARGET in result:
            return(i[1])

def main():
    data = resolve_1()
    result = resolve_2(data)
    print(f"Solution to part 2 : {result}")

if __name__ == "__main__":
    main()