input = "d1_input.txt"

position = 0
floor  = 0
with open(input,"r") as f:
    for line in f:
        for c in line:
            position = position + 1
            if c == "(":
                floor += 1
            elif c == ")":
                floor -= 1

    print(floor)