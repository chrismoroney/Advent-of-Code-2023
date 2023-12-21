def get_next_val(list):
    if all(val == 0 for val in list):
        return 0
    
    list_of_diffs = [int(next_val) - int(val) for val, next_val in zip(list, list[1:])]
    next_diff = get_next_val(list_of_diffs)

    return int(list[-1]) + next_diff


def parse(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.split(' '))
    return lines

if __name__ == '__main__':
    contents = parse('./input.txt')
    total = 0
    for list in contents:
        total += get_next_val(list)
    print(total)
    