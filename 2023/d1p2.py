input = "d1_input.txt"
sum_total = 0
line_sum = 0
first = True
current_digit = 0
first_digit = 0

test = "two1nine"
index = 0

def written_number_indices(text):
    min_index = len(text)
    left_num = "none"
    max_index = -1
    right_num = "none"
    written_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for number in written_numbers:
        start_index = text.find(number)
        if start_index != -1:

            if start_index < min_index:
                min_index = start_index
                left_num = number
            
            # Finding the start index of the last occurrence
            last_occurrence_start_index = text.rfind(number)
            if last_occurrence_start_index > max_index:
                max_index = last_occurrence_start_index
                right_num = number

    return [[left_num, min_index], [right_num, max_index]]

def word_to_text(word):
    if word == "one":
        return "1"
    if word == "two":
        return "2"
    if word == "three":
        return "3"
    if word == "four":
        return "4"
    if word == "five":
        return "5"
    if word == "six":
        return "6"
    if word == "seven":
        return "7"
    if word == "eight":
        return "8"
    if word == "nine":
        return "9"

with open(input, "r") as file:
    for line in file:  
        current_index = 0
        current_digit = 0
        first_digit = 0 
        min_max_written_numbers = written_number_indices(line)
        first_digit_text = word_to_text(min_max_written_numbers[0][0])
        last_digit_text = word_to_text(min_max_written_numbers[1][0])
        first_digit  = first_digit_text
        for index,char in enumerate(line):
            #print(first_digit, char)
            if char.isdigit():
                if first:
                    if index < min_max_written_numbers[0][1]:
                        first_digit = char
                        current_index = index
                        current_digit = char
                        first = False
                    else:
                        first_digit = first_digit_text
                        current_digit = char
                        current_index = index
                        first = False
                else:
                    current_digit = char
                    current_index = index
        print("max_index_Written",min_max_written_numbers[1][1])
        print("current_index", current_index)
        if current_index < min_max_written_numbers[1][1]:
            current_digit = last_digit_text
            current_index = min_max_written_numbers[1][1]
            #print(current_digit)
        #print(first_digit, current_digit)
        line_sum = int(str(first_digit) + str(current_digit))
        
        sum_total += line_sum
        line = line.rstrip()
        print(line_sum, ",", line)
        #print(sum_total)
        first = True
print("linesum:",sum_total)

