from collections import defaultdict
from math import gcd

input = "d8_input.txt"
map_dict = defaultdict(str)
first_key_list = []

with open(input,"r") as f:
    data = f.read()
    instructions, map_data = data.split("\n\n")
    map = map_data.split("\n")
    for m in map:
        key, directions = m.split("=")
        key = key.strip()
        if key[2] == "A":
            first_key_list.append(key)
        directions = directions.replace("(","").replace(")","").split(",")
        directions[0] = directions[0].strip()
        directions[1] = directions[1].strip()
        map_dict[key] = directions



print(first_key_list)
steps_list = []

for k in first_key_list:
    steps = 0
    current_key = k

    for i in range(1000000) :
        input_num = steps%len(instructions)
        #print(f"{input_num}, {instructions[input_num]}, {current_key}")
        


        if instructions[input_num] == "L":
            current_key = map_dict[current_key][0]
        elif instructions[input_num] == "R":
            current_key = map_dict[current_key][1]
        steps += 1
        if current_key[2] == "Z":
            break
    steps_list.append(steps)

print(steps_list)


lcm = 1
for i in steps_list:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)

"""steps = 0
current_key_list = first_key_list

for i in range(50) :
    input_num = steps%len(instructions)

    for k in  range(len(current_key_list)):
        if instructions[input_num] == "L":
            #print(current_key_list[k])
            current_key_list[k] = map_dict[current_key_list[k]][0]
        if instructions[input_num] == "R":
            current_key_list[k] = map_dict[current_key_list[k]][1]
    steps += 1
    print(f"{instructions[input_num]},{current_key_list}")
    all_keys_end_in_z = True
    for k in  range(len(current_key_list)):
        if current_key_list[k][2] != "Z":
            all_keys_end_in_z = False
    
    if all_keys_end_in_z == True: break



print(steps)

"""
