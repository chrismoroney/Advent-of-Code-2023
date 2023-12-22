from collections import deque

def get_total(grid, length, not_in_loop):
    return len(grid) * len(grid[0]) - len(not_in_loop | length)

# Part 2 inspired by HyperNeutrino --  https://www.youtube.com/watch?v=r3i3XE9H4uw&t=1404s
def find_outside_components(grid):
    not_in_loop = set()

    for x, row in enumerate(grid):
        inside = False
        up = None
        for y, char in enumerate(row):
            if char == '|':
                inside = not inside
            elif char in 'LF':
                up = char == 'L'
            elif char in '7J':
                if char != ('J' if up else '7'):
                    inside = not inside
                up = None
            elif char == '.':
                pass
            
            if not inside:
                not_in_loop.add((x, y))
    return not_in_loop

# Part 2 inspired by HyperNeutrino --  https://www.youtube.com/watch?v=r3i3XE9H4uw&t=1404s
def find_loop_and_replace_s(start, grid):
    length = {start}
    queue = deque()
    queue.append(start)
    possible_s = {'J','L','7','F','|','-'}
    while queue:
        row, col = queue.popleft()
        char = grid[row][col]

        if row > 0 and char in '|JLS' and grid[row-1][col] in '|7F' and (row-1, col) not in length:
            valid_char_above = (row-1, col)
            length.add( valid_char_above )
            queue.append( valid_char_above )
            if char == 'S':
                possible_s &= {'|','J','L'}
        if row < len(grid)-1 and char in '|7FS' and grid[row+1][col] in '|JL' and (row+1, col) not in length:
            valid_char_below = (row+1, col)
            length.add( valid_char_below )
            queue.append( valid_char_below )
            if char == 'S':
                possible_s &= {'|','7','F'}
        if col > 0 and char in '-SJ7' and grid[row][col-1] in '-LF' and (row, col-1) not in length:
            valid_char_left = (row, col-1)
            length.add( valid_char_left )
            queue.append( valid_char_left )
            if char == 'S':
                possible_s &= {'-','J','7'}
        if col < len(grid[row])-1 and char in '-SLF' and grid[row][col+1] in '-J7' and (row, col+1) not in length:
            valid_char_right = (row, col+1)
            length.add( valid_char_right )
            queue.append( valid_char_right )
            if char == 'S':
                possible_s &= {'-','L','F'}

    actual_start_pipe = next(iter(possible_s))

    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if grid[x][y] == 'S':
                grid[x][y] = actual_start_pipe
            elif (x, y) not in length:
                grid[x][y] = '.'

    return length, grid


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
    length, grid = find_loop_and_replace_s(start, grid)
    not_in_loop = find_outside_components(grid)
    total = get_total(grid, length, not_in_loop)
    print(total)