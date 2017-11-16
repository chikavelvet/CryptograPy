#!/usr/bin/env python3

from babystep_giantstep import mod_inverse

def main():
    with open("input.txt") as input:
        a = int(input.readline())
        p = int(input.readline())
        b = int(input.readline())
        q = int(input.readline())

        y = ((b - a) % q) * mod_inverse(p, q) % q

        x = (a + (p * y)) % (p * q) 

        with open("output.txt", 'w') as out:
            out.write(str(x))

if __name__ == "__main__":
    main()
