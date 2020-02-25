from functools import cmp_to_key

card_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

card_values_sort = {
    'A': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    '10': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
}

card_values_winner = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    '10': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}


def best_hands(hands):
    hands_ranking = []
    for hand in hands:
        splitted_hand = split_hand_into_list(hand)
        splitted_hand = sort(splitted_hand)
        splitted_hand_numbers = hand_just_numbers(splitted_hand)
        splitted_hand_suits = hand_just_suits(splitted_hand)

        if is_straight_flush(splitted_hand_numbers, splitted_hand_suits):
            if splitted_hand_numbers[0] == 'A' and splitted_hand_numbers[4] == '5':
                # Menor straight flush
                rank_1 = 0
            else:
                biggest_cards_list = biggest_cards_ignoring_list(splitted_hand_numbers)
                rank_1 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 1]]
            hands_ranking.append({
                'hand': hand,
                'rank': 9,
                'rank_1': rank_1,
                'rank_2': 0,
                'rank_3': 0,
                'rank_4': 0,
                'rank_5': 0
            })
            continue
        four_of_a_kind = is_four_of_a_kind(splitted_hand_numbers)
        if four_of_a_kind:
            rank_1 = card_values_winner[four_of_a_kind]
            biggest_cards_list = biggest_cards_ignoring_list(splitted_hand_numbers, [four_of_a_kind])
            rank_2 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 1]]
            hands_ranking.append({
                'hand': hand,
                'rank': 8,
                'rank_1': rank_1,
                'rank_2': rank_2,
                'rank_3': 0,
                'rank_4': 0,
                'rank_5': 0
            })
            continue
        full_house_pair, full_house_three = is_full_house(splitted_hand_numbers)
        if full_house_three:
            rank_1 = card_values_winner[full_house_three]
            rank_2 = card_values_winner[full_house_pair]
            hands_ranking.append({
                'hand': hand,
                'rank': 7,
                'rank_1': rank_1,
                'rank_2': rank_2,
                'rank_3': 0,
                'rank_4': 0,
                'rank_5': 0
            })
            continue
        if is_flush(splitted_hand_suits):
            biggest_cards_list = biggest_cards_ignoring_list(splitted_hand_numbers)
            rank_1 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 1]]
            rank_2 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 2]]
            rank_3 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 3]]
            rank_4 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 4]]
            rank_5 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 5]]
            hands_ranking.append({
                'hand': hand,
                'rank': 6,
                'rank_1': rank_1,
                'rank_2': rank_2,
                'rank_3': rank_3,
                'rank_4': rank_4,
                'rank_5': rank_5
            })
            continue
        if is_straight(splitted_hand_numbers):
            if splitted_hand_numbers[0] == 'A' and splitted_hand_numbers[4] == '5':
                # Menor sequencia
                rank_1 = 0
            else:
                biggest_cards_list = biggest_cards_ignoring_list(splitted_hand_numbers)
                rank_1 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 1]]
            hands_ranking.append({
                'hand': hand,
                'rank': 5,
                'rank_1': rank_1,
                'rank_2': 0,
                'rank_3': 0,
                'rank_4': 0,
                'rank_5': 0
            })
            continue
        three_of_a_kind = is_three_of_a_kind(splitted_hand_numbers)
        if three_of_a_kind:
            rank_1 = card_values_winner[three_of_a_kind]
            biggest_cards_list = biggest_cards_ignoring_list(splitted_hand_numbers, [three_of_a_kind])
            rank_2 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 1]]
            rank_3 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 2]]
            hands_ranking.append({
                'hand': hand,
                'rank': 4,
                'rank_1': rank_1,
                'rank_2': rank_2,
                'rank_3': rank_3,
                'rank_4': 0,
                'rank_5': 0
            })
            continue
        tow_pairs = is_tow_pair(splitted_hand_numbers)
        if tow_pairs[0]:
            biggest_pairs_list = biggest_cards_ignoring_list(tow_pairs)
            rank_1 = card_values_winner[biggest_pairs_list[len(biggest_pairs_list) - 1]]
            rank_2 = card_values_winner[biggest_pairs_list[len(biggest_pairs_list) - 2]]
            biggest_cards_list = biggest_cards_ignoring_list(splitted_hand_numbers, biggest_pairs_list)
            rank_3 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 1]]
            hands_ranking.append({
                'hand': hand,
                'rank': 3,
                'rank_1': rank_1,
                'rank_2': rank_2,
                'rank_3': rank_3,
                'rank_4': 0,
                'rank_5': 0
            })
            continue
        pair = is_pair(splitted_hand_numbers)
        if pair:
            rank_1 = card_values_winner[pair]
            biggest_cards_list = biggest_cards_ignoring_list(splitted_hand_numbers, [pair])
            rank_2 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 1]]
            rank_3 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 2]]
            rank_4 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 3]]
            hands_ranking.append({
                'hand': hand,
                'rank': 2,
                'rank_1': rank_1,
                'rank_2': rank_2,
                'rank_3': rank_3,
                'rank_4': rank_4,
                'rank_5': 0
            })
            continue

        # High card
        biggest_cards_list = biggest_cards_ignoring_list(splitted_hand_numbers)
        rank_1 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 1]]
        rank_2 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 2]]
        rank_3 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 3]]
        rank_4 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 4]]
        rank_5 = card_values_winner[biggest_cards_list[len(biggest_cards_list) - 5]]
        hands_ranking.append({
            'hand': hand,
            'rank': 1,
            'rank_1': rank_1,
            'rank_2': rank_2,
            'rank_3': rank_3,
            'rank_4': rank_4,
            'rank_5': rank_5
        })

    return best_hands_given_ranked_list(sort_all_hands_already_ranked(hands_ranking))


