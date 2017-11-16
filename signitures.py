#!/usr/bin/env python3


def euclidean_gcd_recursive(a, b):
    if a < b:
        return euclidean_gcd_recursive(b, a)
    q, r = b, a % b
    if r == 0:
        return q
    return euclidean_gcd_recursive(q, r)


def gcd(a, b):
    return euclidean_gcd_recursive(a, b)


def inverse(x):
    return x.__inv__()


class Group:
    def elem_inv(self, elem):
        pass


class ZmodPGroup(Group):
    def __init__(self, p):
        self.p = p

    def elements(self):
        return (i for i in range(1, self.p))

    def elem_inv(self, elem):
        assert gcd(elem, self.p) == 1
        for i in self.elements():
            if (elem * i) % self.p == 1:
                return i


class GroupElem:
    def __init__(self, g):
        self.group = g

    def __inv__(self):
        return self.group.elem_inv(self)

    def __invert__(self):
        return self.__inv__()


def brute_force_mod_inv(n, p):
    assert gcd(n, p) == 1
    for i in range(1, p):
        if (n * i) % p == 1:
            return i


def mod_inv(n, p):
    return brute_force_mod_inv(n, p)


class CryptoSystem:
    def decrypt(self, m):
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
        return doc, (doc ** self._d) % self.N

    def verify_sign(self, doc, signature, n=None, e=None):
        if not e:
            e = self.e
        if not n:
            n = self.N
        return (signature ** e) % n == doc

    def public_key(self):
        return self.N, self.e

    def _find_e(self):
        for i in range(2, self._tot):
            if gcd(i, self._tot) == 1:
                yield i

    def __str__(self):
        return "Public key: (%d, %d)" % self.public_key()


def main():
    rsa = RSA(7, 11)


if __name__ == '__main__':
    main()
