def count_steps(instruction, map_of_nodes, num_steps, current):
    for char in instruction:
        if current == 'ZZZ':
            return num_steps
        else:
            num_steps += 1
            if char == 'L':
                current = map_of_nodes[current][0]
            else:
                current = map_of_nodes[current][1]
    return count_steps(instruction, map_of_nodes, num_steps, current)

def create_map_of_nodes(nodes):
    map_of_nodes = {}
    
    for node in nodes:
        split_string = node.split(' = ')
        split_vals = split_string[1].strip('()')
        left_and_right = split_vals.split(', ')
        l_and_r = tuple(vals.strip() for vals in left_and_right)

        map_of_nodes[split_string[0]] = l_and_r
        
    return map_of_nodes

def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)

        nodes = []
        instruction = ''

        for i in range(num_lines):
            if i == 0:
                instruction = lines[i].strip()
            elif i >= 2:
                nodes.append(lines[i].strip())

    return instruction, nodes

if __name__ == '__main__':
    instruction, nodes = parse_file('./input.txt')
    map_of_nodes = create_map_of_nodes(nodes)
    count_num_steps = count_steps(instruction, map_of_nodes, 0, 'AAA')
    print(count_num_steps)