def hand_just_numbers(hand):
    return [hand[0][0:len(hand[0]) - 1], hand[1][0:len(hand[1]) - 1],
            hand[2][0:len(hand[2]) - 1], hand[3][0:len(hand[3]) - 1], hand[4][0:len(hand[4]) - 1]]


def hand_just_suits(hand):
    return [hand[0][len(hand[0])-1], hand[1][len(hand[1])-1], hand[2][len(hand[2])-1],
            hand[3][len(hand[3])-1], hand[4][len(hand[4])-1]]


def split_hand_into_list(hand):
    return hand.split(' ')


def compare_cards_sort(card1, card2):
    if card_values_sort[card1[0:len(card1[0]) - 2]] > card_values_sort[card2[0:len(card2[0]) - 2]]:
        return 1
    elif card_values_sort[card1[0:len(card1[0]) - 2]] < card_values_sort[card2[0:len(card2[0]) - 2]]:
        return -1
    else:
        return 0


def sort(hand):
    return sorted(hand, key=cmp_to_key(compare_cards_sort))


def is_straight(hand):
    first_index_card_order = 0
    is_a = False
    for index_card in range(len(card_order)):
        if card_order[index_card] == hand[0]:
            first_index_card_order = index_card
            break
    if first_index_card_order == 0:
        if hand[1] == '10':
            is_a = True
            # Index 8 representa a carta 10
            first_index_card_order = 8

    index_card_order = first_index_card_order + 1
    index_hand = 1
    straight = True
    while index_card_order < first_index_card_order + 5:
        try:
            if index_hand == 5 and is_a:
                continue
            if hand[index_hand] != card_order[index_card_order]:
                straight = False
                break
        finally:
            index_card_order += 1
            index_hand += 1

    return straight


def is_flush(hand):
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return True
    else:
        return False


def is_three_of_a_kind(hand):
    card_counter = 0
    for card_i in hand:
        for card_j in hand:
            if card_i == card_j:
                card_counter += 1
            if card_counter == 3:
                return card_i
        card_counter = 0
    return False


def is_pair(hand, ignored_card=None):
    card_counter = 0
    # Used to check if the pair is not a three of a kind
    intern_iteration = 0
    for card_i in hand:
        for card_j in hand:
            if card_i == card_j:
                card_counter += 1
            if card_counter == 2 and intern_iteration == 4 and ignored_card != card_i:
                return card_i
            intern_iteration += 1
        intern_iteration = 0
        card_counter = 0
    return False


def is_straight_flush(hand_numbers, hand_suits):
    if is_flush(hand_suits) and is_straight(hand_numbers):
        return True
    else:
        return False


def is_four_of_a_kind(hand):
    card_counter = 0
    for card_i in hand:
        for card_j in hand:
            if card_i == card_j:
                card_counter += 1
            if card_counter == 4:
                return card_i
        card_counter = 0
    return False


def is_full_house(hand):
    pair = is_pair(hand)
    three_of_a_kind = is_three_of_a_kind(hand)
    if pair and three_of_a_kind:
        return pair, three_of_a_kind
    else:
        return False, False


def is_tow_pair(hand):
    first_pair = is_pair(hand)
    second_pair = is_pair(hand, first_pair)
    if first_pair and second_pair:
        return first_pair, second_pair
    return False, False


def compare_cards_biggest(card1, card2):
    if card_values_winner[card1] > card_values_winner[card2]:
        return 1
    elif card_values_winner[card1] < card_values_winner[card2]:
        return -1
    else:
        return 0


def sort_biggest(hand):
    return sorted(hand, key=cmp_to_key(compare_cards_biggest))


def biggest_cards_ignoring_list(hand, list_of_cards_to_ignore=None):
    sorted_biggest = sort_biggest(hand)
    if not list_of_cards_to_ignore:
        return sorted_biggest
    biggest_cards = []
    for card in sorted_biggest:
        if not(card in list_of_cards_to_ignore):
            biggest_cards.append(card)
    return biggest_cards


def sort_all_hands_already_ranked(hands_list):
    hands_list.sort(key=lambda d: d['rank_5'], reverse=True)
    hands_list.sort(key=lambda d: d['rank_4'], reverse=True)
    hands_list.sort(key=lambda d: d['rank_3'], reverse=True)
    hands_list.sort(key=lambda d: d['rank_2'], reverse=True)
    hands_list.sort(key=lambda d: d['rank_1'], reverse=True)
    hands_list.sort(key=lambda d: d['rank'], reverse=True)
    return hands_list


def best_hands_given_ranked_list(hands_list):
    winning_hands_list = []
    for hand in hands_list:
        if hands_list[0]['rank'] == hand['rank'] and hands_list[0]['rank_1'] == hand['rank_1'] and \
                hands_list[0]['rank_2'] == hand['rank_2'] and hands_list[0]['rank_3'] == hand['rank_3']\
                and hands_list[0]['rank_4'] == hand['rank_4'] and hands_list[0]['rank_5'] == hand['rank_5']:
            winning_hands_list.append(hand)
    return [hand['hand'] for hand in winning_hands_list]
