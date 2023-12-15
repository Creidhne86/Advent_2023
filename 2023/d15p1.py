input = "d15_input.txt"
input = "d15_test.txt"

with open(input,"r") as f:
    data = f.read().split(",")

sum = 0
for line in data:
    line = line.strip()
    #print(line)
    value = 0
    for ch in line:
        ascii = ord(ch)
        #print(f"{ch} = {ascii}")
        value += ascii
        value = value*17
        value = value % 256
    sum += value    

print(sum)