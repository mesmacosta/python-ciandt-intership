def best_hands(hands):
    best_hands = []
    for hand in hands:
        if hand == "10♥ J♥ Q♥ K♥ A♥":
            best_hands.append(hand)
    pass


# check if the cards are from the same suit
def check_suit(hand):
    same_suit = True
    cards = hand.slipt()
    suit = cards[1][0]
    for card in cards:
        for i in range(1, 5):
            if card[i][0] != suit:
                same_suit = False
                break
        if not same_suit:
            break;
    return same_suit


# Check if the are four of a kind
def check_four_of_a_kind(hand):
    card_counter = 0
    for card_i in hand:
        for card_j in hand:
            if card_i == card_j:
                card_counter += 1
            if card_counter == 4:
                return True, card_i
        card_counter = 0
    return False, 0


def count_pairs(hand):
    cards = hand.slipt()
    counter = 0
    for i in range(0, 5):
        for j in range(i+1, 5):
            if cards[i] == cards[j]:
                counter += 1
    return counter


def check_triples(hand):
    cards = hand.slipt()
    counter = 0
    for i in range(0, 5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                if cards[i] == cards[j] & cards[j] == cards[k]:
                    counter += 1
                    return counter, cards[i]
    return counter, "0"


def check_straight(hand):
    hand.sort(key = lambda x: x.split())



def hand_atributes(hand):
    same_suit = check_suit(hand)
    num_pairs = count_pairs(hand)
    triples = check_triples(hand)
    four = check_four_of_a_kind(hand)
    straight
    Royal = True

    pass
