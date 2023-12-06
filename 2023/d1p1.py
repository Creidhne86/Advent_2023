input = "d1_input.txt"
sum_total = 0
line_sum = 0
first = True
current_digit = 0
first_digit = 0

with open(input, "r") as file:
    for line in file:       
        for char in line:
            if char.isdigit():
                if first:
                    first_digit =char
                    current_digit = char
                    first = False
                else:
                    current_digit = char
        line_sum = int(first_digit + current_digit)
        sum_total += line_sum
        first = True
        print(line_sum)
print(sum_total)

