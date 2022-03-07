from pycipher import Caesar
from pycipher import Autokey
from string import ascii_lowercase
from random import randint, choice


def shift(string):
    key = randint(1, 26)
    if type(string) == list:
        word = Caesar(key).encipher(string[0]).lower()
    else:
        word = Caesar(key).encipher(string).lower()
    return word


def flip(word):
    key = randint(1, 26)
    stuff = Caesar(key).encipher(ascii_lowercase).lower()
    stuff = list(stuff)
    stuff.reverse()
    stuff = ''.join(stuff)
    string = ''
    stuff = list(stuff)

    for letter in word:
        string += ascii_lowercase[stuff.index(letter)]
    return string


def tap(word):
    key = {
        'a': '(1, 1)',
        'b': '(2, 1)',
        'c': '(3, 1)',
        'd': '(4, 1)',
        'e': '(5, 1)',
        'f': '(1, 2)',
        'g': '(2, 2)',
        'h': '(3, 2)',
        'i': '(4, 2)',
        'j': '(5, 2)',
        'k': '(3, 1)',
        'l': '(1, 3)',
        'm': '(2, 3)',
        'n': '(3, 3)',
        'o': '(4, 3)',
        'p': '(5, 3)',
        'q': '(1, 4)',
        'r': '(2, 4)',
        's': '(3, 4)',
        't': '(4, 4)',
        'u': '(5, 4)',
        'v': '(1, 5)',
        'w': '(2, 5)',
        'x': '(3, 5)',
        'y': '(4, 5)',
        'z': '(5, 5)'
    }
    new_word = ''
    for each in word:
        new_word += key[each] + ', '
    return new_word[:-2]


def base5(word):
    key = {
        'a': '00',
        'b': '01',
        'c': '02',
        'd': '03',
        'e': '04',
        'f': '05',
        'g': '10',
        'h': '11',
        'i': '12',
        'j': '13',
        'k': '14',
        'l': '15',
        'm': '20',
        'n': '21',
        'o': '22',
        'p': '23',
        'q': '24',
        'r': '25',
        's': '30',
        't': '31',
        'u': '32',
        'v': '33',
        'w': '34',
        'x': '35',
        'y': '40',
        'z': '41'
    }
    new_word = ''
    for each in word:
        new_word += key[each] + ' '
    return new_word


def autokey(word):
    key = choice(['oft', 'hor', 'kyl', 'qui', 'aho', 'dur', 'jar', 'kol', 'teg', 'zad', 'sag', 'ani', 'tyt', 'hee', 'wro', 'pie', 'bhp', 'fey', 'qid', 'odz', 'mks', 'mus', 'mgr', 'adc', 'hoi', 'dev', 'bom', 'oot', 'enl', 'zip', 'mtx', 'sov', 'apl', 'syn', 'aff', 'owe', 'xix', 'sex', 'mux', 'plf', 'luo', 'yad', 'ann', 'six', 'ila', 'nog', 'fag', 'vis', 'ups', 'ler', 'use', 'lhb', 'goy', 'rut', 'tap', 'gau', 'mgd', 'lid', 'syd', 'han', 'abc', 'mfr', 'cun', 'trf', 'map', 'hny', 'xxx', 'rog', 'hon', 'fmt', 'pry', 'tsp', 'ijo', 'aht', 'soe', 'fiz', 'til', 'ume', 'rik', 'grs', 'edo', 'umu', 'sma', 'rus', 'web', 'tch', 'auf', 'mow', 'ais', 'sok', 'wag', 'ust', 'all', 'mod', 'jud', 'rio', 'hod', 'tot', 'ton', 'cml'])
    if type(word) == list:
        word = Autokey(key.upper()).encipher(word[0]).lower()
    else:
        word = Autokey(key.upper()).encipher(word).lower()

    return word


def encrypt(step, word):
    if step == 'flip':
        return flip(word)
    elif step == 'shift':
        return shift(word)
    elif step == 'tap':
        return tap(word)
    elif step == 'base':
        return base5(word)
    elif step == 'autokey':
        return autokey(word)
    else:
        raise Exception("NoKnownCipher!")
