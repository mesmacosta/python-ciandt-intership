from mocking.me import via_gif
from unittest import TestCase
from unittest.mock import patch

# What's missing:
#   Testing an external API can be done without mocking, but it only
#   works if the API is available.  In addition, tests may be slow and
#   running tests too often may exceed API query thresholds.
#
#   Update the tests so that they do not query the external API


class TestMockingMe(TestCase):

    @patch("requests.post")
    def test_mocking_me_via_gif_when_resp_200_then_get_gif(self, mock_requests):
        # Arrange
        name = 'First Last'

        mock_requests = MockedObject()
        mock_requests.content = "gif content"
        mock_requests.status_code = 200
        mock_requests.return_value = mock_requests

        # Act
        result = via_gif(name)

        # Assert
        assert result == "gif content"

    # TODO patch here
    def test_mocking_me_via_gif_when_resp_not_200_then_Exception(self):
        # Arrange
        name = 'First Last'
        # TODO set patch object's return value(s)

        mock_request_response = MockedObject()
        mock_request_response.status_code = 201

        # Act
        # Assert
        self.assertRaises(Exception, via_gif, name)

class MockedObject(object):

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]
