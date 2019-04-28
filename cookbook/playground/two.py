# encoding: utf-8

"""a test module"""

__author__ = "Michael liao"

import sys


def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print("hello, world")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("too many arguments")


if __name__ == '__main__':
    test()
