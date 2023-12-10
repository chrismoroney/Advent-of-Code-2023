def count_winning_nums(winning_nums, have_nums):
    wins = 0
    for i in have_nums:
        if i in winning_nums:
            wins += 1
    return wins

def process_ticket(game):
    parts = game.split('|')

    game_num, string_num = parts[0].split(':')
    game_num = int(game_num.replace('Card', '').strip())

    winning_nums = {int(num): False for num in string_num.split()}
    have_nums = [int(num) for num in parts[1].split()]
    
    return game_num, winning_nums, have_nums


def count_total_cards(card_map):
    total = 0
    for cards in card_map.values():
        total += cards
    return total

def parse_file(file_path):
    # create a map that tracks which card and how many of that card there are
    num_copies_of_cards = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                game_num, winning_nums, have_nums = process_ticket(line)
                wins = count_winning_nums(winning_nums, have_nums)

                num_copies_of_cards[game_num] = num_copies_of_cards.get(game_num, 0) + 1
                
                if wins != 0:
                    for i in range(1, wins + 1):
                        num_copies_of_cards[game_num+i] = num_copies_of_cards.get(game_num+i, 0) + num_copies_of_cards[game_num]
                
    except FileNotFoundError:
        print(f"file doesn't exist ", {file_path})
    
    total = count_total_cards(num_copies_of_cards)
    return total
    

if __name__ == "__main__":
    file_path = './input.txt'
    print(parse_file(file_path))
    