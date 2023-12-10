import re

def find_nums(string):
    regex = r"(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"
    matches = re.findall(regex, string)
    print(matches)
    if not matches:
        return 0

    first, last = matches[0], matches[-1]

    num_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Convert words to numbers, if necessary
    first_num = first if first.isdigit() else num_map.get(first, '0')
    last_num = last if last.isdigit() else num_map.get(last, '0')

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
    file_path = './input_sample.txt'
    print(split_string(file_path))
    