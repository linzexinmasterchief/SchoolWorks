# -*- coding: cp936 -*-
print("chengFaBiao")
a = 1
for i in range(1, 10):
    b = 0
    for x in range(1,i + 1):
        b += 1
        print(i,"*",b,"=",i*b,"|",end=" ")
    print("\n")