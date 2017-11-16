#!/usr/bin/env python3

import math

from euclidean_algorithm import gcd

def mod_inverse(x, p):
    assert gcd(x,p) == 1
    for i in range(1, p):
        if (x * i % p == 1):
            return i

def find_order(x, p):
    for i in range(1, p):
        if (x ** i % p == 1):
            return i

def main():
    with open("input.txt") as inp:
        p = int(inp.readline())
        g = int(inp.readline())
        h = int(inp.readline())

        n = int(math.sqrt(find_order(g, p))) + 1

        g_inv = mod_inverse(g, p)
        print(g_inv)
        u = g_inv ** n % p

        list_1 = sorted(((i, g ** i % p) for i in range(0, n + 1)), key=lambda x: x[1])
        list_2 = sorted(((j, h * u ** j % p) for j in range(0, n + 1)), key=lambda x: x[1])

        li_1 = iter(list_1)
        li_2 = iter(list_2)

        a, b = next(li_1), next(li_2)

        try:
            while True:
                if (a[1] == b[1]):
                    break
                elif (a[1] < b[1]):
                    a = next(li_1)
                else:
                    b = next(li_2)
        except StopIteration:
            pass

        x = a[0] + n * b[0]

        with open("output.txt", "w") as out:
            out.write(str(x))

if __name__ == "__main__":
    main()
