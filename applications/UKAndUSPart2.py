import re


if __name__ == '__main__':
    sentences = []
    for x in range(int(input())):
        sentences.append(input())

    string = '\n'.join([x for x in sentences])

    for x in range(int(input())):
        words = re.sub('our', 'o[u]?r', input())
        regex = re.compile('\\b'+words+'\\b', re.IGNORECASE)
        words = regex.finditer(string)
        print(len(list(words)))
