#!/usr/bin/env python3


def deg(arr):
    rev = list(reversed(arr))
    degree = len(rev) - 1
    for i in rev:
        if i != 0:
            return degree
        else:
            degree -= 1
    return 0


class polynomial:
    def __init__(self, p=[0]):
        self.d = deg(p)
        self.array = p[0:self.d + 1] if self.d > 0 else p[0:1]

    def __str__(self):
        rev = list(reversed(self.array))
        d = self.d
        it = iter(rev)
        reduction = ''
        if self.d == 0:
            return str(next(it))
        elif self.d == 1:
            coef = next(it)
            if coef != 1:
                reduction = '%dx' % coef
            else:
                reduction = 'x'
        else:
            reduction = '%dx^%d' % (next(it), d)
        d -= 1
        for p in it:
            if p == 0:
                d -= 1
                continue
            operator = '+' if p > 0 else '-'
            coefficient = str(abs(p)) if p != 1 or d == 0 else ''
            x = 'x' if d > 0 else ''
            power = '^%d' % d if d > 1 else ''

            reduction += ' %s %s%s%s' % (operator, coefficient, x, power)
            d -= 1
        return reduction

    def __add__(self, other):
        arr1 = self.array
        arr2 = other.array

        result = [0] * max(len(arr1), len(arr2))
        for i in range(0, len(result)):
            if i < len(arr1):
                result[i] += arr1[i]
            if i < len(arr2):
                result[i] += arr2[i]

        return polynomial(result)

    def __sub__(self, other):
        arr1 = self.array
        arr2 = other.array
        result = [0] * max(len(arr1), len(arr2))
        for i in range(0, len(result)):
            if i < len(arr1):
                result[i] += arr1[i]
            if i < len(arr2):
                result[i] -= arr2[i]
        return polynomial(result)

    def __mul__(self, other):
        arr1 = self.array
        arr2 = other.array
        result = [0] * (len(arr1) + len(arr2) - 1)
        for i in range(0, len(arr1)):
            for j in range(0, len(arr2)):
                result[i + j] = result[i + j] + (arr1[i] * arr2[j])
        return polynomial(result)

    def deg(self):
        return self.d

    def __divmod__(self, other):
        n = self
        d = other

        def lead(arr):
            rev = list(reversed(arr))
            for i in range(0, len(rev)):
                if rev[i] != 0:
                    return [rev[i]] + [0] * (len(rev) - i - 1)

        def lead_div(p1, p2):
            arr1 = p1.array
            arr2 = p2.array
            l1 = lead(arr1)
            l2 = lead(arr2)
            diff = len(l1) - len(l2)
            if diff < 0:
                return l1
            return polynomial(list(reversed(([l1[0] // l2[0]] + [0] * diff))))

        quo = polynomial()
        r = n

        while r.array != [0] and r.deg() >= d.deg():
            t = lead_div(r, d)
            quo = quo + t
            r = r - (t * d)

        return quo, r

    def __mod__(self, other):
        q, r = divmod(self, other)
        return r

    def reduce(self, p):
        return polynomial([x % p for x in self.array])


def main(p, m, q1, q2):
    return ((q1 + q2) % m).reduce(p), ((q1 * q2) % m).reduce(p)


if __name__ == '__main__':
    print('Inputs read in from input.txt. Format should be:', '\tp', '\tm', '\tq1', '\tq2',
          'Note: all polynomials should be represented by space delimited numbers of ascending order '
          '(0s must be included)', '\tEx.: x^3 + 2x + 4 would be 4 2 0 1\n', sep='\n')
    with open('input.txt', 'r') as inp:
        p = int(inp.readline())
        m = polynomial(list(map(lambda x: int(x), inp.readline().split(' '))))
        q1 = polynomial(list(map(lambda x: int(x), inp.readline().split(' '))))
        q2 = polynomial(list(map(lambda x: int(x), inp.readline().split(' '))))
        print("Read in values:", '\tp: %d' % p, '\tm: %s' % str(m), '\tq1: %s' % str(q1), '\tq2: %s' % str(q2), '', sep='\n')
        r1, r2 = main(p, m, q1, q2)
        print("Result: q1 + q1 = %s (mod m)\n        q1 * q2 = %s (mod m)\n" % (r1, r2))
        with open('output.txt', 'w') as out:
            print('Writing output to %s' % out.name)
            out.write("%s\n%s" % (str(r1), str(r2)))
