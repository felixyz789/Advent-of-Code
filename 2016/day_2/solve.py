import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(input):
    with open(input) as f:
        return f.readlines()

def find_code(data):
    result = []
    point = [1,1]
    for i in data:
        for l in i:
            if l == "U" and point[0] > 0:
                    point[0] -= 1
            elif l == "D" and point[0] < 2:
                    point[0] += 1
            elif l == "L" and point[1] > 0:
                    point[1] -= 1
            elif l == "R" and point[1] < 2:
                    point[1] += 1
        result.append([point[0],point[1]])
    return result

def resolve_1():
    data_x = get_file(os.path.join(THIS_DIR, "input.txt"))
    data = [data_x[i].replace("\n","") for i in range(len(data_x))]
    result = find_code(data)
    result_code = ""
    for i in result:
        result_code += str(i[0] *3 + i[1] + 1)
    print(f"Solution 1: {result_code}")
    
def resolve_2():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    keypad = {
        (0,0): "X", (0,1): "X", (0,2): "1", (0,3): "X", (0,4): "X",
        (1,0): "X", (1,1): "2", (1,2): "3", (1,3): "4", (1,4): "X",
        (2,0): "5", (2,1): "6", (2,2): "7", (2,3): "8", (2,4): "9",
        (3,0): "X", (3,1): "A", (3,2): "B", (3,3): "C", (3,4): "X",
        (4,0): "X", (4,1): "X", (4,2): "D", (4,3): "X", (4,4): "X"
    }
    
    current_position= (2,0)
    MIN_ROW = 0
    MIN_COL = 0
    MAX_ROW = 4
    MAX_COL = 4
    
    pin = []
    
    for full_command in inputs:
        for command in full_command:
            x,y = current_position
            if command == "\n":
                break
            if command == "D" and x<MAX_ROW and keypad[(x+1, y)] != "X":
                x+=1
            elif command == "U" and x>MIN_ROW and keypad[(x-1, y)] != "X":
                x-=1
            elif command == "R" and y<MAX_COL and keypad[(x, y+1)] != "X":
                y+=1
            elif command == "L" and y>MIN_COL and keypad[(x, y-1)] != "X":
                y-=1
            
            current_position = (x,y)
        pin.append(keypad[current_position])
        
    solution = "".join(pin)
    
    print("Solution Part 2:", solution)




#def resolve_2():
#    data_x = get_file(os.path.join(THIS_DIR, "input.txt"))
#    data = [data_x[i].replace("\n","") for i in range(len(data_x))]
#    result = find_code2(data)

def main():
    resolve_1()
    resolve_2()
if __name__ == "__main__":
    main()