def sum_all_vals(list_of_vals):
    return sum(val for val in list_of_vals)

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
    contents = parse('./input_sample.txt')
    list_of_vals = []
    for list in contents:
        list_of_vals.append(get_next_val(list))
    total = sum_all_vals(list_of_vals)
    print(total)
    