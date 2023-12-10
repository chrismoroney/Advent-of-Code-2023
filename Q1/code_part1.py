def find_nums(string):
    first_num = ''
    last_num = ''

    for char in string:
        if char.isdigit():
            first_num = char
            break
    for char in reversed(string):
        if char.isdigit():
            last_num = char
            break
    # Concatenate the numbers as strings and then convert to integer
    combined_num = first_num + last_num
    return int(combined_num)

def split_string(file_path):
    total_sum = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                total_sum += find_nums(line)
    except FileNotFoundError:
        print("File not found:", file_path)
    return total_sum

if __name__ == '__main__':
    file_path = './input.txt'
    print(split_string(file_path))
    