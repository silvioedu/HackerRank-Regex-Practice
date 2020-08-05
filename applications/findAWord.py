import re


if __name__ == '__main__':

    sentence = ' '.join(input() for _ in range(int(input())))

    for _ in range(int(input())):
        print(len(re.findall(r'((?<=\W)|^)%s((?=\W)|$)' % input(), sentence)))


