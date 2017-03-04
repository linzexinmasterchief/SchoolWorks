# -*- coding: cp936 -*-
import time
h=0
for count in range(1,4):
    password = 0
    try:
        password = int(input("请输入密码"))
    except:
        pass
    h += 1
    if password == 123:
        print("welcome back!")
        print("===============================闰年查询器===================================")
        print("v1.0.0")
        print("现在是")
        print(time.strftime('%Y/%m/%d',time.localtime(time.time())))
        print(time.strftime('%H:%M:%S',time.localtime(time.time())))
        print("------------------------------作者：林泽昕----------------------------------")
        x = 0
        try:
            x = int(input("次数:"))
        except:
            pass
        for i in range(1, x + 1):
            year = 0
            try:
                year = int(input("输入年份:"))
            except:
                pass
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print(year,"年是闰年")
                    else:
                        print(year,"年不是闰年")
                else:
                    print(year,"年是闰年")
            else:
                print(year,"年不是闰年")
        restart = 2
        try:
            restart = int(input("是否重新启动？（1=是，0=不是）"))
        except:
            pass
        if restart == 1:
            print("重新启动")
        elif restart == 0:
            break
        else:
            print("你不识字吗？")
            print("系统自动重启")
    
    else:
        print("密码不正确!!!")
        print("请重新输入!!!")


if h >= 3:
    print("别试了，想知道密码就去问作者啊")
else:
    print("程序结束")
    print("欢迎下次使用！     :D")
