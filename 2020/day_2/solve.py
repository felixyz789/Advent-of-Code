import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def resolve_1():
    passwd_file = os.path.join(THIS_DIR,"input.txt")
    valid_passwd = 0    
    with open (passwd_file) as f:
        for lines in f:
            nospace = lines.split(" ")
            letter = nospace[1][:-1]
            passwd = nospace[2]
            minimum,maximum = nospace[0].split("-")
            if int(minimum) <= passwd.count(letter) <= int(maximum):
                valid_passwd += 1
    print(f'Solution at the first problem: {valid_passwd}')

def resolve_2():
    passwd_file = os.path.join(THIS_DIR,"input.txt")
    valid_passwd = 0    
    with open (passwd_file) as f:
        for lines in f:
            nospace = lines.split(" ")
            letter = nospace[1][:-1]
            passwd = nospace[2]
            minimum,maximum = nospace[0].split("-")
            if bool(passwd[int(minimum)-1] == letter) ^ bool(passwd[int(maximum)-1] == letter):
                valid_passwd += 1
    print(f'Solution at the second problem: {valid_passwd}')

if __name__ == "__main__":
    resolve_1()
    resolve_2()