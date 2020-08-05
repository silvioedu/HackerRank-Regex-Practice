import re

if __name__ == '__main__':
    SIGN = '[\+-]?'
    DECIMALS = '(\.[0-9]+)?'
    ZEROS = '(\.0+)?'

    LATITUDE =  f'{SIGN}(90{ZEROS}|[1-8]\d{DECIMALS}|\d{DECIMALS})'
    LONGITUDE = f'{SIGN}(180{ZEROS}|1[0-7]\d{DECIMALS}|[1-9]\d{DECIMALS}|\d{DECIMALS})'

    regex = f'\({LATITUDE}, {LONGITUDE}\)'

    for _ in range(int(input())):
        print("Valid") if re.search(regex, input()) else print("Invalid")
