#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print (i)
        i -= 1
    print (f"Happy New Year!")

def square_integers(int_list):
    int_list = [number * number for number in int_list]
    return int_list

def fizzbuzz():
    i = 1
    while i <= 100:
        if (i % 3 == 0 and i % 5 == 0):
            print (f"FizzBuzz")
        elif i % 3 == 0:
            print (f"Fizz")
        elif i % 5 == 0:
            print (f"Buzz")
        else:
            print (i)
        i += 1
