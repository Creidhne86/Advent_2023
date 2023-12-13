input = "d12_input.txt"
#input = "d12_test.txt"

with open(input, "r") as f:
    data = f.read().splitlines()

for i in range(len(data)):
    data[i] = data[i].split()

def check_line(line):
    split_line = line[0].split(".")
    split_line = [x for x in split_line if x]
    
    line_calc = []
    for damaged_springs in split_line:
        line_calc.append(len(damaged_springs))

    line_sum = line[1].split(",")

    for i in range(len(line_sum)):
        line_sum[i] = int(line_sum[i])

    return line_calc == line_sum

def num_combinations(line):
    unknown_indices = [i for i, ltr in enumerate(line[0]) if ltr == "?"]
    
    split_line = [*line[0]]

    possible_combinations = pow(2,len(unknown_indices))
    sum = 0
    for i in range(possible_combinations):
        binary = bin(i)[2:]
        binary = "0"*(len(unknown_indices) - len(binary)) + binary
        

        #print(f"binary: {binary}")
        for j in range(len(unknown_indices)):
            value = ""
            if binary[j] == "0":
                value = "."
            else:
                value = "#"
            split_line[unknown_indices[j]] = value
        
        if check_line(["".join(split_line), line[1]]):
            sum += 1

    #print(split_line)
    
    return sum

#print(num_combinations(["???.###", "1,1,3"]))
total_sum = 0
for line in data:
    total_sum += num_combinations(line)


print(total_sum)
