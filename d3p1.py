input = "d3p1_input.txt"

with open(input, "r") as file:
    grid = [line.strip() for line in file]

def has_adjacent_symbol(grid, start_x, y, part_number_length):
    # Check adjacent cells for symbols for the entire part number
    adjacent_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(part_number_length):
        x = start_x + i
        for dx, dy in adjacent_offsets:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] not in '0123456789.':
                return True
    return False

sum = 0

def process_grid(grid):
    total_sum = 0
    part_number_digits = []

    for y, line in enumerate(grid):
        part_number_ongoing = False
        for x, char in enumerate(line):
            if char.isdigit():
                part_number_digits.append(char)
                part_number_ongoing = True
            else:
                if part_number_ongoing:
                    # Check if the part number has an adjacent symbol
                    if has_adjacent_symbol(grid, x - len(part_number_digits), y, len(part_number_digits)):
                        total_sum += int("".join(part_number_digits))
                part_number_digits = []
                part_number_ongoing = False

        # Check for a part number at the end of the line
        if part_number_ongoing and has_adjacent_symbol(grid, len(line) - len(part_number_digits), y, len(part_number_digits)):
            total_sum += int("".join(part_number_digits))
            part_number_digits = []
            part_number_ongoing = False

    return total_sum



print(process_grid(grid))
