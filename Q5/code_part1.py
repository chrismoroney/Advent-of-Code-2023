def find_min_locations(locations):
    return min(locations)

def find_location(seeds, mappings):
    locations = []
    for seed in seeds:
        current = seed
        for maps in mappings.values():
            for nums in maps:
                dest_start, src_start, rnge = nums[0], nums[1], nums[2]
                if src_start <= current and current < src_start + rnge:
                    current = dest_start + current - src_start
                    break
        locations.append(current)

    return locations

def generate_maps(contents):
    mappings = {}
    idx = -1
    maps_per_idx = []
    for line in contents:
        if 'map' not in line:
            m = line.split(' ')
            int_map = [int(num) for num in m]
            maps_per_idx.append(int_map)
        else:
            mappings[idx] = maps_per_idx
            idx += 1
            maps_per_idx = []
    mappings[idx] = maps_per_idx
    del mappings[-1]
    return mappings

def generate_seeds(contents):
    split_content = contents.split(' ')
    seeds = [int(num) for num in split_content[1:]]
    return seeds

def parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = [line for line in file.read().split('\n') if line]
            return contents
    except FileNotFoundError:
        print("File not found:", file_path)

if __name__ == '__main__':
    contents = parse_file('./input.txt')
    seeds = generate_seeds(contents[0])
    print(seeds)
    remains = contents[1:]
    mappings = generate_maps(remains)
    locations = find_location(seeds, mappings)
    min_loc = find_min_locations(locations)
    #print(min_loc)