# -*- coding: cp936 -*-
import time
h=0
for count in range(1,4):
    password = 0
    try:
        password = int(input("����������"))
    except:
        pass
    h += 1
    if password == 123:
        print("welcome back!")
        print("===============================�����ѯ��===================================")
        print("v1.0.0")
        print("������")
        print(time.strftime('%Y/%m/%d',time.localtime(time.time())))
        print(time.strftime('%H:%M:%S',time.localtime(time.time())))
        print("------------------------------���ߣ������----------------------------------")
        x = 0
        try:
            x = int(input("����:"))
        except:
            pass
        for i in range(1, x + 1):
            year = 0
            try:
                year = int(input("�������:"))
            except:
                pass
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print(year,"��������")
                    else:
                        print(year,"�겻������")
                else:
                    print(year,"��������")
            else:
                print(year,"�겻������")
        restart = 2
        try:
            restart = int(input("�Ƿ�������������1=�ǣ�0=���ǣ�"))
        except:
            pass
        if restart == 1:
            print("��������")
        elif restart == 0:
            break
        else:
            print("�㲻ʶ����")
            print("ϵͳ�Զ�����")
    
    else:
        print("���벻��ȷ!!!")
        print("����������!!!")


if h >= 3:
    print("�����ˣ���֪�������ȥ�����߰�")
else:
    print("�������")
    print("��ӭ�´�ʹ�ã�     :D")
