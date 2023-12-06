from collections import defaultdict

input = "d5_test.txt"

def preprocess_map(map_list):
    direct_map = {}
    for dest_start, src_start, length in map_list:
        for i in range(length):
            direct_map[src_start + i] = dest_start + i
    return direct_map

def combine_maps(maps):
    # Preprocess each map
    current_map = {}
    for key in ["seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map", 
                "water-to-light map", "light-to-temperature map", "temperature-to-humidity map", 
                "humidity-to-location map"]:
        next_map = preprocess_map(maps[key])
        if not current_map:
            current_map = next_map
        else:
            new_map = {}
            for src, dest in current_map.items():
                new_map[src] = next_map.get(dest, dest)
            current_map = new_map

    # Convert the final mapping to the required format
    seed_to_location_map = []
    for src, dest in sorted(current_map.items()):
        seed_to_location_map.append([dest, src, 1])  # Each mapping is a range of length 1

    return defaultdict(None, {'seed-to-location map': seed_to_location_map})

# Example usage

def source_to_destination(source,map):
    destination = source
    for key in map:
        if key[1] <= source and key[1]+key[2] > source:
            destination = key[0] + source - key[1]

    return destination


def get_seed_nums(input):
    with open(input) as f:
        seeds = []
        for line in f:
            if "seeds:" in line:
                seeds_str = line.split(":")[1].split()
                for num in seeds_str:
                  seeds.append(int(num))  
                return seeds

seeds = [79,14,55,13]

maps = defaultdict(None, {'seed-to-soil map': [[50, 98, 2], [52, 50, 48]], 
                          'soil-to-fertilizer map': [[0, 15, 37], [37, 52, 2], [39, 0, 15]], 
                          'fertilizer-to-water map': [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], 
                          'water-to-light map': [[88, 18, 7], [18, 25, 70]], 
                          'light-to-temperature map': [[45, 77, 23], [81, 45, 19], [68, 64, 13]], 
                          'temperature-to-humidity map': [[0, 69, 1], [1, 0, 69]], 
                          'humidity-to-location map': [[60, 56, 37], [56, 93, 4]]})

combined_map = combine_maps(maps)
print(combined_map)

seeds = get_seed_nums(input)
for seed in seeds:
    location = source_to_destination(seed, combined_map["seed-to-location map"])
    print(location)


