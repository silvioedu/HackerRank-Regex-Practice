import re

if __name__ == '__main__':
    regex = r'^[A-Z]{5}\d{4}[A-Z]$'
    dict = {True: "YES", False: "NO"}

    for _ in range(int(input())):
        print(dict[bool(re.search(regex, input()))])
