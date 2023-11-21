import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def is_abba(stringa):
    for i in range(1,len(stringa)-2):
        char_1 = stringa[i]
        char_2 = stringa[i+1]
        if char_1 == char_2 and stringa[i-1] == stringa[i+2] and stringa[i-1] != stringa[i]:
            return True 
    return False

def resolve_1():
    input = os.path.join(THIS_DIR, "input.txt")
    result = 0
    with open(input) as f:
        for f in f.readlines():
            square = False
            outofsquare = False
            tmp = f.strip().split("]")
            outof = [i.split("[")[0] for i in tmp]
            insquare = [i.split("[")[1] for i in tmp if "[" in i]            
            for e in outof:
                if is_abba(e):
                    outofsquare = True
                    break
            for e in insquare:
                if is_abba(e):
                    square = True
                    break
            if square == False and outofsquare == True:
                result+=1
    print(f"Result of part 1:{result}")

#----------------------

def is_aba(stringa,insquare):
    for l in range(0,len(stringa)-2):
        char_1 = stringa[l]
        char_2 = stringa[l+2]
        if char_1 == char_2:
            aba = f"{char_1}{stringa[l+1]}{char_2}"
            bab =  f"{stringa[l+1]}{char_1}{stringa[l+1]}"
            for e in insquare:
                if bab in e:
                    return True
    return False

def resolve_2():
    input = os.path.join(THIS_DIR, "input.txt")
    result = 0
    with open(input) as f:
        for f in f.readlines():
            aba = False
            tmp = f.strip().split("]")
            outof = [i.split("[")[0] for i in tmp]
            insquare = [i.split("[")[1] for i in tmp if "[" in i] 
            for i in outof:
                if is_aba(i,insquare):
                    aba = True
                    break
            if aba == True:
                result += 1
    print(f"Result to part 2: {result}")

def main():
    resolve_1()
    resolve_2()

if __name__ == "__main__":
    main()