import unittest
from services import MAX_TIME
from endpoints import new, start, handle_guess, reset
from unittest.mock import patch, MagicMock


class HangmanTest(unittest.TestCase):

    @patch("services.randint")
    def test_new_id_must_return_integer_value(self, mock_randint):
        mock_randint.return_value = 10000001
        response_id = new()
        self.assertEqual(response_id, ({'game_id': 10000001}, 200))

    def test_new_game_with_no_id_should_not_start_and_should_return_400_code(self):
        self.assertEqual(start(""), ({
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
        new_game_create_test = start(18902)
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

        handle_guess_response = handle_guess(31234, 'a')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': 'A___a',
                                  'tries': 0,
                                  'result': '',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': None
                              }
                          }, 200)
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_gess_word_is_a_correct_word_and_the_word_is_accentuated(self, mocking_session_maker, mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Gestão Financeira',
                            find='______ __________', tries=0, result='',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        handle_guess_response = handle_guess(31234, 'a')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': '____ã_ ___a_____a',
                                  'tries': 0,
                                  'result': '',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': None
                              }
                          }, 200)
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_gess_word_is_a_correct_word_and_the_gess_is_accentuated(self, mocking_session_maker, mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Gestão Financeira',
                            find='______ __________', tries=0, result='',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        handle_guess_response = handle_guess(31234, 'À')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': '____ã_ ___a_____a',
                                  'tries': 0,
                                  'result': '',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': None
                              }
                          }, 200)
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

        handle_guess_response = handle_guess(31234, 'b')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': '_____',
                                  'tries': 1,
                                  'result': '',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': None
                              }
                          }, 200)
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

        handle_guess_response = handle_guess(31234, 'b')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': '_____',
                                  'tries': 6,
                                  'result': 'lose',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': 'Alura'
                              }
                          }, 200)
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

        handle_guess_response = handle_guess(31234, 'r')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': 'Alura',
                                  'tries': 1,
                                  'result': 'win',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': 'Alura'
                              }
                          }, 200)
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

        handle_guess_response = handle_guess(31234, 'r')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': 'Alu_a',
                                  'tries': 1,
                                  'result': 'lose',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': 'Alura'
                              }
                          }, 200)
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

        handle_guess_response = handle_guess(31234, 'R')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': 'Alura',
                                  'tries': 1,
                                  'result': 'win',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': 'Alura'
                              }
                          }, 200)
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_game_already_won_if_a_new_incorrect_gess_word_is_passed_nothing_should_happen(self, mocking_session_maker,
                                                                                           mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='Alura', tries=1, result='win',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        handle_guess_response = handle_guess(31234, 'J')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': 'Alura',
                                  'tries': 1,
                                  'result': 'win',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': 'Alura'
                              }
                          }, 200)
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_game_already_won_if_a_new_correct_gess_word_is_passed_nothing_should_happen(self, mocking_session_maker,
                                                                                         mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='Alura', tries=1, result='win',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        handle_guess_response = handle_guess(31234, 'a')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': 'Alura',
                                  'tries': 1,
                                  'result': 'win',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': 'Alura'
                              }
                          }, 200)
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_game_already_lost_if_a_new_incorrect_gess_word_is_passed_nothing_should_happen(self, mocking_session_maker,
                                                                                            mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='Al__a', tries=6, result='lose',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        handle_guess_response = handle_guess(31234, 'J')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': 'Al__a',
                                  'tries': 6,
                                  'result': 'lose',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': 'Alura'
                              }
                          }, 200)
                         )

    @patch("time.time")
    @patch("repository.sessionmaker")
    def test_game_already_lost_if_a_new_correct_gess_word_is_passed_nothing_should_happen(self, mocking_session_maker,
                                                                                          mocking_time):
        mocking_session_maker.return_value = MagicMock()
        current_game = Game(_id=31234, date='14/11/1990', word='Alura',
                            find='Al__a', tries=6, result='lose',
                            time_sec=3213213213,
                            )
        mocking_session_maker()().query().filter().one.return_value = current_game
        mocking_time.return_value = 3213213214

        handle_guess_response = handle_guess(31234, 'u')

        self.assertEqual(handle_guess_response,
                         ({
                              'game_id': 31234,
                              'data': {
                                  'find': 'Al__a',
                                  'tries': 6,
                                  'result': 'lose',
                                  'time_sec': 3213213213,
                                  'date': '14/11/1990',
                                  'word': 'Alura'
                              }
                          }, 200)
                         )

    @patch("repository.sessionmaker")
    def test_reset_game_must_return_success_if_everything_is_ok(self, mocking_session_maker):
        mocking_session_maker.return_value = MagicMock()
        self.assertEqual(reset(325),
                         ({
                              'success': True
                          }, 200)
                         )

    @patch("repository.sessionmaker")
    def test_reset_game_must_return_not_success_if_everything_if_a_exception_happens(self, mocking_session_maker):
        mocking_session_maker.side_effect = MagicMock()
        mocking_session_maker()().query().filter().delete.side_effect = Exception("Test")
        self.assertEqual(reset(325),
                         ({
                              'success': False
                          }, 400)
                         )

    def test_gess_with_null_word_should_return_error(self):
        handle_guess_response = handle_guess(31234, None)

        self.assertEqual(handle_guess_response,
                         ({
                              'error': 'guess must not be null'
                          }, 400)
                         )

    def test_gess_being_a_string_with_lenght_greater_than_1_should_return_error(self):
        handle_guess_response = handle_guess(31234, 'abc')

        self.assertEqual(handle_guess_response,
                         ({
                              'error': 'guess must have 1 character'
                          }, 400)
                         )

    def test_gess_being_a_string_with_lenght_lesser_than_1_should_return_error(self):
        handle_guess_response = handle_guess(31234, '')

        self.assertEqual(handle_guess_response,
                         ({
                              'error': 'guess must have 1 character'
                          }, 400)
                         )

    def test_gess_having_null_id_should_return_error(self):
        handle_guess_response = handle_guess(None, 'a')

        self.assertEqual(handle_guess_response,
                         ({
                              'error': 'game_id should be passed'
                          }, 400)
                         )

    def test_gess_having_id_undefined_or_0_should_return_error(self):
        handle_guess_response = handle_guess(0, 'a')
        handle_guess_response2 = handle_guess('', 'a')
        self.assertEqual(handle_guess_response,
                         ({
                              'error': 'game_id should be passed'
                          }, 400)
                         )
        self.assertEqual(handle_guess_response2,
                         ({
                              'error': 'game_id should be passed'
                          }, 400)
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

"""
Instructions for viewing the coverage of the tests:

pip install coverage

coverage run -m unittest tests_hangman.py
coverage report --omit */venv/*

to get html page:
coverage html
"""
