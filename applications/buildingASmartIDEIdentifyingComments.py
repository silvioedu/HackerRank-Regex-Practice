import re
import sys

if __name__ == '__main__':
    regex = r'(/\*.*?\*/|//.*?$)'
    sentence = sys.stdin.read()
    print("\n".join(re.sub('\n\s+', '\n', comment) for comment in re.findall(regex, sentence, re.DOTALL|re.MULTILINE)))
