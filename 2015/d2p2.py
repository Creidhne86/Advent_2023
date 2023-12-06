input ="d2_input.txt"

with open(input,"r") as f:
    total = 0
    for line in f:
        l = line.split("x")
        l = [int(i) for i in l]
        l.sort()
        #print(l)
        total += l[0]*l[1]*l[2] + 2*l[0] + 2*l[1]
    print(total)