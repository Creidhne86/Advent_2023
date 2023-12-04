from collections import defaultdict

input = "d4_input.txt"
num_copies = defaultdict(int)
total_scratchcards = 0
card = 0
print(num_copies)
with open(input) as f:
    
    lines = f.readlines()
    for line in lines:
        card +=1
        split_input = line.split("|")
        winning_numbers = split_input[0].strip().split(":")[1].split()
        my_numbers = split_input[1].strip().split()
        
        #Finds how many matching numbers there are for a given card
        matching_numbers = 0
        for num in my_numbers:
            if num in winning_numbers:
                matching_numbers +=1
        copies_of_current_card = num_copies[f"card {card}"]

        for c in range(copies_of_current_card+1):
            for i in range(matching_numbers):
                num_copies[f"card {card+i+1}"] += 1
        
                
        print(f"card {card} has {matching_numbers} matching numbers.")
        print(num_copies)
    print(num_copies)
    total_scratchcards = sum(num_copies.values()) + card
    print(f"Total scratchcards: {total_scratchcards}")

