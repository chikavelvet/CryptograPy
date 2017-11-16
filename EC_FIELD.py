#!/usr/bin/env python3


def main():
    p = 13
    a = 3
    b = 8
    for x in range(0, p):
        for y in range(0, p):
            # y^2 = x^3 + ax + b
            if (y ** 2) % p == (x ** 3 + a * x + b) % p:
                print("(%d, %d): O" % (x, y))


if __name__ == '__main__':
    main()
