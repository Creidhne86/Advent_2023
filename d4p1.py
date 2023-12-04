input = "d4_input.txt"


card = 0
pile_score = 0
with open(input) as f:
    
    lines = f.readlines()
    for line in lines:
        card +=1
        split_input = line.split("|")
        winning_numbers = split_input[0].strip().split(":")[1].split()
        my_numbers = split_input[1].strip().split()
        
        score = 0
        for num in my_numbers:
            if num in winning_numbers:
                #print(f"{num} is a winning number")
                if score == 0:
                    score +=1
                else:
                    score = score * 2
        pile_score += score
        print(f"card {card} score: {score}") 
    print(f"Total score: {pile_score}")