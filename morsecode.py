import re

morsecode = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...',
    't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', ' ': ".......", '0': '-----',
    '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}


class MorseCode():

    def __init__(self):
        self.word = ''

    def get_morse_code(self):
        pattern = re.compile("[A-Za-z0-9\s]+")
        if bool(pattern.fullmatch(self.word)):
            morse_code_word = ''
            for letter in self.word:
                morse_code_word += f'{morsecode[letter]} '
            return morse_code_word