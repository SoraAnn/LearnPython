# -*- coding: utf-8 -*-
import psutil
import datetime
#查看cpu的信息

#print(u"CPU 个数 %s"%psutil.cpu_count())
##print(u"物理CPU个数 %s"%psutil.cpu_count(logical=False))
#print(u"CPU uptimes")
#print(psutil.cpu_times())
#print("")

def  cpu_count():
    return str(psutil.cpu_count())

s = u'CPU个数：'





def cpu_percent():
    text = str(psutil.cpu_percent())
    return text

b = u'CPU占用率：'

f = open("cpu.txt","a+")
print(cpu_percent())
f.write(s + cpu_count())
f.write(b + cpu_percent())
f.close()