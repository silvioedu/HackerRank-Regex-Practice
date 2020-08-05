import re

if __name__ == '__main__':
    found = 0
    regex = r'hackerrank'
    for _ in range(int(input())):
        match = re.findall(regex, input().lower())
        found += len(match)
    print(found)