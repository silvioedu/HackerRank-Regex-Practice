import re

if __name__ == '__main__':
    regex = r'http(s?)://(?:www.)?(([a-zA-Z0-9_-]+\.)+[a-zA-Z]+)'
    list = []

    for i in range(int(input())):
        s = input()
        if re.search(regex, s):
            for match in re.findall(regex, s):
                list.append(match[1])

    print(*sorted(set(list)), sep=';')
