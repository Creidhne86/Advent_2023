from collections import defaultdict

input = "d8_input.txt"
map_dict = defaultdict(str)
first_key_bool = True

with open(input,"r") as f:
    data = f.read()
    instructions, map_data = data.split("\n\n")
    map = map_data.split("\n")
    for m in map:
        key, directions = m.split("=")
        key = key.strip()
        if first_key_bool:
            first_key = "AAA"
            first_key_bool = False
        directions = directions.replace("(","").replace(")","").split(",")
        directions[0] = directions[0].strip()
        directions[1] = directions[1].strip()
        map_dict[key] = directions
    
    #print(f"{map_dict}")

    steps = 0
    current_key = first_key

    for i in range(1000000) :
        input_num = steps%len(instructions)
        #print(f"{input_num}, {instructions[input_num]}, {current_key}")
        


        if instructions[input_num] == "L":
            current_key = map_dict[current_key][0]
        elif instructions[input_num] == "R":
            current_key = map_dict[current_key][1]
        steps += 1
        if current_key == "ZZZ":
            break

    print(steps)