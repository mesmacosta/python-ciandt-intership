import unittest

from services import start_game, gess_word, reset_game, new_id, MAX_TIME
from unittest.mock import patch, MagicMock


class HangmanTest(unittest.TestCase):

    @patch("services.randint")
    def test_new_id_must_return_integer_value(self, mock_randint):
        mock_randint.return_value = 10000001
        id = new_id()
        self.assertEqual(id, 10000001)

    def test_new_game_with_no_id_should_not_start_and_should_return_400_code(self):
        self.assertEqual(start_game(_id=""), ({
                                                  'data': {
                                                      'status': 'invalid id'
                                                  }
                                              }, 400))

    @patch("repository.sessionmaker")
    @patch("time.asctime")
    @patch("time.time")
    @patch("services.choice")
    def test_new_game_must_start_and_return_values_correctly_shouldnt_show_word(self, mocking_choice,
                                                                                mocking_time, mocking_asc_time,
                                                                                mocking_session_maker):
        mocking_choice.return_value = "Alura"
        mocking_time.return_value = 1000
        mocking_asc_time.return_value = "10/11/1990"
        mocking_session_maker.return_value = MagicMock()
        new_game_create_test = start_game(18902)
        self.assertEqual(new_game_create_test,
                         ({
                              'game_id': 18902,
                              'data': {
                                  'id': 18902,
                                  'find': '_____',
                                  'tries': 0,
                                  'result': '',
                                  'time_sec': 1000,
                                  'date': '10/11/1990'
                              }
                          }, 200)
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_gess_word_is_a_correct_word(self, mocking_session_maker, mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='_____', tries=0, result='',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        gess_word_return = gess_word(31234, 'a')

        self.assertEqual(gess_word_return,
                         {
                              'game_id': 31234,
                              'data': {
                                  'find': 'a___a',
                                  'tries': 0,
                                  'result': '',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': None
                              }
                          }
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_gess_word_is_an_incorrect_word(self, mocking_session_maker, mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='_____', tries=0, result='',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        gess_word_return = gess_word(31234, 'b')

        self.assertEqual(gess_word_return,
                         {
                             'game_id': 31234,
                             'data': {
                                 'find': '_____',
                                 'tries': 1,
                                 'result': '',
                                 'time_sec': 3213213213,
                                 'date': '14/11/1990',
                                 'word': None
                             }
                         }
                         )


    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_gess_word_losing_game_must_return_lose_and_word(self, mocking_session_maker, mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='_____', tries=5, result='',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        gess_word_return = gess_word(31234, 'b')

        self.assertEqual(gess_word_return,
                         {
                             'game_id': 31234,
                             'data': {
                                 'find': '_____',
                                 'tries': 6,
                                 'result': 'lose',
                                 'time_sec': 3213213213,
                                 'date': '14/11/1990',
                                 'word': 'Alura'
                             }
                         }
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_gess_word_winning_game_should_return_word(self, mocking_session_maker, mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='Alu_a', tries=1, result='',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        gess_word_return = gess_word(31234, 'r')

        self.assertEqual(gess_word_return,
                         {
                             'game_id': 31234,
                             'data': {
                                 'find': 'Alura',
                                 'tries': 1,
                                 'result': 'win',
                                 'time_sec': 3213213213,
                                 'date': '14/11/1990',
                                 'word': 'Alura'
                             }
                         }
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_gess_word_winning_game_but_time_is_up_should_lose(self, mocking_session_maker, mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='Alu_a', tries=1, result='',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214 + MAX_TIME

        gess_word_return = gess_word(31234, 'r')

        self.assertEqual(gess_word_return,
                         {
                             'game_id': 31234,
                             'data': {
                                 'find': 'Alu_a',
                                 'tries': 1,
                                 'result': 'lose',
                                 'time_sec': 3213213213,
                                 'date': '14/11/1990',
                                 'word': 'Alura'
                             }
                         }
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_gess_word_winning_game_uppercase_letter_should_return_word(self, mocking_session_maker, mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='Alu_a', tries=1, result='',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        gess_word_return = gess_word(31234, 'R')

        self.assertEqual(gess_word_return,
                         {
                             'game_id': 31234,
                             'data': {
                                 'find': 'Alura',
                                 'tries': 1,
                                 'result': 'win',
                                 'time_sec': 3213213213,
                                 'date': '14/11/1990',
                                 'word': 'Alura'
                             }
                         }
                         )


class Game:
    id: str
    date: str
    find: str
    result: str
    time_sec: float
    tries: int
    word: str

    def __init__(self, _id, date, word, find, tries, result, time_sec):
        self.id = _id
        self.date = date
        self.word = word
        self.find = find
        self.tries = tries
        self.result = result
        self.time_sec = time_sec


if __name__ == "__main__":
    unittest.main()
