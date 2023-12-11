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

    #print(f"north: {north}")
    #print(f"south: {south}")
    #print(f"west: {west}")
    #print(f"east: {east}")

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
                #print(f"start_x: {start_x}")
                #print(f"start_y: {start_y}")
    return (start_x, start_y)

def distance_from_start(map,start_type,starting_position):
    start_x = starting_position[0]
    start_y = starting_position[1]
    distance_map = copy.deepcopy(map)

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
        distance_map[direction_1[1]][direction_1[0]] = "X"
        distance_map[direction_2[1]][direction_2[0]] = "X"

        #print(1)
        direction_1,prev_loc_1 = next_loc(prev_loc_1,direction_1,map[direction_1[1]][direction_1[0]])
        #print(2)
        direction_2,prev_loc_2 = next_loc(prev_loc_2,direction_2,map[direction_2[1]][direction_2[0]])
        
        distance += 1

    print(distance)

    distance_map[direction_1[1]][direction_1[0]] = str(distance)
    distance_map[direction_2[1]][direction_2[0]] = str(distance)

    return distance_map
    
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

    #print(f"My current location is {current_loc}, my previous location was {prev_loc}, my type is {type}")
    #print(f"frm_north: {frm_north}")
    #print(f"frm_south: {frm_south}")
    #print(f"frm_west: {frm_west}")
    #print(f"frm_east: {frm_east}")

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

    #print(f"My new location is {new_loc}")

    return new_loc, current_loc

with open(input,"r") as f:
    map = f.read().split("\n")
    for i, line in enumerate(map):
        line = [*line]
        map[i] = line
    
starting_position = find_start(map)
starting_type = which_type_is_the_start_pipe(map, starting_position)

distance_map = distance_from_start(map, starting_type,starting_position)


for line in distance_map:
    print(''.join(line))


