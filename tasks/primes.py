#!/usr/bin/env python

from math import sqrt, ceil


"""
Write a program that accepts two integer parameters, X and Y.  Have it print all prime numbers between X and Y, inclusive.
"""


def isPrime(n):
    """
    Basically the quick test for whether or not a prime
    Arguments:
      n - an int
    Returns:
      A boolean of True or false 
    """
    #0 and 1 are special cases.
    if n == 0 or n == 1 or type(n) is not int: return False
    for num in xrange(2, int(ceil(sqrt(n)))):
        if n % num == 0:
            return False
    return True
            

def primes(x, y):
    """
    Takes 2 integers and gives you back all the prime
    numbers inclusive

    Arguments:
        x - a positive integer
        y - a positive integer
    """
    if type(x) is not int or type(y) is not int:
        print "All values need to be ints"
        return
    if x < 0 or y < 0:
        print "All values must be non-negative"
        return
    for val in xrange(x, y+1):
        if isPrime(val):
            print val

#Regular Ints
primes(0,101)
#Doesn't accept strings
primes(0, 's')
#Doesn't accept Negatives
primes(-1, 10)
primes(10, -1)

#This is a slightly more fun way to pull out the primes and force em in a list
#You need to make sure that you add 1 to the end since xrange goes up to n-1
print filter(isPrime, xrange(0,102))
