#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    inf_add = 0
    for i in range(len(argv) - 1):
        inf_add += int(argv[i + 1])

    print("{}".format(inf_add))
