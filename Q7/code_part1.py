def get_total_score(rank_hands_in_groups):
    total_score = 0
    for i in range(1, len(rank_hands_in_groups) + 1):
        hand = rank_hands_in_groups[i]
        total_score += i * int(hand[1])

    return total_score

def card_value_to_rank(card):
    card_rank_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return card_rank_map[card]

def sort_hands_in_group(hands):
    def hand_rank(hand):
        return tuple(card_value_to_rank(card) for card in hand[0])
    return sorted(hands, key=hand_rank)

def rank_hands(map_of_hands):
    weakest_to_strongest_hands = [
        'high_card', 'one_pair', 'two_pair', 'three_of_kind', 'full_house', 'four_of_a_kind', 'five_of_a_kind'
    ]

    ranks_all_hands = {}
    rank = 1

    for group in weakest_to_strongest_hands:
        hands_in_group = map_of_hands[group]
        sorted_hands_in_group = sort_hands_in_group(hands_in_group)
        for hand in sorted_hands_in_group:
            ranks_all_hands[rank] = hand
            rank += 1

    return ranks_all_hands

def classify_hands(hands_and_bids):
    map_of_hands = {
        'five_of_a_kind': [],
        'four_of_a_kind': [],
        'full_house': [],
        'three_of_kind': [],
        'two_pair': [],
        'one_pair': [],
        'high_card' : []
    }

    for hand in hands_and_bids:
        hand_contents = {}
        for char in hand[0]:
            if char in hand_contents:
                hand_contents[char] += 1
            else:
                hand_contents[char] = 1

        is_two_pair = sum(1 for occ in hand_contents.values() if occ == 2) == 2
        inserted_into_list = False

        if 5 in hand_contents.values() and not inserted_into_list:
            map_of_hands['five_of_a_kind'].append(hand)
            inserted_into_list = True
        elif 4 in hand_contents.values() and not inserted_into_list:
            map_of_hands['four_of_a_kind'].append(hand)
            inserted_into_list = True
        elif 3 in hand_contents.values() and 2 in hand_contents.values() and not inserted_into_list:
            map_of_hands['full_house'].append(hand)
            inserted_into_list = True
        elif 3 in hand_contents.values() and 2 not in hand_contents.values() and not inserted_into_list:
            map_of_hands['three_of_kind'].append(hand)
            inserted_into_list = True
        elif is_two_pair and not inserted_into_list:
            map_of_hands['two_pair'].append(hand)
            inserted_into_list = True
        elif 2 in hand_contents.values() and not is_two_pair and not inserted_into_list:
            map_of_hands['one_pair'].append(hand)
            inserted_into_list = True
        else:
            map_of_hands['high_card'].append(hand)
            inserted_into_list = True

    return map_of_hands
    

def parse_file(file_path):
    processed_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            contents = tuple(line.split())
            processed_lines.append(contents)

    return processed_lines

if __name__ == '__main__':
    hands_and_bids = parse_file('./input.txt')
    map_of_hands = classify_hands(hands_and_bids)
    rank_hands_in_groups = rank_hands(map_of_hands)
    total_score = get_total_score(rank_hands_in_groups)
    print(total_score)