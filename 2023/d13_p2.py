input = "d13_input.txt"
#input = "d13_test.txt"

with open(input, "r") as f:
    data = f.read().split("\n\n")

def check_reflection(map,original_val = -1):
    #print(map)

    #checks for a horizontal reflection
    for r in range(len(map)-1):
        #print(f"checking row {r+1} and {r+2}")
        if(r<len(map)//2):
            first_section = map[:r+1]
            second_section = map[r+1:r+1+len(first_section)]
            second_section.reverse()
            if first_section == second_section:
                print(f"found horizontal reflection between rows {r+1} and {r+2}")
                new_val = (r + 1) * 100
                if new_val!=original_val:
                    return new_val

        else:
            second_section = map[r+1:len(map)]
            first_section = map[r-len(second_section)+1:r+1]
            second_section.reverse()
            if first_section == second_section:
                print(f"found horizontal reflection between rows {r+1} and {r+2}")
                new_val = (r + 1) * 100
                if new_val!=original_val:
                    return new_val
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
                print(f"found vertical reflection between columns {c+1} and {c+2}")
                new_val = c + 1
                if new_val!=original_val:
                    return new_val
        else:
            second_section = v_map[c+1:len(v_map)]
            first_section = v_map[c-len(second_section)+1:c+1]
            second_section.reverse()
            if first_section == second_section:
                print(f"found vertical reflection between columns {c+1} and {c+2}")
                print(f"i should return {c+1}")
                new_val = c + 1
                if new_val!=original_val:
                    return new_val
    return 0

def print_map(map):
    for row in map:
        print("".join(row))

def find_smudge_reflection(map):
    map = map.splitlines()
    for r, row in enumerate(map):
        map[r] = [*row]    
    
    original_val = check_reflection(map)
    print(f"Original value is {original_val}")

    for r in range(len(map)):
        row_len = len(map[r])
        for c, col in enumerate(map[r]):
            
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
                if map[r-1][row_len-1] == "#":
                    map[r-1][row_len-1] = "."
                else:
                    map[r-1][row_len-1] = "#"
            print(f"Map {m+1} Row {r+1} Column {c+1} was bit flipped")
            print_map(map)
            new_val = check_reflection(map,original_val)
            print(new_val)
            if new_val != original_val and new_val != 0:
                print(f"   Found a new reflection! {new_val} should be added to the sum")
                return new_val

sum = 0
for m, map in enumerate(data):
    print(f"Processing Map {m}")
    sum += find_smudge_reflection(map)

        #print_map(map)            
                
      
            



    

print(sum)