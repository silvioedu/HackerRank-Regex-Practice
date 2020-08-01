import re

if __name__ == '__main__':

    regex_pattern = r"(?<=<)\w+"
    li = set()
    for _ in range(int(input())):
        s = input()
        [li.add(i) for i in re.findall(regex_pattern, s)]

    print(";".join(sorted(li)))
