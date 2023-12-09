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

def process(line):
    game_phases = line.split(';')
    if game_phases:
        game_phases[0] = game_phases[0].split(':', 1)[1].strip()
    games = line.split(':')[0].strip()
    game_num = games.split()[1]

    for phase in game_phases:
        colors = parse(phase)
        if check_invalid_game(colors):
            return 0
        
    return int(game_num)

def vals_from_file(file_path):
    total_score = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                total_score += process(line)
    except FileNotFoundError:
        print("File not found:", file_path)
    return total_score


if __name__ == '__main__':
    file_path = './input.txt'
    print(vals_from_file(file_path))
