#!/usr/bin/env python3


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    q = a // b
    r = a % b
    if r == 0:
        return q
    return gcd(q, r)


def brute_force_mod_inv(n, p):
    assert gcd(n, p) == 1
    for i in range(1, p):
        print(n, i, n*i % p)
        if (n * i) % p == 1:
            return i


def mod_inv(n, p):
    return brute_force_mod_inv(n, p)


class CryptoSystem:
    pass


class RSA(CryptoSystem):
    def __init__(self, p, q):
        self._p = p
        self._q = q
        self.N = p * q
        self._tot = (p - 1) * (q - 1)
        self.e = next(self._find_e())
        self._d = mod_inv(self.e, self._tot)

    def sign(self, doc):
        pass

    def public_key(self):
        return self.N, self.e

    def _find_e(self):
        for i in range(1, self._tot):
            if gcd(i, self._tot) == 1:
                yield i


def main():
    rsa = RSA(7, 11)


if __name__ == '__main__':
    main()
