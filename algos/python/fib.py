#!/usr/bin/env python

def rec_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return rec_fib(n-1) + rec_fib(n-2)

if __name__ == '__main__':
    print rec_fib(12)
