
input = "d11_test.txt"
#input = "d11_input.txt"
data = []


def find_galaxies(galaxy):
    galaxies = []
    for r, row in enumerate(galaxy):
        for c, char in enumerate(row):
            if char == "#":
                galaxies.append((r,c))
    return galaxies

def expand_galaxy(galaxy):
    expanded_galaxy = []
    
    
    for r, row in enumerate(galaxy):
        found_galaxy = False
        for c, char in enumerate(row):
            if char == "#":
                found_galaxy = True
                break
        expanded_galaxy.append(row)
        if not found_galaxy:
            expanded_galaxy.append(row)
    
    expanded_galaxy_col = []
    for c, col in enumerate(zip(*expanded_galaxy)):
        found_galaxy = False
        for r, char in enumerate(col):
            if char == "#":
                found_galaxy = True
                break
        expanded_galaxy_col.append(col)
        if not found_galaxy:
            expanded_galaxy_col.append(col)
    
    final_galaxy = []
    for row in zip(*expanded_galaxy_col):
        final_galaxy.append(list(row))

    return final_galaxy
def calculate_distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

with open(input,"r") as f:
    data = f.read().split("\n")
    for i, line in enumerate(data):
        line = [*line]
        data[i] = line

#for line in data:
#    print(''.join(line))

expanded_galaxy = expand_galaxy(data)

print("Expanded galaxy:")
for line in expanded_galaxy:
    print(''.join(line))

galaxy_list = find_galaxies(expanded_galaxy)


print(galaxy_list)

sum = 0

for i in range(len(galaxy_list)-1):
    compare = galaxy_list[0]
    galaxy_list.pop(0)
    for j in range(len(galaxy_list)):
        sum += calculate_distance(compare, galaxy_list[j])
            
print(sum)