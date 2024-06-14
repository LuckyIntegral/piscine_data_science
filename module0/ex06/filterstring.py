''' day0, ex06 of python piscine data science '''
import sys
from ft_filter import ft_filter


def ft_split(text: str, sep: str) -> list:
    ''' same as split(), lol '''
    res = []
    curr = ""

    for char in text:
        if char != sep:
            curr += char
        else:
            if curr != '':
                res.append(curr)
            curr = ''

    if curr != '':
        res.append(curr)

    return res


def extract_input() -> list:
    ''' returnes the arguments passed as argv '''

    if len(sys.argv) != 3 or sys.argv[2].isdigit() is False:
        raise AssertionError('the arguments are bad')

    return [sys.argv[1], int(sys.argv[2])]


def main():
    ''' entrypoint to the filter tester '''
    try:
        text, word_len = extract_input()
        print(ft_filter(lambda x: len(x) > word_len, ft_split(text, ' ')))
    except AssertionError as ae:
        print(f"AssertionError: {ae}")


if __name__ == '__main__':
    main()
