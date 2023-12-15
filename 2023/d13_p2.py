input = "d13_input.txt"
input = "d13_test.txt"

with open(input, "r") as f:
    data = f.read().split("\n\n")

def check_reflection(map):
    print(map)

    #checks for a horizontal reflection
    for r in range(len(map)-1):
        #print(f"checking row {r+1} and {r+2}")
        if(r<len(map)//2):
            first_section = map[:r+1]
            second_section = map[r+1:r+1+len(first_section)]
            second_section.reverse()
            if first_section == second_section:
                print(f"found reflection between rows {r+1} and {r+2}")
                return (r + 1) * 100
        else:
            second_section = map[r+1:len(map)]
            first_section = map[r-len(second_section)+1:r+1]
            second_section.reverse()
            if first_section == second_section:
                print(f"found reflection between rows {r+1} and {r+2}")
                return (r + 1) * 100
    
    #checks for a vertical reflection
    v_map = []
    for c in zip(*map):
        v_map.append(c)
    for c in range(len(v_map)-1):
        #print(f"checking columns {c+1} and {c+2}")
        if(c<len(v_map)//2):
            first_section = v_map[:c+1]
            second_section = v_map[c+1:c+1+len(first_section)]
            second_section.reverse()
            if first_section == second_section:
                print(f"found reflection between columns {c+1} and {c+2}")
                return c + 1
        else:
            second_section = v_map[c+1:len(v_map)]
            first_section = v_map[c-len(second_section)+1:c+1]
            second_section.reverse()
            if first_section == second_section:
                print(f"found reflection between columns {c+1} and {c+2}")
                return c + 1
    return 0



sum = 0
for m, map in enumerate(data):
    map = map.splitlines()
    for r, row in enumerate(map):
        map[r] = [*row]    
    
    
    for r in range(len(map)):
        for c, col in enumerate(map[r]):
            print(f"Map {m} Row {r} Column {c} should be bit flipped")
            if map[r][c] == "#":
                map[r][c] = "."
            else:
                map[r][c] = "#"
            #unflip the previous space
            if c > 0:
                if map[r][c-1] == "#":
                    map[r][c-1] = "."
                else:
                    map[r][c-1] = "#"
            if c == 0 and r > 0:
                if map[r-1][len(col)] == "#":
                    map[r-1][len(col)] = "."
                else:
                    map[r-1][len(col)] = "#"

            sum += check_reflection(map)  
      
            



    

print(sum)