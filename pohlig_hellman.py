#!/usr/bin/env python3

from babystep_giantstep import find_order

def prime_factorize(n):
    # TODO: Finish This
    factors = []
    for x in range(1, n):
        if (n % x == 0):
            factors += prime_factorize(x)

def main():
    # Pohlig-Hellman Algorithm
    with open("input.txt") as input:
        g = int(input.readline())
        h = int(input.readline())
        p = int(input.readline())
        p_minus_1 = p - 1

        p_minus_1_prime_factors = prime_factorize(p_minus_1)

        N = find_order(g, p)

        
if __name__ == "__main__":
    main()

