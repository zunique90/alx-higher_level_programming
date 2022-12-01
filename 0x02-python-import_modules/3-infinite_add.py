#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    total = 0
    if args < 2:
        print(f"{total:d}")
    else:
        for i in range(1, args):
            total += int(argv[i])
        print(f"{total:d}")
