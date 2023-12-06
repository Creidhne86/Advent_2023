from collections import defaultdict

input = "d3_input.txt"

with open(input, "r") as file:
    grid = [line.strip() for line in file]

def has_adjacent_gear(grid, start_x, y, part_number_length):
    # Check adjacent cells for symbols for the entire part number
    adjacent_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(part_number_length):
        x = start_x + i
        for dx, dy in adjacent_offsets:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] in '*':
                #print("The gear is at:", nx, ny)
                return (nx, ny) #return nx, ny
    return None

sum = 0

def process_grid(grid):
    total_sum = 0
    part_number_digits = []
    gear_list = defaultdict(list)

    for y, line in enumerate(grid):
        part_number_ongoing = False
        for x, char in enumerate(line):
            if char.isdigit():
                part_number_digits.append(char)
                part_number_ongoing = True
            else:
                if part_number_ongoing:
                    # Check if the part number has an adjacent symbol
                    gear_test = has_adjacent_gear(grid, x - len(part_number_digits), y, len(part_number_digits))
                    if gear_test is not None:
                        gear_list[gear_test].append(int("".join(part_number_digits)))
                part_number_digits = []
                part_number_ongoing = False

        # Check for a part number at the end of the line
        if part_number_ongoing and has_adjacent_gear(grid, len(line) - len(part_number_digits), y, len(part_number_digits)):
            gear_list[has_adjacent_gear(grid, len(line) - len(part_number_digits), y, len(part_number_digits))].append(int("".join(part_number_digits)))
            part_number_digits = []
            part_number_ongoing = False

    print(gear_list)
    for key in gear_list:
        if len(gear_list[key]) == 2:
            total_sum += gear_list[key][0] * gear_list[key][1]
            print(f"Gear {key} has {gear_list[key][0]} and {gear_list[key][1]} with a total of {gear_list[key][0] * gear_list[key][1]}, and a sum total of {total_sum}")
            

    return total_sum



print(process_grid(grid))
