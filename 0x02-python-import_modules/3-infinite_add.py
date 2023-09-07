#!/usr/bin/python3
def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("0")
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add = add + int(argv[i])
            i += 1
        print("{}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
