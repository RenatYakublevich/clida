from typing import List, Dict
import math
import string

from clida.exceptions import WrongValueType


class Visualizer:
    _PLUS = '+'
    _DASH = '-'
    _VERTICAL = '|'
    _BLANK = ' '
    _ALL_FONTS = {
        'bold': {
            'head_letter': ['▄▀█','█▄▄','█▀▀','█▀▄','█▀▀','█▀▀','█▀▀','█ █','█','  █','█▄▀','█  ','█▀▄▀█','█▄ █','█▀█','█▀█','█▀█','█▀█','█▀','▀█▀','█ █','█ █','█ █ █','▀▄▀','█▄█','▀█',' '],
            'body_letter': ['█▀█','█▄█','█▄▄','█▄▀','██▄','█▀ ' ,'█▄█','█▀█','█','█▄█','█ █','█▄▄','█ ▀ █','█ ▀█','█▄█','█▀▀','▀▀█','█▀▄','▄█',' █ ','█▄█','▀▄▀','▀▄▀▄▀','█ █',' █ ','█▄',' ']
        }
    }
    _ALPHABET = string.ascii_lowercase + ' '

    @classmethod        
    def visualize_dict(cls, dictionary: Dict):
        if not isinstance(dictionary, dict):
            raise WrongValueType('Expected list')

        max_line_length = {
            'key': 0,
            'value': 0
        }
        for key,value in dictionary.items():
            max_line_length = {'key': len(str(key)), 'value': len(str(value))} if len(str(key) + str(value)) > max_line_length['key'] + max_line_length['value'] else max_line_length

        for key,value in dictionary.items():
            key, value = str(key), str(value)
            blanks_key = lambda size_line: int((max_line_length['key'] + 2 - size_line) / 2) * cls._BLANK
            blanks_value = lambda size_line: int((max_line_length['value'] + 2 - size_line) / 2) * cls._BLANK

            print(cls._PLUS + cls._DASH * (max_line_length['key'] + 2) + cls._PLUS + cls._DASH * (max_line_length['value'] + 2) + cls._PLUS)
            print(cls._VERTICAL + blanks_key(len(key)) + key + blanks_key(len(key)) + cls._VERTICAL + blanks_value(len(value)) + value + blanks_value(len(value)) + cls._VERTICAL)
    
    @classmethod
    def visualize_list(cls, array: List, horizontal=False):
        if not isinstance(array, list):
            raise WrongValueType('Expected list')
        if not horizontal:
            for element in array:
                element = str(element)
                print(cls._PLUS + cls._DASH * (len(element) + 2) + cls._PLUS)
                print(cls._VERTICAL + cls._BLANK + element + cls._BLANK + cls._VERTICAL)
            print(cls._PLUS + cls._DASH * (len(element) + 2) + cls._PLUS)
        elif horizontal:
            head_square_element = [(cls._PLUS + cls._DASH * (len(str(element)) + 2) + cls._PLUS) for element in array]
            body_square_element = [cls._VERTICAL + cls._BLANK + str(element) + cls._BLANK + cls._VERTICAL for element in array]
            print(' '.join(head_square_element))
            print(' '.join(body_square_element))
            print(' '.join(head_square_element))

    @classmethod
    def visualize_str(cls, string: str, font='bold'):
        print(' '.join([cls._ALL_FONTS[font]['head_letter'][cls._ALPHABET.index(letter.lower())] for letter in string]))
        print(' '.join([cls._ALL_FONTS[font]['body_letter'][cls._ALPHABET.index(letter.lower())] for letter in string]))
        print('\n')
