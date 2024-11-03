import pytest
import unittest.mock
from unittest.mock import patch
from user_interface import UserInterface
from world_map import WorldMap


@patch('builtins.input', side_effect=['Tok', '1', 'Ber', '1'])
def test_take_user_input(mock_input):
    instance = UserInterface()
    world_map = WorldMap()
    world_map.load(".\\test\\resources\\worldcities_countries.csv")
    source, destination = instance.take_partial_user_input(world_map)
    expected_result = ('Japan,Tokyo', 'Germany,Berlin')
    assert expected_result == (source, destination)


# def test_take_user_input_2():
#     instance = UserInterface()
#     world_map = WorldMap()
#     world_map.load(".\\resources\\worldcities_countries.csv")
#     with unittest.mock.patch('builtins.input', return_value="Tok"):
#         instance.take_user_input_2(world_map)


# @patch('builtins.input', side_effect=['First', 'Second', 'Third'])
# def test_using_side_effect(mock_input):
#     calling_1 = mock_input()
#     calling_2 = mock_input()
#     calling_3 = mock_input()
#
#     assert calling_1 == 'First' and calling_2 == 'Second' and calling_3 == 'Third'


#
# def test_foo():
#     string = '1 United States,New York'
#     list_of_tokens = string.split(' ')
#     print(list_of_tokens)
#     final_string = ''
#     for index, token in enumerate(list_of_tokens):
#         if index == 0:
#             continue
#         print('token', token)
#         final_string = final_string + token + ' '
#     final_string = final_string.rstrip()
#     print(final_string)
#     assert final_string == 'United States,New York'
