# Poker

>*After Grade School take this for fun!!*

Pick the best hand(s) from a list of poker hands among a list of hands.

Develop the best_hands(list_of_hadns) -> best_hand OR list_of_hands in case of draw.

## Deck: 52 Cards in 4 Suits: 
- Clubs:
    - 2♣ | 3♣ | 4♣ | 5♣ | 6♣ | 7♣ | 8♣ | 9♣ | 10♣ | J♣ | Q♣ | K♣ | A♣
- Diamonds:
    - 2♦ | 3♦ | 4♦ | 5♦ | 6♦ | 7♦ | 8♦ | 9♦ | 10♦ | J♦ | Q♦ | K♦ | A♦
- Hearts:
    - 2♥ | 3♥ | 4♥ | 5♥ | 6♥ | 7♥ | 8♥ | 9♥ | 10♥ | J♥ | Q♥ | K♥ | A♥
- Spades:
    - 2♠ | 3♠ | 4♠ | 5♠ | 6♠ | 7♠ | 8♠ | 9♠ | 10♠ | J♠ | Q♠ | K♠ | A♠

# Hands Rank

### Royal Flush: 10
    * 10♥ J♥ Q♥ K♥ A♥ | Nothing beats a Royal Flush. This is a straight flush from 10 to Ace.

### Straight Flush 9 
    * 9♠ 10♠ J♠ Q♠ K♠ | Second best hand. Just like straight with all cards same suit.

### Four of a Kind 8
    * A♣ A♦ A♥ A♠ A♣ | Four of the same cards. Completed with the highest card from table (kiker).

### Full House 7 
    * A♠ A♦ A♣ K♥ K♠ | Combo of three kind and one pair. The highest three of kind wins from other full houses.

### Flush 6
    * 2♥ 4♥ 6♥ 8♥ k♥ | Five cards of the same suit. Don't need to be in order. Highest card in the flushes wins.

### Straight 5 
    * 5♥ 6♣ 7♦ 8♠ 9♥ | Series of five cards in sequence but not the same suit. Aces can follow a king or start a straight before a two.

### Three of a Kind
    * A♠ A♦ A♣ 2♥ 7♠ | Three cards of the same suit. Completed with the two highest cards. 4
  
### Tow Pair
    * K♦ K♥ Q♣ Q♠ J♦ | Two sets of two cards of the same kind. Compled with the highest card. 3

### Pair
    * A♣ A♥ 9♠ 8♦ 6♣ | Two cards of the same cards with the three highest cards that are left avaliable. 2

### High Card
    A♥ 8♣ 6♦ 4♠ 2♥ | None of the above sequences just check the highest card. 1


## Running the tests

To run the tests, run `pytest poker_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest poker_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Incomplete Solutions

Create a folder with your name inside of 'deliveries' make copy of the challenge files and create your pull request to submit.
