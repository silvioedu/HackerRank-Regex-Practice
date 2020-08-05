import re


if __name__ == '__main__':
    sentences = ""
    for _ in range(int(input())):
        sentences += input()

    for _ in range(int(input())):
        s = input()
        s = s[:len(s)-2] + '[sz]e'
        print(len(re.findall(s, sentences)))
