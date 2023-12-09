def locate_symbols(matrix):
    matrix_rows = matrix.split('\n')
    symbols = {}
    not_symbols = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for row in range(len(matrix_rows)):
        for col in range(len(matrix_rows[row])):
            if matrix_rows[row][col] not in not_symbols:
                symbols[(row,col)] = matrix_rows[row][col]
    
    return symbols

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

def find_adjacent_numbers(symbols, nums):
    adjacent_numbers = []
    for (num, num_row, num_start_col, num_length) in nums:
        for (sym_row, sym_col), sym in symbols.items():
            if is_adjacent(num_row, num_start_col, num_length, sym_row, sym_col):
                adjacent_numbers.append(num)
                break
    return adjacent_numbers


def is_adjacent(num_row, num_start_col, num_length, sym_row, sym_col):
    # Check if symbol is horizontally adjacent
    if num_row == sym_row and (num_start_col - 1 <= sym_col <= num_start_col + num_length):
        return True
    # check is symbol is vertically adjacent
    if num_row - 1 <= sym_row <= num_row + 1 and (num_start_col - 1 <= sym_col <= num_start_col + num_length):
        return True
    # Check if the symbol is diagonal
    if sym_row == num_row - 1 or sym_row == num_row + 1:
        if num_start_col - 1 <= sym_col <= num_start_col + num_length:
            return True
        
    return False


def sum_adjacent_nums(nums):
    total = 0
    for num in nums:
        total += num

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
    symbols = locate_symbols(matrix)
    nums = locate_numbers(matrix)
    adjacent_to_symbol = find_adjacent_numbers(symbols, nums)
    total = sum_adjacent_nums(adjacent_to_symbol)
    print(total)