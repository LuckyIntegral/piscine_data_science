''' day0, ex07 of python piscine data science '''
import sys


def convert_to_morse(to_converte: str) -> str:
    ''' function to converte chars into morses code '''
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    if to_converte not in NESTED_MORSE:
        raise AssertionError("the arguments are bad")

    return NESTED_MORSE[to_converte]


def get_input() -> str:
    ''' function to receive users input '''

    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    return sys.argv[1]


def display_code(codes: str) -> None:
    ''' convertes all the characters to morse codes and prints them out '''
    output = []
    for char in codes:
        output.append(convert_to_morse(char.upper()))
        output.append(' ')

    if output:
        output.pop()

    for code in output:
        print(code, end="")
    print()


def main():
    ''' entrypoint for morse encoder program '''
    try:
        users_input = get_input()
        display_code(users_input)
    except AssertionError as ae:
        print(f"AssertionError: {ae}")


if __name__ == '__main__':
    main()
