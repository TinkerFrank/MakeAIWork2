import sys

def cat():
    print('miauw')

def default():
    print('hello')

def dog():
    print('woof')

def main():
    if sys.argv[1]=='dog':
        dog()
    elif sys.argv[1]=='cat':
        cat()
    else:
        default()


if __name__ == '__main__':
    main()


