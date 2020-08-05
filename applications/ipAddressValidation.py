import re


if __name__ == '__main__':
    regex_ipv6 = r'^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$'
    regex_ipv4 = r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'

    for _ in range(int(input())):
        s = input()
        if re.search(regex_ipv6, s):
            print('IPv6')
        elif re.search(regex_ipv4, s):
            print('IPv4')
        else:
            print('Neither')
