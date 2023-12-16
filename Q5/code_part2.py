def find_min_locations(ranges):
    ranges = sorted(ranges)
    return min(ranges[0])

def find_location(seed_ranges, mappings):
    for key in sorted(mappings.keys()):
        map_ranges = mappings[key]
        new_seed_ranges = []
        while seed_ranges:
            start, end = seed_ranges.pop()
            for dest_start, src_start, rnge in map_ranges:
                os = max(start, src_start)
                oe = min(end, src_start + rnge)
                if os < oe:
                    new_seed_ranges.append((os - src_start + dest_start, oe - src_start + dest_start))
                    if os > start:
                        seed_ranges.append((start, os))
                    if end > oe:
                        seed_ranges.append((oe, end))
                    break
            else:
                new_seed_ranges.append((start, end))
        seed_ranges = new_seed_ranges
    return seed_ranges

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

def generate_seeds_ranges(contents):
    seeds_ranges = []
    split_content = contents.split(' ')[1:]
    for i in range(0, len(split_content), 2):
        start_range = int(split_content[i])
        end_range = int(start_range) + int(split_content[i+1])
        seeds_ranges.append((start_range, end_range))
    
    return seeds_ranges

def parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = [line for line in file.read().split('\n') if line]
            return contents
    except FileNotFoundError:
        print("File not found:", file_path)

if __name__ == '__main__':
    contents = parse_file('./input.txt')
    seeds_ranges = generate_seeds_ranges(contents[0])
    remains = contents[1:]
    mappings = generate_maps(remains)
    locations = find_location(seeds_ranges, mappings)
    min_loc = find_min_locations(locations)
    print(min_loc)
    