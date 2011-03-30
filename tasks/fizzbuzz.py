#!/usr/bin env python

def fizzbuzz(n):
    if n % 15 == 0:
        print "FizzBuzz"
    elif n % 5 == 0:
        print "Fizz"
    elif n % 3 == 0:
        print "Buzz"
    else:
        print n

def recfizzbuzz(n):
    if n == 0: return ""
    if n % 15 == 0:
        return recfizzbuzz(n-1) + "Fizzbuzz \n"
    elif n % 5 == 0:
        return recfizzbuzz(n-1) + "Fizz \n"
    elif n % 3 == 0:
        return recfizzbuzz(n-1) + "Buzz \n"
    else:
        return recfizzbuzz(n-1) + str(n) +"\n"

for i in range(1,100):
    fizzbuzz(i)

print recfizzbuzz(100)

fizzbuzz = lambda x: x % 15 == 0 and 'FizzBuzz' or x % 5 == 0 and 'Fizz' or x % 3 == 0 and 'Buzz' or x 
print map(fizzbuzz, range(1,101))
