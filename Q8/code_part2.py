from math import gcd

def find_lcm(num_steps_in_cycle):
    lcm = num_steps_in_cycle.pop()
    for num in num_steps_in_cycle:
        lcm = lcm * num // gcd(lcm, num)
    return lcm

# Def inspired and recieved help from HyperNeutrino: https://www.youtube.com/watch?v=_nnxLcrwO_U
def count_steps_in_cycle(instruction, map_of_nodes, starting_nodes):
    all_cycles = []
    for node in starting_nodes:
        cycle = []
        current_steps = instruction
        step_count = 0
        first_z = None

        while True:
            while step_count == 0 or not node.endswith('Z'):
                step_count += 1
                if current_steps[0] == 'L':
                    node = map_of_nodes[node][0]
                else:
                    node = map_of_nodes[node][1]
                current_steps = current_steps[1:] + current_steps[0]

            cycle.append(step_count)
            if first_z is None:
                first_z = node
                step_count  = 0
            elif node == first_z:
                break
        all_cycles.append(cycle)
    
    return [cycle[0] for cycle in all_cycles]
            

def find_starting_nodes(map_of_nodes):
    starting_nodes = []
    for map in map_of_nodes:
        if map[2] == 'A':
            starting_nodes.append(map)
    return starting_nodes

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
    starting_nodes = find_starting_nodes(map_of_nodes)
    num_steps_in_cycle= count_steps_in_cycle(instruction, map_of_nodes, starting_nodes)
    lcm = find_lcm(num_steps_in_cycle)
    print(lcm)