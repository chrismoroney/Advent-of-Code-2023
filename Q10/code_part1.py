def find_start(grid):
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == 'S':
                return (x, y)
    


def parse_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

if __name__ == '__main__':
    grid = parse_file('./input_sample_2.txt')
    start = find_start(grid)
    print(start)