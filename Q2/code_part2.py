def parse(phase):
    colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    sections = phase.split(',')

    for section in sections:
        for color in colors.keys():
            if color in section:
                count = int(section.split()[0])
                colors[color] += count
    return colors

def check_invalid_game(colors, max_red=12, max_green=13, max_blue=14):
    return colors.get('red') > max_red or colors.get('green') > max_green or colors.get('blue') > max_blue

def check_min_cubes(min_colors, colors):
    for color in colors:
        min_colors[color] = max(min_colors.get(color), colors.get(color))

    return min_colors

def process(line):
    game_phases = line.split(';')
    if game_phases:
        game_phases[0] = game_phases[0].split(':', 1)[1].strip()
    games = line.split(':')[0].strip()
    game_num = games.split()[1]

    min_colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for phase in game_phases:
        colors = parse(phase)
        min_colors = check_min_cubes(min_colors, colors)
        
    power = 1
    for value in min_colors.values():
        power *= value
    return power

def vals_from_file(file_path):
    sum_of_powers = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                sum_of_powers += process(line)
    except FileNotFoundError:
        print("File not found:", file_path)
    return sum_of_powers


if __name__ == '__main__':
    file_path = './input.txt'
    print(vals_from_file(file_path))
