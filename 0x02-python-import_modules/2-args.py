#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    if args < 2:
        print("0 arguments.")
    elif args == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(args - 1))
        for i in range(args):
            if i < 1:
                continue
            print("{}: {}".format(i, argv[i]))
