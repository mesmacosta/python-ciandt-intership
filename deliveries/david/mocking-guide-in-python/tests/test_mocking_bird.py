from mocking.bird import Bird, DiamondRingException
from unittest import TestCase
from unittest.mock import patch

# What's missing:
#     The first test passes sometimes, other times it fails. The second
#     test has the same problem!  Make is so that both tests ALWAYS pass.


class TestMockingBird(TestCase):

    @patch('random.randint')
    def test_mocking_bird_when_sing_then_get_song(self, return_random_randint):

        # Arrange
        bird = Bird()
        return_random_randint.return_values = 2

        # Act
        result = bird.sing()

        # Assert
        assert result == "chirp chirp"

    @patch("random.randint")
    def test_mocking_bird_when_dont_sing_then_get_diamond_ring_exception(self, return_random_randint):
        # Arrange
        bird = Bird()
        return_random_randint.return_values = 1


        # Act
        # Assert
        self.assertRaises(DiamondRingException, bird.sing)
