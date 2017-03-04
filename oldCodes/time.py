# -*- coding: cp936 -*-
import time

print ("it is now")
print (time.strftime('%Y/%m/%d',time.localtime(time.time())))
print (time.strftime('%H:%M:%S',time.localtime(time.time())))
