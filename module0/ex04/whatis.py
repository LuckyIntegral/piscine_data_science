''' day0, ex04 of python piscine data science '''
import sys

if len(sys.argv) == 1:
    sys.exit(1)

if len(sys.argv) > 2:
    print('AssertionError : more than one argument is provided')
    sys.exit(1)

try:
    print("I'm Even." if int(sys.argv[1]) % 2 == 0 else "I'm Odd.")
except ValueError as ve:
    print('AssertionError : argument is not an integer')
