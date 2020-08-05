import re

if __name__ == '__main__':
    regex = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'
    dict = {True: "VALID", False: "INVALID"}

    for _ in range(int(input())):
        print(dict[bool(re.search(regex, input()))])
