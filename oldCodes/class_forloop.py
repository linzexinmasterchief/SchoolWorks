# -*- coding: cp936 -*-
x = 1
try:
    x = int(input("times"))
except:
    pass
for t in range(1, x + 1):
    a = 0
    try:
        a = int(input("input a number"))
    except:
        pass
    b = 1
    for i in range(1, a + 1):
        b = b * i
    print(b)
        
