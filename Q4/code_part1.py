def count_score(wins):
    if wins == 0:
        return 0
    else:
        return 2 ** (wins - 1)

def count_winning_nums(winning_nums, have_nums):
    wins = 0
    for i in have_nums:
        if i in winning_nums:
            wins += 1
    return wins

def process_ticket(game):
    parts = game.split('|')

    _, string_num = parts[0].split(':')
    _ = _.replace('Card', '').strip()

    winning_nums = {int(num): False for num in string_num.split()}
    have_nums = [int(num) for num in parts[1].split()]
    
    return winning_nums, have_nums


def parse_file(file_path):
    total_scores = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                winning_nums, have_nums = process_ticket(line)
                wins = count_winning_nums(winning_nums, have_nums)
                points = count_score(wins)
                total_scores += points
    except FileNotFoundError:
        print(f"file doesn't exist ", {file_path})
    return total_scores

if __name__ == "__main__":
    file_path = './input.txt'
    print(parse_file(file_path))
    