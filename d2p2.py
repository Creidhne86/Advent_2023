input = "d2_input.txt"

def min_cubes_game(game_text):
    max_red = 0
    max_blue = 0
    max_green = 0
    split_game = game_text.split(";")
    #print("test:",split_game)
    for r in range(len(split_game)):
        for i in range (len(split_game[r].split(","))):
            round = split_game[r].split(",")[i].strip().split(" ")
            if round[1] == "red" and int(round[0]) > max_red:
                max_red = int(round[0])
            if round[1] == "blue" and int(round[0]) > max_blue:
                max_blue = int(round[0])
            if round[1] == "green" and int(round[0]) > max_green:
                max_green = int(round[0])



    return [max_red, max_green, max_blue]

def cube_power(min_cubes):
    red = min_cubes[0]
    blue = min_cubes[1]
    green = min_cubes[2]
    
    return int(red)*int(blue)*int(green)

with open(input, "r") as file:
    sum = 0
    for n,game in enumerate(file):
        game = game.split(":")
        power = cube_power(min_cubes_game(game[1]))
        print("Cube Power of game",game[0],"is",power)
        sum+= power

print(sum)
