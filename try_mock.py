#import random
import unittest
from unittest.mock import patch

# importing function name
from test_mock import get_random_number_plus_one


class TestRandom(unittest.TestCase):
    # imoportent of mock is where is mock ?
    #@patch('__main__.random.randint')
    @patch('test_mock.random.randint')
    def test_it_should_get_4_when_random_get_3(self, mock):
        
        # Is working from up to low

        mock.return_value = 3
        result = get_random_number_plus_one()

        self.assertEqual(result, 4)

        # mock.assert_called_once_with(1, 10)
        
        # assert here

    def test_it_should_get_3(self):
        while True:
            result = get_random_number_plus_one()
            if result == 3 :
                break
        
        self.assertEqual(result, 3)

    



# def get_random_number_plus_one():
   
    # return random.randint(1, 10) + 1
     # randint => random int
# print(get_random_number_plus_one())
unittest.main()