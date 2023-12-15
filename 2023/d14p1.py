import re

input = "d14_input.txt"
#input = "d14_test.txt"

with open(input,"r") as f:
    data = f.read().split("\n")
    for i in range(len(data)):
        data[i] = [*data[i]]

def shift_rocks(data,dir = "North"):
    if dir == "North" or dir == "South":
        str_dir = None
        if dir == "North": str_dir = "Left" 
        else: str_dir = "Right"
        zip_data = []
        shifted_zip_data = []
        unzipped_data = []
        for col in zip(*data):
            zip_data.append(list(col))
        for col in zip_data:
            shifted_zip_data.append(shift_row_or_column(col,str_dir))
        for col in zip(*shifted_zip_data):
            unzipped_data.append(list(col))
        return unzipped_data
    elif dir == "East" or dir == "West":
        str_dir = None
        shifted_data = []
        if dir == "East": str_dir = "Right" 
        else: str_dir = "Left"
        for row in data:
            shifted_data.append(shift_row_or_column(row,str_dir))
        return shifted_data
def split_keep_delimiters(s, delimiter='#'):
    # The regular expression: matches non-delimiter characters or delimiter characters
    pattern = f'([^{delimiter}]+|{delimiter}+)'
    return [part for part in re.split(pattern, s) if part]

def shift_row_or_column(data,dir = "Left"):
    #print(f"{data} {len(data)}")
    string_data = "".join(data)
    zeros_left = None
    if dir == "Left": zeros_left = True
    else: zeros_left = False 
    

    

    if "#" not in string_data:
        #print("no square rocks")
        return sorted(data,reverse = zeros_left)
    d = "#"
    split_data = split_keep_delimiters(string_data,d)
    new_list = []
    
    for i in range(len(split_data)):
        if split_data[i] == d:
            new_list.append(d)
        else:
            sorted_substring = sorted(split_data[i],reverse = zeros_left)
            for j in range(len(sorted_substring)):
                new_list.append(sorted_substring[j])

    return new_list

def calculate_load(data):
    sum = 0
    for i, row in enumerate(data):
        sum += row.count("O")*(len(data)-i)
        #print(f"row {len(data)-i} has {row.count('O')} rocks")
    return sum

def find_cycle(data, min_cycle_length=2, similarity_threshold=0.9):
    def is_similar(seq1, seq2, threshold):
        return sum(a == b for a, b in zip(seq1, seq2)) / len(seq1) >= threshold

    for cycle_length in range(min_cycle_length, len(data) // 2 + 1):
        cycle_found = True
        for i in range(0, len(data) - cycle_length, cycle_length):
            if not is_similar(data[i:i + cycle_length], data[i + cycle_length:i + 2 * cycle_length], similarity_threshold):
                cycle_found = False
                break
        if cycle_found:
            return data[:cycle_length]
    return None

# Main script
cycles = 1500
count = 0
new_data = data
data_buffer = []
buffer_size = 50  # Example size, adjust as needed

while count < cycles:
    direction_cycle = count % 4
    if direction_cycle == 0:
        load = calculate_load(new_data)
        print(f"{count//4 + 1}, {load}")
        data_buffer.append(load)
        if len(data_buffer) > buffer_size:
            data_buffer.pop(0)  # Maintain buffer size
        cycle = find_cycle(data_buffer)
        if cycle:
            print("Cycle detected")
            break
        direction = "North"
    elif direction_cycle == 1:
        direction = "West"
    elif direction_cycle == 2:
        direction = "South"
    elif direction_cycle == 3:
        direction = "East"
    count += 1
    new_data = shift_rocks(new_data, direction)





