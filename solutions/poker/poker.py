
def best_hands(hands):
    cardHands = sorted([CardHand(hand) for hand in hands])
    return [c.hand for c in cardHands
            if cardHands[-1].rank_hand == c.rank_hand
            and cardHands[-1].count_tuple == c.count_tuple]


class CardHand():
    card_rank = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    rank_score = [
        'High card',
        'One pair',
        'Two pair',
        'Three of a kind',
        'Straight',
        'Flush',
        'Full house',
        'Four of a kind',
        'Straight flush'
    ]

    def __init__(self, hand):
        self.hand = hand
        self.values_suites = list(
            zip(*[(card[0:-1], card[-1]) for card in hand.split()]))
        
        hand_vals = self.values_suites[0]
        hand_suites = self.values_suites[1]

        self.value_count = dict((value, hand_vals.count(value))
                                for value in hand_vals)
        self.count_tuple = sorted([(self.card_rank[key], self.value_count[key])
                                for key in self.value_count],key=lambda tup:(-tup[1], -tup[0]))# sort!
        self.suite_count = dict((suite, hand_suites.count(suite))
                                for suite in hand_suites)
        self.rank_hand = self.rank_values()

    def rank_values(self):
        high_count = self.count_tuple[0][1]
        unique_count = len(self.value_count)
        if unique_count == 4:  # check pair
            return self.rank_score.index('One pair')
        elif unique_count == 3:  # check two pair or three of a kind,
            return (self.rank_score.index('Two pair')
                    if high_count == 2
                    else self.rank_score.index('Three of a kind'))
        elif unique_count == 2:  # check full house or four of a kind
            return (self.rank_score.index('Four of a kind')
                    if high_count == 4
                    else self.rank_score.index('Full house'))
        elif unique_count == 5:  # check one high card, flush or stright
            if self.straight():
                if self.flush():
                    return self.rank_score.index('Straight flush')
                return self.rank_score.index('Straight')
            elif self.flush():
                return self.rank_score.index('Flush')
            else:
                return self.rank_score.index('High card')
            pass
        else:
            raise ValueError(
                'Some one has been cheating with this deck of cards')

    def straight(self):
        lowCard = self.count_tuple[-1][0]
        highCard = self.count_tuple[0][0]
        # First check special case with low ace straight
        if (highCard == 14 and lowCard == 2 and self.count_tuple[1][0]-lowCard == 3):
            self.count_tuple.append(self.count_tuple.pop(0)) # in this case the Ace is lowest ranked in straight
            return True
        else:
            return (highCard - lowCard == 4)
        
    def flush(self):
        return len(self.suite_count) == 1

    def __eq__(self, other):
        return ((self.rank_hand, self.count_tuple) ==
                (other.rank_hand, other.count_tuple))

    def __lt__(self, other):
        return ((self.rank_hand, self.count_tuple) <
                (other.rank_hand, other.count_tuple))
