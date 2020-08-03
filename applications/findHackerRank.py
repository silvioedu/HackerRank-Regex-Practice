import re

for _ in range(int(input())):

    sentence = input()
    start_pattern = r'^hackerrank'
    end_pattern = r'hackerrank$'
    start_end_pattern = r'^hackerrank(.*hackerrank)?$'

    if re.search(start_end_pattern, sentence):
        print(0)
    elif re.search(start_pattern, sentence):
        print(1)
    elif re.search(end_pattern, sentence):
        print(2)
    else:
        print(-1)
