#!/usr/bin/env python3


def gcd(a, b):
    if b == 0:
        return a
    q = a // b
    r = a % b
    return gcd(b, r)


def mod_inverse(x, p):
    assert gcd(x,p) == 1
    for i in range(1, p):
        if x * i % p == 1:
            return i


def main(p, a, b, x1, y1, x2, y2):
    # Curve function: y^2 = x^3 + a*x + b
    # Over Field F_p (integers mod p)
    # Points to add: (x1, y1) + (x2, y2)

    # Create line out of points
    # y = m(x - x1) + y1
    # m = (y2 - y1)/(x2 - x1)

    if x1 == x2:
        if y1 == y2:
            s_top = (3 * x1 ** 2 + a) % p
            s_bot = (2 * y1) % p
            s = (s_top * mod_inverse(s_bot, p)) % p
            x3 = (s ** 2 - 2 * x1) % p
            y3 = (s * (x1 - x3) - y1) % p
        else:
            return 'X', None
    else:
        s_top = (y2 - y1) % p
        s_bot = (x2 - x1) % p
        s = (s_top * mod_inverse(s_bot, p)) % p
        x3 = ((s ** 2) - x1 - x2) % p
        y3 = (s * (x1 - x3) - y1) % p

    return x3, y3


if __name__ == '__main__':
    print("Inputs read in from input.txt. Format should be:", '\tp\ta\tb', '\tx1\ty1', '\tx2\ty2',
          '(tab delimited numbers)', '', sep='\n')
    with open('input.txt', 'r') as inp:
        p, a, b = inp.readline().split('\t')
        p, a, b = int(p), int(a), int(b)

        x1, y1 = inp.readline().split('\t')
        x2, y2 = inp.readline().split('\t')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        print("Read in values:", '\tp: %d\ta: %d\tb: %d' % (p, a, b), '\tx1: %d\ty1: %d' % (x1, y1),
              '\tx2: %d\ty2: %d' % (x2, y2), '', sep='\n')

        x3, y3 = main(p, a, b, x1, y1, x2, y2)

        if y3:
            print("Result: (%d, %d) + (%d, %d) = (%d, %d)" % (x1, y1, x2, y2, x3, y3))
        else:
            print("Result: (%d, %d) + (%d, %d) = X" % (x1, y1, x2, y2))

        with open('output.txt', 'w') as out:
            print("Writing output to " + out.name)
            if y3:
                out.write('%d\t%d' % (x3, y3))
            else:
                out.write('X')
