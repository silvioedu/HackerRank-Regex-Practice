import re

if __name__ == '__main__':
    regex = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'
    for _ in range(int(input())):
        res = re.findall(regex, input())
        for link, title in res:
            print("{},{}".format(link, title.strip()))
