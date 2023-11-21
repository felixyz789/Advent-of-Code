import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(input):
    with open(input) as f:
        return f.readlines()

def resolve():
    data = get_file(os.path.join(THIS_DIR, "input.txt"))
    x = [i.strip() for i in data]
    counter = {}
    result = ""
    result_2 = ""

    for i in range(len(x[0])):  
        counter[str(i)] = {}
        for l in x:
            if l[i] in counter[str(i)]:
                counter[str(i)][l[i]] += 1
            else:
                counter[str(i)][l[i]] = 1
    
    for n in counter:
        maximum = 0
        letter = ""
        minimum = 420
        letter_2 = ""
        for l in counter[n]:
            if counter[n][l] > maximum:
                maximm = counter[n][l]
                letter = str(l)
            if counter[n][l] < minimum:
                minimum = counter[n][l]
                letter_2 = str(l)
        result += letter
        result_2 += letter_2

    print(f"Solution of part 1: {result}")
    print(f"Solution of part 2: {result_2}")

def main():
    resolve()

if __name__ == "__main__":
    main()