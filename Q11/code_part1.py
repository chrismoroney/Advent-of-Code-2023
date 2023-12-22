def sum_of_distances(distances):
    total = 0
    for distance in distances:
        total += distance
    return total

def find_all_distances(empty_rows, empty_cols, galaxies):
    distances = []
    
    for i, (x1, y1) in enumerate(galaxies):
        for (x2, y2) in galaxies[:i]:
            row_steps = 0
            col_steps = 0
            for row_dist in range(min(x1, x2), max(x1, x2)):
                if row_dist in empty_rows:
                    row_steps += 2
                else:
                    row_steps += 1
            for col_dist in range(min(y1, y2), max(y1, y2)):
                if col_dist in empty_cols:
                    col_steps += 2
                else:
                    col_steps += 1
            distances.append(row_steps+col_steps)

    return distances

def find_all_galaxies(input):
    galaxies = []

    for x, row in enumerate(input):
        for y, col in enumerate(row):
            if input[x][y] == '#':
                galaxies.append((x, y))
    
    return galaxies

def find_empty_rows_cols(input):
    empty_rows = []
    empty_cols = []

    for row_num, row in enumerate(input):
        row_empty = True
        for char in row:
            if char != '.':
                row_empty = False
                break
        if row_empty:
            empty_rows.append(row_num)

    for col_num, col in enumerate(zip(*input)):
        col_empty = True
        for char in col:
            if char != '.':
                col_empty = False
                break
        if col_empty:
            empty_cols.append(col_num)

    return empty_rows, empty_cols


def parse_file(file_path):
    input = []
    with open(file_path, 'r') as file:
        for line in file:
            input.append(list(line.strip()))
    return input

if __name__ == '__main__':
    input = parse_file('./input.txt')
    empty_rows, empty_cols = find_empty_rows_cols(input)
    galaxies = find_all_galaxies(input)
    distances = find_all_distances(empty_rows, empty_cols, galaxies)
    total = sum_of_distances(distances)
    print(total)