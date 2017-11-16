#!/usr/bin/env python3

from math import sqrt

def euclidean_gcd(a, b):
    if (b == 0):
        return a
    q = a // b
    r = a % b
    return euclidean_gcd(b, r)

def brute_mod_inverse(x, p):
    if euclidean_gcd(x, p) != 1:
        raise Exception
    for i in range(1, p):
        if (x * i % p == 1):
            return i

def brute_factor(x):
    for i in range(1, int(sqrt(x))):
        if x % i == 0:
            yield i
            yield x // i

def brute_root(x, pow, m):
    if x == 0:
        return 0
    for i in range(1, m):
        if i ** pow % m == x:
            return i

def binary_chinese_remainder_theorem (a, p, b, q):
    y = ((b - a) % q) * brute_mod_inverse(p, q) % q
    x = (a + (p * y)) % (p * q)
    return x, (p * q)

def eulers_phi(N):
    return len([k for k in range(0, N) if euclidean_gcd(k, N) == 1])

def main(e, c, p):
    
    print("Done.")


if __name__ == "__main__":
    print("Note: p must be prime or be a product of two primes")
    with open("input.txt") as inp:
        e = int(inp.readline())
        c = int(inp.readline())
        p = int(inp.readline())

        main(e, c, p)
        with open("output.txt", 'w') as out:
            out.write(str(x))
            print("Successfully wrote to " + str(out.name))


