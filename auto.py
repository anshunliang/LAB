import sys,queue,time
from globalfile import gwh as gw         #导入工位号全局变量
from globalfile import shuju as sj        #导入数据全局变量

def sy(x):
    s=gw.get()
    ss=s.index(x)
    return sj.get()[ss]


    
#下面这个函数写自动控制逻辑
def autocontronl(dl):
    
    if float(sy("e3fs"))>2: 
        dl.put("iiiiiii")