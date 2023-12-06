input = "d1_input.txt"
sum_total = 0
line_sum = 0
first = True
current_digit = 0
first_digit = 0

def parse_string_text_to_number(text):
    replaced_text = text.replace("one", "o1e")
    replaced_text = replaced_text.replace("two", "t2o")
    replaced_text = replaced_text.replace("three", "th3ee")
    replaced_text = replaced_text.replace("four", "fo4r")
    replaced_text = replaced_text.replace("five", "fi5e")
    replaced_text = replaced_text.replace("six", "s6x")
    replaced_text = replaced_text.replace("seven", "se7en")
    replaced_text = replaced_text.replace("eight", "ei8ht")
    replaced_text = replaced_text.replace("nine", "ni9e")
    return replaced_text

with open(input, "r") as file:
    for line in file:       
        parsed_line = parse_string_text_to_number(line)
        line = parsed_line
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

