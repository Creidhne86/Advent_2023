input = "d2_input.txt"


def is_valid_pull(num,color):
    max_red = 12
    max_green = 13
    max_blue = 14
    
    if color == "red" and int(num) > max_red:
        return False
    if color == "green" and int(num) > max_green:
        return False
    if color == "blue" and int(num) > max_blue:
        return False
    return True

def is_valid_round(round_list):
    for i in range (len(round_list)):
        round = round_list[i].strip().split(" ")
        if not is_valid_pull(round[0],round[1]):
            return False
    return True
    

def is_valid_game(game_text):
    #print(game_text[1])
    split_game = game_text.split(";")
    for r in range(len(split_game)):
        round = split_game[r].split(",")
        if not is_valid_round(round):
            return False

    return True

with open(input, "r") as file:
    sum = 0
    for n,game in enumerate(file):
        game = game.split(":")
        if is_valid_game(game[1]):
            print(game[0],"is a valid game")
            sum+= n+1


print(sum)