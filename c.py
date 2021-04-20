#import ctypes
import sys
from ctypes import *
'''
foo=cdll.LoadLibrary('C:\\Users\\lh\Desktop\\p-test\\lab\\LABb\\x.dll')
foo.pp.argtypes = (c_float, c_float) # addf 有两个形参，都是 float 类型
foo.pp.restype = c_float # addf 返回值的类型是 flaot
print(foo.pp(2,9))
'''

pyarray = [1,2,3,4,5,6,7,8,9,10]
carray = (c_int*len(pyarray))(*pyarray)
foo=cdll.LoadLibrary('x.dll')

foo.pp.argtypes = [POINTER(c_int)]      #定义输入参数的类型
foo.pp(carray)
print(carray[0])
print(carray[1])
print(carray[2])
print(carray[3])