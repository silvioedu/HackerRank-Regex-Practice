import sys

if __name__ == '__main__':
    src = ''.join(sys.stdin.readlines())

    if 'import java' in src:
        print("Java")
    elif '#include' in src:
        print("C")
    else:
        print("Python")
