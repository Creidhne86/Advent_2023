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
min_acceleration_time = 0
for i in range(len(times)):
    ways_to_win = 0
    for j in range(int(times[i])):
        d = distance_moved(int(times[i]),j)
        if d > int(distances[i]):
            print(f"race time:{times[i]} acceleration time: {j} distance {d}")
            min_acceleration_time = j
            break
max_acceleration_time = 0
i = 1
while True:
    a = int(times[0]) - i
    d = distance_moved (int(times[0]),a)
    if d > int(distances[0]):
        print(f"race time:{times[0]} acceleration time: {a} distance {d}")
        max_acceleration_time = a
        break
    i += 1



print(min_acceleration_time)
print(max_acceleration_time)
print(f"total ways to win the race: {max_acceleration_time - min_acceleration_time}")
