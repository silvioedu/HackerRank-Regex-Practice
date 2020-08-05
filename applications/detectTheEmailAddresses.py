import re
import sys

if __name__ == '__main__':
    s = sys.stdin.read()
    regex = r'[\w\.]+@(?:\w+\.)+\w+'
    elist = re.findall(regex, s)
    print(';'.join(sorted(list(set(elist)))))
