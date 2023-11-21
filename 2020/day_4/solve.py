import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_cred(input_file):
    with open(input_file) as f:
        file_content = f.read()
        list_of_cred = file_content.split('\n\n') 
        new_arr = [list_of_cred[i].replace('\n',' ') for i in range(len(list_of_cred))]           
        return new_arr

def resolve_1():
    list_of_cred = get_cred(os.path.join(THIS_DIR,"input.txt"))
    solution = 0
    words = ("byr","iyr","eyr","hgt","hcl","ecl","pid")
    valid_arr = []
    for item in list_of_cred:
        counter = 0
        for word in words:
            if word in item:
                counter += 1
            else:
                break
        if counter == 7:
            solution += 1
            valid_arr.append(item)
    print(f'Solution at the first problem: {solution}')
    return valid_arr

def resolve_2(valid_arr):
    new_arr = [i.split(" ") for i in valid_arr]
    solution = 0
    for i in range(len(new_arr)):
        counter = 0
        for item in new_arr[i]:
            k,v = item.split(":")
            if k == "byr":
                if 1920 <= int(v) <= 2002:
                    counter += 1
            elif k == "iyr":
                if 2010 <= int(v) <= 2020:
                    counter += 1
            elif k == "eyr":
                if 2020 <= int(v) <= 2030:
                    counter += 1
            elif k == "hgt":
                if v[-2:] == "cm":
                    if 150 <= int(v[:-2]) <= 193:
                        counter += 1
                if v[-2:] == "in":
                    if 59 <= int(v[:-2]) <= 76:
                        counter += 1
            elif k == "hcl":
                dizionario = "01234567890abcdef"
                counter_hcl = 0
                if v[0] == "#" and len(v) == 7:
                    for i in range(len(v[1:])):
                        if v[i+1] in dizionario:
                            counter_hcl += 1
                    if counter_hcl == 6:
                        counter += 1
            elif k == "ecl":
                filt = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]    
                if v in filt:
                    counter += 1
            elif k == "pid":
                if len(v) == 9:
                    counter += 1
        if counter == 7:
            solution += 1
    print(f'Solution at the second problem: {solution}')

def main():
    valid_arr = resolve_1()
    resolve_2(valid_arr)

if __name__ == "__main__":
    main()