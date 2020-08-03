import re

if __name__ == '__main__':
    regex = r"\d+"
    for _ in range(int(input())):
        match = re.findall(regex, input())
        print("CountryCode={},LocalAreaCode={},Number={}".format(match[0], match[1], match[2]))