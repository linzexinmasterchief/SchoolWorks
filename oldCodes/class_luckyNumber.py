# -*- coding: cp936 -*-
import random

number = random.randrange(100)

while True:
    x = 0
    try:
        x = int(input("Enter a number:"))
    except:
        pass
    if x == number:
        print("you are right!")
        break
    else:
        if x > number:
            print("too big")
        else:
            print("too small")
