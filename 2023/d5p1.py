from collections import defaultdict

input = "d5_test.txt"

def get_seed_nums(input):
    with open(input) as f:
        seeds = []
        for line in f:
            if "seeds:" in line:
                seeds_str = line.split(":")[1].split()
                for num in seeds_str:
                  seeds.append(int(num))  
                return seeds

def map_converter(map_text):

    map_text = map_text.split("\n")
    map_text = [x.split(" ") for x in map_text]
    map_list = [[int(y) for y in x] for x in map_text]
    return map_list

def create_maps(input):
    input_start = False
    map = ""
    
    with open(input) as f:
        maps = defaultdict()
        map_text = ""
        for line in f:
            if line == "\n" and input_start == True:
                input_start = False
                #print(f"this is the current map text: \n{map_text.strip()}")
                maps[map_type] = map_converter(map_text.strip())
                map_text = ""
            if input_start == True:
                #print(line.strip())
                map_text += line
            if "map" in line:
                map_type = line.strip().split(":")[0]
                input_start = True
        maps[map_type] = map_converter(map_text.strip())
    return maps

def source_to_destination(source,map):
    destination = source
    for key in map:
        if key[1] <= source and key[1]+key[2] > source:
            destination = key[0] + source - key[1]

    return destination

map_dictionary = create_maps(input)
print(map_dictionary)

min_location = None
for seed in get_seed_nums(input):
    soil = source_to_destination(seed,map_dictionary["seed-to-soil map"])
    fertilizer = source_to_destination(soil,map_dictionary["soil-to-fertilizer map"])
    water = source_to_destination(fertilizer,map_dictionary["fertilizer-to-water map"])
    light = source_to_destination(water,map_dictionary["water-to-light map"])
    temperature = source_to_destination(light,map_dictionary["light-to-temperature map"])
    humidity = source_to_destination(temperature,map_dictionary["temperature-to-humidity map"])
    location = source_to_destination(humidity,map_dictionary["humidity-to-location map"])
    print(f"seed: {seed} -> soil: {soil} -> fertilizer: {fertilizer} -> water: {water} -> light: {light} -> temperature: {temperature} -> humidity: {humidity} -> location: {location}")
    if min_location == None:
        min_location = location
    elif location<min_location:
        min_location = location


print(min_location)


