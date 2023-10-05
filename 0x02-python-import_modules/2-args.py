#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    nbr_args = len(sys.argv) - 1
    args = sys.argv[1:]

    if nbr_args == 0:
        print('0 arguments.')
    elif nbr_args == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(nbr_args))

    for i in range(nbr_args):
        print('{}: {}'.format(i + 1, args[i]))
