''' day0, ex06 of python piscine data science '''
import sys
from ft_filter import ft_filter


def extract_input() -> list:
    ''' returnes the arguments passed as argv '''

    if len(sys.argv) != 3 or sys.argv[2].isdigit() is False:
        print('AssertionError: the arguments are bad')
        sys.exit(1)

    return [sys.argv[1], int(sys.argv[2])]


def main():
    ''' entrypoint to the filter tester '''
    text, word_len = extract_input()
    print(ft_filter(lambda x: len(x) > word_len, text.split(' ')))


if __name__ == '__main__':
    main()
