from collections import deque

def get_loop_length(loop):
    return int(len(loop) / 2)

def find_loop(start, grid):
    length = {start}

    queue = deque()
    queue.append(start)

    while queue:
        row, col = queue.popleft()
        char = grid[row][col]

        if row > 0 and char in '|JLS' and grid[row-1][col] in '|7F' and (row-1, col) not in length:
            valid_char_above = (row-1, col)
            length.add( valid_char_above )
            queue.append( valid_char_above )
        
        if row < len(grid)-1 and char in '|7FS' and grid[row+1][col] in '|JL' and (row+1, col) not in length:
            valid_char_below = (row+1, col)
            length.add( valid_char_below )
            queue.append( valid_char_below )

        if col > 0 and char in '-SJ7' and grid[row][col-1] in '-LF' and (row, col-1) not in length:
            valid_char_left = (row, col-1)
            length.add( valid_char_left )
            queue.append( valid_char_left )
        
        if col < len(grid[row])-1 and char in '-SLF' and grid[row][col+1] in '-J7' and (row, col+1) not in length:
            valid_char_right = (row, col+1)
            length.add( valid_char_right )
            queue.append( valid_char_right )
    
    return length

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
    grid = parse_file('./input.txt')
    start = find_start(grid)
    loop_coords = find_loop(start, grid)
    loop_length = get_loop_length(loop_coords)
    print(loop_length)