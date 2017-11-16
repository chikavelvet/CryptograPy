#!/usr/bin/env python3

import random

with open("input.txt") as f:
    p = int(f.readline())
    g = int(f.readline())
    m = int(f.readline())
    g_to_a = int(f.readline())
    
    k = 197 #random.randint(1, p)

    c_1, c_2 = (g ** k) % p, (m * (g_to_a ** k)) % p
    
    print("c_1 = %d^%d = %d (mod %d)" % (g, k, c_1, p))
    print("c_2 = %d*%d^%d = %d (mod %d)" % (m, g_to_a, k, c_2, p))

    with open("output.txt", "w") as out:
        out.write("(%d, %d)" % (c_1, c_2))


