import sys,queue,time
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout,QLineEdit
import queue
import sys
import globalvar as gl  #导入自建的全局变量

aaa="0000"
#q=queue.Queue()
class Demo(QWidget):
    def __init__(self,pp,q,llock1):          #pp代表阀门号。q代表传入子窗口的队列，用于发送控制消息。llock1用于锁住自建全局变量"
        super(Demo, self).__init__()  #重写父类的方法而不是覆盖的父类方法
        #获取参数
        self.x=pp 
        self.llock1=llock1
        self.q=q
        # 获取桌面属性
        desktop = QApplication.desktop()
        # 通过桌面的宽和高来比例位置显示
        self.move(desktop.width()*0.2, desktop.height()*0.2)
        self.resize(300, 100)

        #上一次给定
        self.labelt = QLabel('上次给定·', self)
        self.labelt.setAlignment(Qt.AlignCenter)
        self.labelt.setGeometry(150, 10, 80, 20)  #位置，大小

        #上一次给定值
        self.la = QLabel('00', self)
        self.la.setAlignment(Qt.AlignCenter)
        self.la.setGeometry(220, 10, 80, 20)  #位置，大小
        

        #开到位
        self.button_5 = QPushButton('开到位', self)           # 3
        #self.button_5.clicked.connect(self.op)
        self.button_5.setGeometry(60, 40, 60, 20)  #位置，大小

        #关到位
        self.button_6 = QPushButton('关到位', self)           # 3
        #self.button_6.clicked.connect(self.cs)
        self.button_6.setGeometry(60, 70, 60, 20)  #位置，大小

     






        #发送控制命令的按键
        self.button_3 = QPushButton('打开', self)           # 3
        self.button_3.clicked.connect(self.op)
        self.button_3.setGeometry(160, 40, 60, 20)  #位置，大小

        #发送控制命令的按键
        self.button_4 = QPushButton('关闭', self)           # 3
        self.button_4.clicked.connect(self.cs)
        self.button_4.setGeometry(160, 70, 60, 20)  #位置，大小

        self.sub_thread = subThread(q)
        self.sub_thread.sub_signal.connect(self.set_label_func)


        #自动开始线程
        self.sub_thread.is_on = True         # 5
        self.sub_thread.start()
        


    
    #重写关闭事件
    def closeEvent(self, event):
        print("chongxie")
        self.sub_thread.is_on = False
        self.sub_thread.count = 0
        self.close()

    

    #接收到子线程信号的处理函数,在子窗口显示反馈信息
    def set_label_func(self, fs0,fs1):
        
       
        self.la.setText(gl.get_value(str(self.x+"_o"))) 
        kdw=gl.get_value(str(self.x+"_k"))         #从全局变量获取值,获取开反馈，button_5
        gdw=gl.get_value(str(self.x+"_g"))         #从全局变量获取值,获取开反馈，button_6
        o=gl.get_value(str(self.x+"_o"))         #从全局变量获取值,获取开指令，button_3
        c=gl.get_value(str(self.x+"_c"))         #从全局变量获取值,获取关指令，button_4
        
        print(kdw,gdw,o,c)
        if kdw=="1":
            self.button_5.setStyleSheet("background: rgb(0,255,0)")   #设置按钮背景颜色
        else:
            self.button_5.setStyleSheet("background: rgb(255,255,255)")   #设置按钮背景颜色
        if gdw=="1":
            self.button_6.setStyleSheet("background: rgb(0,255,0)")   #设置按钮背景颜色
        else:
            self.button_6.setStyleSheet("background: rgb(255,255,255)")   #设置按钮背景颜色
        if o=="1":
            self.button_3.setStyleSheet("background: rgb(0,255,0)")   #设置按钮背景颜色
        else:
            self.button_3.setStyleSheet("background: rgb(255,255,255)")   #设置按钮背景颜色
        if c=="1":
            self.button_4.setStyleSheet("background: rgb(0,255,0)")   #设置按钮背景颜色
        else:
            self.button_4.setStyleSheet("background: rgb(255,255,255)")   #设置按钮背景颜色

        
      
       



    
    def op(self):
       
        #gl.set_value('score',self.x+"kz"+"+"+x1)  #向主程序发送值
        self.q.put(self.x+"+"+"open")

    def cs(self):
        
        #gl.set_value('score',self.x+"kz"+"+"+x1)  #向主程序发送值
        self.q.put(self.x+"+"+"close")


    #不能直接重写show方法
    def open(self):
        print(self.x)
        #self.plpp=True
        self.sub_thread.is_on = True         # 5
        self.sub_thread.start()
        self.setWindowTitle(self.x)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.show()
    
    def cd(self):
        print(self.x)
        self.sub_thread.is_on = True         # 5
        self.sub_thread.start()
        self.setWindowTitle(self.x)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.showw()
    

       
    
    
#子窗口用于刷新信号的线程

class subThread(QThread):
    #定义线程传递的信号
    sub_signal = pyqtSignal(str,str)

    def __init__(self,qq):
        super(subThread, self).__init__()
        self.q=qq
        self.count = 0
        self.is_on = True   # 1

    def run(self):
        while self.is_on:   # 2
            
            #获取反馈信号
            #gl.set_value('score', self.count) #设定值
            #xxx=gl.get_value('e2')         #从全局变量获取值,用于更新子窗口的
            self.sub_signal.emit("world","hello")  #发送获取的值,用于更新子窗口的数据,这里只用来触发更新子窗口数据的函数
            #qqq=self.q
            #qqq.put("hello world")
            self.sleep(1)
            
            
            
            

            
            

