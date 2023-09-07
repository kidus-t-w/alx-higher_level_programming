#!/usr/bin/python3
def print_arg(argv):
    argvalues = sys.argv
    for i in range(1, len(argvalues)):
        if len(argvalues) == 2:
            print("1 argument:\n1: {}".format(argvalues[1]))
        elif len(argvalues) == 1:
            print(".")
        elif len(argvalues) > 2:
            if i == 1:
                print("{} arguments".format(len(argvalues) - 1))
                print("{}: {}".format(i, argvalues[i]))
            else:
                print("{}: {}".format(i, argvalues[i]))

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
