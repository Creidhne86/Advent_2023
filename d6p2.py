input = "d6_test.txt"
times = []
distances = []

def distance_moved(race_time,acceleration_time):
    moving_time = race_time - acceleration_time
    speed = acceleration_time
    distance = moving_time * speed

    return distance

with open(input, "r") as file:
    data = file.read()
    times = data.split("\n")[0].split(": ")[1].strip().split()
    distances = data.split("\n")[1].split(": ")[1].strip().split()



margin = 1
for i in range(len(times)):
    ways_to_win = 0
    for j in range(int(times[i])):
        d = distance_moved(int(times[i]),j)
        if d > int(distances[i]):
            print(j)
            ways_to_win += 1
    print(ways_to_win)
    
    margin *= ways_to_win
print(margin)
