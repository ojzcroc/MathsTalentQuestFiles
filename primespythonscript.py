#sieve of Eratosthenes
def sieve_of_Eratosthenes(n):
    i = 2
    while n%i != 0 and 2*i < n:
        i += 1
    if n == 2:
        return True
    elif n%i != 0:
        return True
    else:
        return False
s=sieve_of_Eratosthenes
def Fermat():
    n=2
    while 1 == 1:
        print n+1
        print s(n+1)
        n = n*2
def prime():
    n = 1
    while 1 == 1:
        print n
        print s(n)
        n += 1
def prime_only():
    n = 0
    i = 0
    while 1 == 1:
        n += 1
        if s(n) == True:
            print str(i) + ": " + str(n)
            i += 1

p = prime_only

def factorising(n):
    i = 1
    for x in range(0,n):
        if n%i == 0:
            print i
            i += 1
        if n%i != 0:
            i += 1
f = factorising
def fac(n):
    m = n-1
    res = n
    for x in range(0,n):
        if m != 0:
            res *= m
            m -= 1
    return res
def prime_factorials():
    n = 1
    i = fac(n) - 1
    while 1 == 1:
        if s(i) == True:
            print n-1
            n += 1
        else:
            n += 1

def Series(n):
    return (n**2 + n)/2

ser = Series

def prime_factorising(n):
    i = 1
    for x in range(0,n):
        if n%i == 0:
            if s(i) == True or i == n or i == 1:
                print i
            i += 1
        if n%i != 0:
            i += 1
pf = prime_factorising
def pToq():
    primes = [2,3,5,7,11,13]
    while 1 == 1:
        Q = 1
        for x in primes:
            print x
            Q *= x
        Q += 1
        if s(Q) == True:
            primes.append(Q)
        else:
            i = 1
            for x in range(0,Q):
                if Q%i == 0:
                    if s(i) == True:
                        primes.append(i)
                    i += 1
                if Q%i != 0:
                    i += 1
        print Q
        print primes

