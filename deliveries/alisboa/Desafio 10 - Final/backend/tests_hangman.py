import unittest

from services import start_game, gess_word, reset_game, new_id
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


if __name__ == "__main__":
    unittest.main()

# class MockedObject(object):
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __getitem__(self, key):
#         return self.__dict__[key]
