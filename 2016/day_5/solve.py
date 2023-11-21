import os
import hashlib

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def resolve_1(input):
    num_end = 0
    
    result = ""
    while len(result) < 8:

        passwd = f"{input}{num_end}"

        input_string = passwd
        
        md5_hash = hashlib.md5()
        md5_hash.update(passwd.encode('utf-8'))
        hashed_string = md5_hash.hexdigest()
        
        if hashed_string[:5] == "00000":
            result += hashed_string[5]

        num_end +=1

    print(f"Result to part 1 : {result}") 

def resolve_2(input):
    num_end = 0
    result = ""
    lolo = {}
    while len(lolo) < 8:
        
        passwd = f"{input}{num_end}"

        input_string = passwd
        
        md5_hash = hashlib.md5()
        md5_hash.update(passwd.encode('utf-8'))
        hashed_string = md5_hash.hexdigest()

        if hashed_string[:5] == "00000" and hashed_string[5].isdigit() and int(hashed_string[5]) < 8:
            if (hashed_string[5]) not in lolo:
                lolo[hashed_string[5]] = hashed_string[6]
                
        num_end +=1   
    
    for i in range(8):
        result += lolo[str(i)]

    print(f"Result to part 2: {result}")

def main():
    input = "ugkcyxxp"
    resolve_1(input)
    resolve_2(input)

if __name__ == "__main__":
    main()