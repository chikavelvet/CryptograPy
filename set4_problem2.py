#!/usr/bin/env python3

def euclidean_gcd(a, b):
    if (b == 0):
        return a
    q = a // b
    r = a % b
    return euclidean_gcd(b, r)

def main(N):
    a = 2
    d = 1
    bound = 1000
    for j in range(2, bound):
        a = a ** j % N
        d = euclidean_gcd(a - 1, N)
        if d > 1 and d < N:
            break
    else:
        print("Couldn't find non-trivial gcd in first %d powers" % (bound))

    return d, N // d


if __name__ == "__main__":
    with open("input.txt") as inp:
        N = int(inp.readline())
        p, q = main(N)
        print("Done.")
        with open("output.txt", 'w') as out:
            out.write(str(p) + "\n" + str(q))
            print("Successfully wrote to " + out.name)
