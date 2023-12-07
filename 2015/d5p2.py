input = "d5_input.txt"

nice_words = 0


with open(input, "r") as f:
    for line in f:
        constraint_1 = False
        constraint_2 = False
        for c in range(len(line)-2):
            if line[c] == line[c+2]:
                print(f"{line.strip()} contains repeating letter with one in between {line[c]}{line[c+1]}{line[c+2]}")
                constraint_1 = True
            pair = line[c]+line[c+1]
            #print(pair)
            if line.count(pair) >= 2:
                print(f"{pair} is repeated more than once")
                constraint_2 = True
        if constraint_1 and constraint_2:
            nice_words += 1
                
        

print(nice_words)