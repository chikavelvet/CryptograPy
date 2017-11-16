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


def main():
    with open("input.txt") as inp:
        e = int(inp.readline())
        c = int(inp.readline())
        p = int(inp.readline())

        #        print("e=%d, c=%d, p=%d" % (e, c, p))
        factors = list(brute_factor(p))
        if len(factors) > 2:
            factors = factors[2:]

        print("Factors: " + str(factors))

        congruences = [(c % f, f) for f in factors]

        print("Congruences: " + str(congruences))

        roots = [(brute_root(x, e, m), m) for x, m in congruences]

        print("Roots: " + str(roots))

        try:
            x, p_iden = binary_chinese_remainder_theorem(*roots[0], *roots[1])
        except TypeError:
            print("Error: e-th root not found in mod-space of at least one factor")
            return

        print("Self-check: " + str(p == p_iden and x ** e % p == c))

        print("Done.")

        with open("output.txt", 'w') as out:
            out.write(str(x))
            print("Successfully wrote to " + str(out.name))


if __name__ == "__main__":
    print("Note: p must be prime or be a product of two primes")
    main()
