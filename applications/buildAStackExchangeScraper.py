import re
import sys

if __name__ == '__main__':
    stack = sys.stdin.read()
    regex = r'question-summary-(\w\w\w\w\w)".*?class="question-hyperlink">(.+?)</a>.*?class=\"relativetime\">(.+?)</span>'

    results = re.findall(regex, stack, re.DOTALL)

    for result in results:
        print(';'.join(result))
