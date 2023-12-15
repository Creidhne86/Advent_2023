from collections import defaultdict

input = "d15_input.txt"
input = "d15_test.txt"

with open(input,"r") as f:
    data = f.read().split(",")

def hashing(input):
    value = 0
    for ch in input:
        ascii = ord(ch)
        #print(f"{ch} = {ascii}")
        value += ascii
        value = value*17
        value = value % 256 
    return value

#print(hashing("ot"))


box_data = defaultdict(list)

box_num = 0

sum = 0
for line in data:
    line = line.strip()
    if "=" in line:
        line = line.split("=")
        box_num ="Box " + str(hashing(line[0]))
        #print(f"{box_num} = {line[0]}")
        line_data = line[0]+ " " + line[1]
        box_data[box_num].append(line_data)
        # implement lens switching
    if "-" in line:
        line = line.split("-")
        print(line)
        print(box_data)
        box_num ="Box " + str(hashing(line[0]))
        
        print(box_data[box_num])
    #print(line)

print(box_data)

