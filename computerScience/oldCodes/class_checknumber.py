# -*- coding: cp936 -*-
import random
while True:
    a = random.randrange(9)
    b = random.randrange(9)
    c = random.randrange(9)
    d = random.randrange(9)
    print(a,b,c,d)
    e = 1000 * a + 100 * b + 10 * c + d
    x = 0
    try:
        x = int(input("input check number:"))
    except:
        pass
    if x == e:
        print("welcome!")
        break
    else:
        print("wrong!")

