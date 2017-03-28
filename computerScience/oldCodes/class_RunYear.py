# -*- coding: cp936 -*-
import time
h=0
for count in range(1, 4):
    password = 0
    try:
        password = int(input("enter password:"))
    except:
        pass
    h += 1
    if password == 123:
        print("welcome back!")
        print("===============================[welecome]===================================")
        print("v1.0.0")
        print("today is")
        print(time.strftime('%Y/%m/%d', time.localtime(time.time())))
        print(time.strftime('%H:%M:%S', time.localtime(time.time())))
        print("----------------------------------------------------------------------------")
        x = 0
        try:
            x = int(input("times:"))
        except:
            pass
        for i in range(1, x + 1):
            year = 0
            try:
                year = int(input("years:"))
            except:
                pass
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print(year, "is run year")
                    else:
                        print(year, "is not run year")
                else:
                    print(year, "is run year")
            else:
                print(year, "is not run year")
        restart = 2
        try:
            restart = int(input("do you want to restart?(1=yes, 0=no)"))
        except:
            pass
        if restart == 1:
            continue
        elif restart == 0:
            break
        else:
            print("are you silly?")
            continue
    else:
        print("wrong password!!!")
        print("Enter again!!!")


if h >= 3:
    print("tried 3 times, exiting")
else:
    print("thank you for using")
