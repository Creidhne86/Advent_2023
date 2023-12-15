from collections import defaultdict

input = "d15_input.txt"
#input = "d15_test.txt"

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
max_box = 256
for i in range(max_box):
    box_data["Box " + str(i)] = []


box_num = 0

sum = 0
for l, line in enumerate(data):
    line = line.strip()
    print(f"Processing Line {l+1}: {line}")
    if "=" in line:
        line = line.split("=")
        box_num ="Box " + str(hashing(line[0]))
        print(f"{box_num} = {line[0]}")
        line_data = line[0]+ " " + line[1]
        has_lens = False

        for i, lens in enumerate(box_data[box_num]):
            lens_val = lens.split()
            if line[0] == lens_val[0]:
                print(f"{box_num}: has lens {line[0]} at index {i}")
                box_data[box_num][i] = line_data
                has_lens = True
        if not has_lens:
            box_data[box_num].append(line_data)
    if "-" in line:
        line = line.split("-")
        box_num ="Box " + str(hashing(line[0]))
        print(f"Trying to remove {line[0]} from {box_num} = {box_data[box_num]}")
        for i, lens in enumerate(box_data[box_num]):
            if line[0] in lens:
                print(f"{box_num}: has lens {line[0]} at index {i} which is being removed")
                box_data[box_num].pop(i)
        else:
            #pass
            print("No lens to remove")
    print(f"updated {box_num} to {box_data[box_num]}")

  
for box in box_data:
    print(f"{box}: {box_data[box]}")



focusing_power = 0
print("Calculating focusing power")
for i in box_data:
    print(i)
    print(box_data[i])
    
    for j,li in enumerate(box_data[i]):
        individual_focus = 1
        lens_data = li.split()
        (hashing(lens_data[0])+1)*(j+1)*int(lens_data[1])
        individual_focus *= (hashing(lens_data[0])+1)*(j+1)*int(lens_data[1])
        print(f"Individual focus: {individual_focus}")
        focusing_power += individual_focus

    
print(f"Total power: {focusing_power}")

#print(box_data)

