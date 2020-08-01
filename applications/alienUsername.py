import re

if __name__ == '__main__':
    dict = {True: 'VALID', False: 'INVALID'}
    pattern = '^[_.]\d+[a-zA-Z]*[_]?$'
    for _ in range(int(input())):
        print(dict[bool(re.search(pattern, input()))])
