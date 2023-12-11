
#input = "d11_test.txt"
input = "d11_input.txt"
data = []


def find_galaxies(galaxy,empty_rows,empty_cols):
    galaxies = []
    expansion_value = 1000000
    for r, row in enumerate(galaxy):
        for c, char in enumerate(row):
            if char == "#":
                #calculate the number of rows and columns that are smaller than r and c, add a fixed expansion value* the number of empty rows and columns
                num_r = 0
                num_c = 0
                exp_r = 0
                exp_c = 0
                for i in empty_rows:
                    if i < r:
                        num_r += 1
                for j in empty_cols:
                    if j < c:
                        num_c += 1
                if num_r != 0: exp_r = num_r*expansion_value - num_r
                if num_c !=0: exp_c = num_c*expansion_value - num_c

                galaxies.append((r+exp_r,c+exp_c))
    return galaxies

def expand_galaxy(galaxy):
    expansion_rows = []
    expansion_columns = []
    
    
    for r, row in enumerate(galaxy):
        found_galaxy = False
        for c, char in enumerate(row):
            if char == "#":
                found_galaxy = True
                break
        if not found_galaxy:
            print(f"row {r} is empty and shall be expanded")
            expansion_rows.append(r)
    

    for c, col in enumerate(zip(*galaxy)):
        found_galaxy = False
        for r, char in enumerate(col):
            if char == "#":
                found_galaxy = True
                break
        if not found_galaxy:
            print(f"col {c} is empty and shall be expanded")
            expansion_columns.append(c)
    
    return expansion_rows,expansion_columns
def calculate_distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

with open(input,"r") as f:
    data = f.read().split("\n")
    for i, line in enumerate(data):
        line = [*line]
        data[i] = line

for line in data:
    print(''.join(line))

empty_rows, empty_cols = expand_galaxy(data)

print(f"Empty rows: {empty_rows}")
print(f"Empty cols: {empty_cols}")

galaxy_list = find_galaxies(data, empty_rows, empty_cols)


print(galaxy_list)

sum = 0

for i in range(len(galaxy_list)-1):
    compare = galaxy_list[0]
    galaxy_list.pop(0)
    for j in range(len(galaxy_list)):
        sum += calculate_distance(compare, galaxy_list[j])
            
print(sum)