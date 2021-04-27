import sys
from ctypes import *
'''
foo=cdll.LoadLibrary('C:\\Users\\lh\Desktop\\p-test\\lab\\LABb\\x.dll')
foo.pp.argtypes = (c_float, c_float) # addf 有两个形参，都是 float 类型
foo.pp.restype = c_float # addf 返回值的类型是 flaot
print(foo.pp(2,9))
'''

pyarray = [1.2,2,3,4,5,6,7,8,9,10]   #模拟原始值
pyarrayx = [1,2,3,4,5,6,7,8,9,10]    #模拟工程值下限
pyarrays = [1,2,3,4,5,6,7,8,9,10]    #模拟工程值上限
pyarrayjg=[1.1,2.2,3.3,4,5,6,7,8,9,10]


carray = (c_float*len(pyarray))(*pyarray)
carrayx = (c_float*len(pyarrayx))(*pyarrayx)
carrays = (c_float*len(pyarrays))(*pyarrays)
carrayjs = (c_float*len(pyarrayjg))(*pyarrayjg)




foo=cdll.LoadLibrary('F:\\jiemian\\C\\x.dll')

foo.pp.argtypes = [POINTER(c_float),POINTER(c_float),POINTER(c_float),POINTER(c_float),c_int] 

pointer(carray).contents[6]=9999

foo.pp(carray,carrayx,carrays,carrayjs,4)
for i in carray:
    print(i)