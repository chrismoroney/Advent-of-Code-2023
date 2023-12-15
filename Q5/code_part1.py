def find_location(seeds, maps):
    locations = []

    for seed in seeds:
        current = seed
        for m in maps:
            dest_start, src_start, rnge = m[0], m[1], m[2]
            if src_start <= current and current < src_start + rnge:
                current = dest_start + current - src_start
                break
        locations.append(current)

    return locations

def generate_maps(contents):
    mappings = []

    for line in contents:
        if 'map' not in line:
            m = line.split(' ')
            int_map = [int(num) for num in m]
            mappings.append(int_map)

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
    contents = parse_file('./input_sample.txt')
    seeds = generate_seeds(contents[0])
    remains = contents[1:]
    maps = generate_maps(remains)
    locations = find_location(seeds, maps)
    print(maps)