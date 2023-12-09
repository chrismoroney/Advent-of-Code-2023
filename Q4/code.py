def process_ticket(game):
    parts = game.split('|')
    if parts:
        parts[0] = parts[0].split(':')[1].strip()
    print(parts)


def parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                process_ticket(line)
    except FileNotFoundError:
        print(f"file doesn't exist ", {file_path})

if __name__ == "__main__":
    file_path = './input_sample.txt'
    parse_file(file_path)