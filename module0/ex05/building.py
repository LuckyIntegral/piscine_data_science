''' day0, ex05 of python piscine data science '''
import sys


def get_input() -> str:
    ''' function to receive input '''
    if len(sys.argv) > 2:
        print('AssertionError : more than one argument is provided')
        sys.exit(1)

    if len(sys.argv) == 2:
        return sys.argv[1]

    print("What is the text to count?")
    text = sys.stdin.readline()

    return text


def analyse_text(text: str) -> None:
    ''' function that makes statistics for the text passed as argument '''
    lowercases, uppercases, spaces, punctuations, digits = 0, 0, 0, 0, 0

    for char in text:
        if char.islower():
            lowercases += 1
        elif char.isupper():
            uppercases += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
        else:
            punctuations += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{uppercases} upper letters")
    print(f"{lowercases} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


# 2 upper letters
# 121 lower letters
# 8 punctuation marks
# 25 spaces
# 15 digits


def main():
    ''' entrypoint of text analysis program '''
    text = get_input()
    analyse_text(text)


if __name__ == "__main__":
    main()
