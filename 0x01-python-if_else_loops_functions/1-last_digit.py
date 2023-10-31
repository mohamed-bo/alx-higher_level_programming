#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last = number * -1
    last = last % 10
    last = last * -1
else:
    last = number % 10
print("Last digit of {}".format(number), end=' ')
if last > 5:
    print("is {} and is greater than 5".format(last))
elif last == 0:
    print("is {} and is 0".format(last))
elif last < 6 and last != 0:
    print("is {} and is less than 6 and not 0".format(last))
