from collections import defaultdict 

input  = "d3_input.txt"

with open(input,"r") as f:
    santa_loc = [0,0]
    robo_santa_loc = [0,0]
    houses = defaultdict(int)
    print(houses)
    for line in f:
        
        for i,char in enumerate(line):
            if i%2 == 0:
                if char == "^":
                    santa_loc[1]+=1
                if char == "v":
                    santa_loc[1]-=1
                if char == ">":
                    santa_loc[0]+=1
                if char == "<":
                    santa_loc[0]-=1
                santa_tuple_loc = tuple(santa_loc)
                houses[santa_tuple_loc] +=1
            else:
                if char == "^":
                    robo_santa_loc[1]+=1
                if char == "v":
                    robo_santa_loc[1]-=1
                if char == ">":
                    robo_santa_loc[0]+=1
                if char == "<":
                    robo_santa_loc[0]-=1
                robo_santa_tuple_loc = tuple(robo_santa_loc)
                houses[robo_santa_tuple_loc] +=1

print(len(houses))