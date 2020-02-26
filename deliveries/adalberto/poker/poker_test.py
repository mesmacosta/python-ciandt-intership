import unittest

from poker import best_hands

class PokerTest(unittest.TestCase):
    def test_single_hand_always_wins(self):
        self.assertEqual(best_hands(["4♠ 5♠ 7♥ 8♦ J♣"]), ["4♠ 5♠ 7♥ 8♦ J♣"])

    def test_highest_card_out_of_all_hands_wins(self):
        self.assertEqual(
            best_hands(["4♦ 5♠ 6♠ 8♦ 3♣", "2♠ 4♣ 7♠ 9♥ 10♥", "3♠ 4♠ 5♦ 6♥ J♥"]),
            ["3♠ 4♠ 5♦ 6♥ J♥"],
        )

    def test_a_tie_has_multiple_winners(self):
        self.assertEqual(
            best_hands(
                [
                    "4♦ 5♠ 6♠ 8♦ 3♣",
                    "2♠ 4♣ 7♠ 9♥ 10♥",
                    "3♠ 4♠ 5♦ 6♥ J♥",
                    "3♥ 4♥ 5♣ 6♣ J♦",
                ]
            ),
            ["3♠ 4♠ 5♦ 6♥ J♥", "3♥ 4♥ 5♣ 6♣ J♦"],
        )

    def test_multiple_hands_with_the_same_high_cards_tie_compares_next_highest_ranked_down_to_last_card(
        self
    ):
        self.assertEqual(
            best_hands(["3♠ 5♥ 6♠ 8♦ 7♥", "2♠ 5♦ 6♦ 8♣ 7♠"]), ["3♠ 5♥ 6♠ 8♦ 7♥"]
        )

    def test_one_pair_beats_high_card(self):
        self.assertEqual(
            best_hands(["4♠ 5♥ 6♣ 8♦ K♥", "2♠ 4♥ 6♠ 4♦ J♥"]), ["2♠ 4♥ 6♠ 4♦ J♥"]
        )

    def test_highest_pair_wins(self):
        self.assertEqual(
            best_hands(["4♠ 2♥ 6♠ 2♦ J♥", "2♠ 4♥ 6♣ 4♦ J♦"]), ["2♠ 4♥ 6♣ 4♦ J♦"]
        )

    def test_two_pairs_beats_one_pair(self):
        self.assertEqual(
            best_hands(["2♠ 8♥ 6♠ 8♦ J♥", "4♠ 5♥ 4♣ 8♣ 5♣"]), ["4♠ 5♥ 4♣ 8♣ 5♣"]
        )

    def test_both_hands_have_two_pairs_highest_ranked_pair_wins(self):
        self.assertEqual(
            best_hands(["2♠ 8♥ 2♦ 8♦ 3♥", "4♠ 5♥ 4♣ 8♠ 5♦"]), ["2♠ 8♥ 2♦ 8♦ 3♥"]
        )

    def test_both_hands_have_two_pairs_with_the_same_highest_ranked_pair_tie_goes_to_low_pair(self):
        self.assertEqual(
            best_hands(["2♠ Q♠ 2♣ Q♦ J♥", "J♦ Q♥ J♠ 8♦ Q♣"]), ["J♦ Q♥ J♠ 8♦ Q♣"]
        )

    def test_both_hands_have_two_identically_ranked_pairs_tie_goes_to_remaining_card_kicker(self):
        self.assertEqual(
            best_hands(["J♦ Q♥ J♠ 8♦ Q♣", "J♠ Q♠ J♣ 2♦ Q♦"]), ["J♦ Q♥ J♠ 8♦ Q♣"]
        )

    def test_three_of_a_kind_beats_two_pair(self):
        self.assertEqual(
            best_hands(["2♠ 8♥ 2♥ 8♦ J♥", "4♠ 5♥ 4♣ 8♠ 4♥"]), ["4♠ 5♥ 4♣ 8♠ 4♥"]
        )

    def test_both_hands_have_three_of_a_kind_tie_goes_to_highest_ranked_triplet(self):
        self.assertEqual(
            best_hands(["2♠ 2♥ 2♣ 8♦ J♥", "4♠ A♥ A♠ 8♣ A♦"]), ["4♠ A♥ A♠ 8♣ A♦"]
        )

    def test_with_multiple_decks_two_players_can_have_same_three_of_a_kind_ties_go_to_highest_remaining_cards(
        self
    ):
        self.assertEqual(
            best_hands(["4♠ A♥ A♠ 7♣ A♦", "4♠ A♥ A♠ 8♣ A♦"]), ["4♠ A♥ A♠ 8♣ A♦"]
        )

    def test_a_straight_beats_three_of_a_kind(self):
        self.assertEqual(
            best_hands(["4♠ 5♥ 4♣ 8♦ 4♥", "3♠ 4♦ 2♠ 6♦ 5♣"]), ["3♠ 4♦ 2♠ 6♦ 5♣"]
        )

    def test_aces_can_end_a_straight_10_j_q_k_a(self):
        self.assertEqual(
            best_hands(["4♠ 5♥ 4♣ 8♦ 4♥", "10♦ J♥ Q♠ K♦ A♣"]), ["10♦ J♥ Q♠ K♦ A♣"]
        )

    def test_aces_can_start_a_straight_a_2_3_4_5(self):
        self.assertEqual(
            best_hands(["4♠ 5♥ 4♣ 8♦ 4♥", "4♦ A♥ 3♠ 2♦ 5♣"]), ["4♦ A♥ 3♠ 2♦ 5♣"]
        )

    def test_both_hands_with_a_straight_tie_goes_to_highest_ranked_card(self):
        self.assertEqual(
            best_hands(["4♠ 6♣ 7♠ 8♦ 5♥", "5♠ 7♥ 8♠ 9♦ 6♥"]), ["5♠ 7♥ 8♠ 9♦ 6♥"]
        )

    def test_even_though_an_ace_is_usually_high_a_5_high_straight_is_the_lowest_scoring_straight(
        self
    ):
        self.assertEqual(
            best_hands(["2♥ 3♣ 4♦ 5♦ 6♥", "4♠ A♥ 3♠ 2♦ 5♥"]), ["2♥ 3♣ 4♦ 5♦ 6♥"]
        )

    def test_flush_beats_a_straight(self):
        self.assertEqual(
            best_hands(["4♣ 6♥ 7♦ 8♦ 5♥", "2♠ 4♠ 5♠ 6♠ 7♠"]), ["2♠ 4♠ 5♠ 6♠ 7♠"]
        )

    def test_both_hands_have_a_flush_tie_goes_to_high_card_down_to_the_last_one_if_necessary(
        self
    ):
        self.assertEqual(
            best_hands(["4♥ 7♥ 8♥ 9♥ 6♥", "2♠ 4♠ 5♠ 6♠ 7♠"]), ["4♥ 7♥ 8♥ 9♥ 6♥"]
        )

    def test_full_house_beats_a_flush(self):
        self.assertEqual(
            best_hands(["3♥ 6♥ 7♥ 8♥ 5♥", "4♠ 5♥ 4♣ 5♦ 4♥"]), ["4♠ 5♥ 4♣ 5♦ 4♥"]
        )

    def test_both_hands_have_a_full_house_tie_goes_to_highest_ranked_triplet(self):
        self.assertEqual(
            best_hands(["4♥ 4♠ 4♦ 9♠ 9♦", "5♥ 5♠ 5♦ 8♠ 8♦"]), ["5♥ 5♠ 5♦ 8♠ 8♦"]
        )

    def test_with_multiple_decks_both_hands_have_a_full_house_with_the_same_triplet_tie_goes_to_the_pair(
        self
    ):
        self.assertEqual(
            best_hands(["5♥ 5♠ 5♦ 9♠ 9♦", "5♥ 5♠ 5♦ 8♠ 8♦"]), ["5♥ 5♠ 5♦ 9♠ 9♦"]
        )

    def test_four_of_a_kind_beats_a_full_house(self):
        self.assertEqual(
            best_hands(["4♠ 5♥ 4♦ 5♦ 4♥", "3♠ 3♥ 2♠ 3♦ 3♣"]), ["3♠ 3♥ 2♠ 3♦ 3♣"]
        )

    def test_both_hands_have_four_of_a_kind_tie_goes_to_high_quad(self):
        self.assertEqual(
            best_hands(["2♠ 2♥ 2♣ 8♦ 2♦", "4♠ 5♥ 5♠ 5♦ 5♣"]), ["4♠ 5♥ 5♠ 5♦ 5♣"]
        )

    def test_with_multiple_decks_both_hands_with_identical_four_of_a_kind_tie_determined_by_kicker(
        self
    ):
        self.assertEqual(
            best_hands(["3♠ 3♥ 2♠ 3♦ 3♣", "3♠ 3♥ 4♠ 3♦ 3♣"]), ["3♠ 3♥ 4♠ 3♦ 3♣"]
        )

    def test_straight_flush_beats_four_of_a_kind(self):
        self.assertEqual(
            best_hands(["4♠ 5♥ 5♠ 5♦ 5♣", "7♠ 8♠ 9♠ 6♠ 10♠"]), ["7♠ 8♠ 9♠ 6♠ 10♠"]
        )

    def test_both_hands_have_straight_flush_tie_goes_to_highest_ranked_card(self):
        self.assertEqual(
            best_hands(["4♥ 6♥ 7♥ 8♥ 5♥", "5♠ 7♠ 8♠ 9♠ 6♠"]), ["5♠ 7♠ 8♠ 9♠ 6♠"]
        )


if __name__ == "__main__":
    unittest.main()
