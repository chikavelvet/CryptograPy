def gcd(a, b):
    if (b == 0):
        return a
    q = a // b
    r = a % b
    #print("%d = %d * %d + %d" % (a, b, q, r))
    return gcd(b, r)

    
