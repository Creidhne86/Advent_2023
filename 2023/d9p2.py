input = "d9_test.txt"

with open(input,"r") as f:
    lines = f.read().split("\n")
    for i in range(len(lines)):
        lines[i]=lines[i].split()
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
def difference_at_step(analysis):
    difference = []
    for i in range(len(analysis)-1):
        difference.append(analysis[i+1]-analysis[i])
    return difference


sum = 0
for line in lines:
    #print(line)
    h = []
    h.append(line)
    difference = difference_at_step(line)
    h.append(difference)
    while not all([val == 0 for val in difference]):
        difference = difference_at_step(difference)
        h.append(difference)
    print("newline")
    for i in range(len(h)-1):
        #print(f"{h[len(h)-i-2]}")
        h[len(h)-i-2].insert(0,h[len(h)-i-2][0]-h[len(h)-i-1][0])
    print(h)
    sum += h[0][0]



print(sum)

    
    
    

