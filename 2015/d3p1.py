from collections import defaultdict 

input  = "d3_input.txt"

with open(input,"r") as f:
    loc = [0,0]
    houses = defaultdict(int)
    print(houses)
    for line in f:
        for char in line:
            if char == "^":
                loc[1] = loc[1] + 1
            if char == "v":
                loc[1]-=1
            if char == ">":
                loc[0]+=1
            if char == "<":
                loc[0]-=1
            tuple_loc = tuple(loc)
            houses[tuple_loc] +=1

print(len(houses))
