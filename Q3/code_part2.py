def locate_gears(matrix):
    matrix_rows = matrix.split('\n')
    gears = {}
    
    for row in range(len(matrix_rows)):
        for col in range(len(matrix_rows[row])):
            if matrix_rows[row][col] == '*':
                # init num_of_adjacent_nums for each gear
                gears[(row,col)] = []
    
    return gears

def locate_numbers(matrix):
    matrix_rows = matrix.split('\n')
    nums = []

    for row_index, row in enumerate(matrix_rows):
        num = ""
        start_index = None
        for col_index, char in enumerate(row):
            if char.isdigit():
                if num == "":
                    start_index = col_index
                num += char
            elif num != "":
                # Append the number, starting position, and length
                nums.append((int(num), row_index, start_index, len(num)))
                num = ""
        # if we reach the end of the line and still have a number 
        if num != "":
            nums.append((int(num), row_index, start_index, len(num)))

    return nums

def find_adjacent_numbers(gears, nums):
    #adjacent_numbers = []
    for (num, num_row, num_start_col, num_length) in nums:
        for (gear_row, gear_col), gear in gears.items():
            if is_adjacent(num_row, num_start_col, num_length, gear_row, gear_col):
                #adjacent_numbers.append(num)
                gears[(gear_row, gear_col)].append(num)

    return gears


def is_adjacent(num_row, num_start_col, num_length, gear_row, gear_col):
    # Check if gear is horizontally adjacent
    if num_row == gear_row and (num_start_col - 1 <= gear_col <= num_start_col + num_length):
        return True
    # check is gear is vertically adjacent
    if num_row - 1 <= gear_row <= num_row + 1 and (num_start_col - 1 <= gear_col <= num_start_col + num_length):
        return True
    # Check if the gear is diagonal
    if gear_row == num_row - 1 or gear_row == num_row + 1:
        if num_start_col - 1 <= gear_col <= num_start_col + num_length:
            return True
        
    return False


def get_gear_ratios(gears):
    gear_ratio_list = []
    
    for list in gears.values():
        if len(list) == 2:
            gear_ratio_list.append(list[0] * list[1])

    return gear_ratio_list

def sum_all_ratios(ratios):
    total = 0

    for ratio in ratios:
        total += ratio

    return total

def parse_file(file_path):
    matrix = ""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                matrix += line
    except FileNotFoundError:
        print("File not found:", file_path)

    return matrix


if __name__ == '__main__':
    file_path = './input.txt'
    matrix = parse_file(file_path)
    gears = locate_gears(matrix)
    nums = locate_numbers(matrix)
    gears_with_adjacent_nums = find_adjacent_numbers(gears, nums)
    print(gears_with_adjacent_nums)
    gear_ratios = get_gear_ratios(gears_with_adjacent_nums)
    sum = sum_all_ratios(gear_ratios)
    print(sum)