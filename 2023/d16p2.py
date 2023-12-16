input = "d16_input.txt"
#input = "d16_test.txt"

with open(input,"r") as f:
    data = f.readlines()

starting_position = (0,-1) #row, col
starting_dir = "East"
start_pos_dir = [starting_position, starting_dir]


def num_tiles_traveled(start_pos_dir):
    traveled_list = []
    buffer = []
    print(start_pos_dir)
    buffer.append(start_pos_dir)
    while buffer:

        pos_dir = buffer.pop(0)
        traveled_list.append(pos_dir)
        pos = pos_dir[0]
        dir = pos_dir[1]
        next_pos = None
  

        #check what type of square i'm on
        if dir == "North" and pos[0] > 0:
            next_pos = (pos[0]-1,pos[1])
            if data[next_pos[0]][next_pos[1]] in ".|":
                next_pos_dir = [next_pos, "North"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == "-":
                next_pos_dir = [next_pos, "East"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
                next_pos_dir = [next_pos, "West"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == '\\':
                next_pos_dir = [next_pos, "West"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == '/':
                next_pos_dir = [next_pos, "East"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
        elif dir == "South" and pos[0] < len(data)-1:
            next_pos = (pos[0]+1,pos[1])
            if data[next_pos[0]][next_pos[1]] in ".|":
                next_pos_dir = [next_pos, "South"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == "-":
                next_pos_dir = [next_pos, "East"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
                next_pos_dir = [next_pos, "West"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == '\\':
                next_pos_dir = [next_pos, "East"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == '/':
                next_pos_dir = [next_pos, "West"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
        elif dir == "East" and pos[1] < len(data[0].strip())-1:
            next_pos = (pos[0],pos[1]+1)
            if data[next_pos[0]][next_pos[1]] in ".-":
                next_pos_dir = [next_pos, "East"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == "|":
                next_pos_dir = [next_pos, "North"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
                next_pos_dir = [next_pos, "South"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == '\\':
                next_pos_dir = [next_pos, "South"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == '/':
                next_pos_dir = [next_pos, "North"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
        elif dir == "West" and pos[1] > 0:
            next_pos = (pos[0],pos[1]-1)
            if data[next_pos[0]][next_pos[1]] in ".-":
                next_pos_dir = [next_pos, "West"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == "|":
                next_pos_dir = [next_pos, "North"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
                next_pos_dir = [next_pos, "South"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == '\\':
                next_pos_dir = [next_pos, "North"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
            elif data[next_pos[0]][next_pos[1]] == '/':
                next_pos_dir = [next_pos, "South"]
                if next_pos_dir not in traveled_list: buffer.append(next_pos_dir)
        #print(buffer)

    #print(traveled_list)

    unique_locations_traveled = []


    for item in traveled_list:
        if item[0] not in unique_locations_traveled:
            unique_locations_traveled.append(item[0])

    num_tiles = len(unique_locations_traveled)-1
    print(f"num_tiles = {num_tiles}")
    return num_tiles

max_tiles = 0

part_one = num_tiles_traveled(start_pos_dir)


for i in range(len(data)):
    start_pos_dir = [(i,-1),"East"]
    new_num = num_tiles_traveled(start_pos_dir)
    if new_num>max_tiles:
        max_tiles = new_num
for i in range(len(data)):
    start_pos_dir = [(i,len(data[i])),"West"]
    new_num = num_tiles_traveled(start_pos_dir)
    if new_num>max_tiles:
        max_tiles = new_num
for i in range(len(data[0])):
    start_pos_dir = [(-1,i),"South"]
    new_num = num_tiles_traveled(start_pos_dir)
    if new_num>max_tiles:
        max_tiles = new_num
for i in range(len(data[0])):
    start_pos_dir = [(len(data)-1,i),"North"]
    new_num = num_tiles_traveled(start_pos_dir)
    if new_num>max_tiles:
        max_tiles = new_num

print(f"part_one = {part_one}")
print(f"part_two = {max_tiles}")
