# -*- coding: cp936 -*-
while True:
    a = 0
    try:
        a = int(input("票数"))
    except:
        pass
    if a < 0:
        print("are you silly?")
    elif 0 <= a < 10:
        price = a * 20 * 1.0
    elif 10 <= a < 20:
        price = a * 20 * 0.9
    else:
        price = a * 20 * 0.8
    print(price)
