import copy

input = "d10_input.txt"

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# for my input, the starting position is at 53, 75
# input is map[y][x] y starts on the top of the map and goes down

def clean_grid(map,loop,start):
    clean_map = copy.deepcopy(map)
    
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "S":
                clean_map[y][x] = which_type_is_the_start_pipe(map, start)
            elif (x,y) not in loop:
                clean_map[y][x] = "."
    return clean_map

def which_type_is_the_start_pipe(map, start):
    start_x = start[0]
    start_y = start[1]

    north = "."
    south = "."
    west = "."
    east = "."

    if start_y > 0: north = map[start_y - 1][start_x]
    if start_y < len(map): south = map[start_y + 1][start_x]
    if start_x > 0: west = map[start_y][start_x - 1]
    if start_x < len(map[start_y]): east = map[start_y][start_x + 1]


    north_connection = False
    south_connection = False
    west_connection = False
    east_connection = False

    if north == "|" or north == "7" or north == "F": north_connection = True
    if south == "|" or south == "L" or south == "J": south_connection = True
    if west == "-" or west == "L" or west == "F": west_connection = True
    if east == "-" or east == "7" or east == "J": east_connection = True

    if north_connection and south_connection: return "|"
    if west_connection and east_connection: return "-"
    if north_connection and east_connection: return "L"
    if north_connection and west_connection: return "J"
    if south_connection and west_connection: return "7"
    if south_connection and east_connection: return "F"

def find_start(map):
    start_x = 0
    start_y = 0


    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "S":
                start_x = x
                start_y = y

    return (start_x, start_y)

def path_coordinates_list(map,start_type,starting_position):
    start_x = starting_position[0]
    start_y = starting_position[1]
    path_coordinates = [starting_position]

    if start_type == "|": 
        direction_1 = (start_x, start_y + 1)
        direction_2 = (start_x, start_y - 1)
    if start_type == "-": 
        direction_1 = (start_x + 1, start_y)
        direction_2 = (start_x - 1, start_y)
    if start_type == "L": 
        direction_1 = (start_x, start_y - 1)
        direction_2 = (start_x + 1, start_y)
    if start_type == "J":
        direction_1 = (start_x, start_y - 1)
        direction_2 = (start_x - 1, start_y)
    if start_type == "7":
        direction_1 = (start_x, start_y + 1)
        direction_2 = (start_x - 1, start_y)
    if start_type == "F":
        direction_1 = (start_x, start_y + 1)
        direction_2 = (start_x + 1, start_y)

    distance = 1
    prev_loc_1 = starting_position
    prev_loc_2 = starting_position
    while(direction_1 != direction_2):
        #initialized the starting location for traversing the pipe in both directions
        path_coordinates.append(direction_1)
        path_coordinates.append(direction_2)


        direction_1,prev_loc_1 = next_loc(prev_loc_1,direction_1,map[direction_1[1]][direction_1[0]])
        direction_2,prev_loc_2 = next_loc(prev_loc_2,direction_2,map[direction_2[1]][direction_2[0]])
        
        distance += 1

    path_coordinates.append(direction_1)

    return path_coordinates
    
def next_loc(prev_loc,current_loc,type):
    #did i come from the north, south, east, or west?
    frm_north = False
    frm_south = False
    frm_west = False
    frm_east = False

    

    if prev_loc[1]>current_loc[1]: frm_south = True
    if prev_loc[1]<current_loc[1]: frm_north = True
    if prev_loc[0]>current_loc[0]: frm_east = True
    if prev_loc[0]<current_loc[0]: frm_west = True

    new_loc = (0,0)

    if type == "|":
        if frm_north: new_loc = (current_loc[0], current_loc[1] + 1)
        if frm_south: new_loc = (current_loc[0], current_loc[1] - 1)
    if type == "-":
        if frm_east: new_loc = (current_loc[0] - 1, current_loc[1])
        if frm_west: new_loc = (current_loc[0] + 1, current_loc[1])
    if type == "L":
        if frm_east: new_loc = (current_loc[0], current_loc[1] - 1)
        if frm_north: new_loc = (current_loc[0] + 1, current_loc[1])
    if type == "J":
        if frm_west: new_loc = (current_loc[0], current_loc[1] - 1)
        if frm_north: new_loc = (current_loc[0] - 1, current_loc[1])
    if type == "7":
        if frm_west: new_loc = (current_loc[0], current_loc[1] + 1)
        if frm_south: new_loc = (current_loc[0] - 1, current_loc[1])
    if type == "F":
        if frm_east: new_loc = (current_loc[0], current_loc[1] + 1)
        if frm_south: new_loc = (current_loc[0] + 1, current_loc[1])

    return new_loc, current_loc

with open(input,"r") as f:
    map = f.read().split("\n")
    print(len(map))
    print(len(map[0]))
    for i, line in enumerate(map):
        line = [*line]
        map[i] = line
    
starting_position = find_start(map)

starting_type = which_type_is_the_start_pipe(map, starting_position)

coordinates = path_coordinates_list(map, starting_type,starting_position)

clean_map = clean_grid(map,coordinates,starting_position)

inside = []

"""loops through the cleaned map horizontally. "inside_loop" is initially set to false and when it crosses a pipe, the condition is flipped 
(EG: if it crosses a vertical pipe once, it's inside the pipe, if it crosses twice, it's outside) 

There are 2 ways to "cross" a pipe. The first is just crossing the "|" symbol. The second is when you travel along a horizontal pipe, 
and first encounter an L, then flip to a 7 (This is because the pipe "flipped") 

"""
for i, line in enumerate(clean_map):
    inside_loop = False
    up = None
    for j,char in enumerate(line):
        if char == "|":
            assert up is None
            inside_loop = not inside_loop
        elif char =="-":
            assert up is not None
        elif char in "LF":
            assert up is None
            up = char == "L"
        elif char in "7J":
            assert up is not None
            if char != ("J" if up else "7"):
                inside_loop = not inside_loop
            up = None
        elif char == ".":
            pass
        else:
            raise RuntimeError(f"Unexpected character: {char}")

        if inside_loop and char == ".":
            inside.append((j,i))
            clean_map[i][j] = "I"



print(inside)
print(len(inside))

for line in clean_map:
    print(''.join(line))


