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

     
        #反馈标签
        self.label0 = QLabel('反馈', self)
        self.label0.setAlignment(Qt.AlignCenter)
        self.label0.setGeometry(0, 20, 80, 20)  #位置，大小

        #反馈值
        self.label = QLabel('反馈值', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 20, 80, 20)  #位置，大小

        #上一次给定
        self.labelt = QLabel('上次给定·', self)
        self.labelt.setAlignment(Qt.AlignCenter)
        self.labelt.setGeometry(150, 20, 80, 20)  #位置，大小

        #上一次给定值
        self.la = QLabel('00', self)
        self.la.setAlignment(Qt.AlignCenter)
        self.la.setGeometry(220, 20, 80, 20)  #位置，大小


        #输入控制数字
        self.ip1 = QLineEdit(self)
        #self.ip1.setText("0")
        self.ip1.setGeometry(20, 60, 130, 20)  #位置，大小

        #发送控制命令的按键
        self.button_3 = QPushButton('给定', self)           # 3
        self.button_3.clicked.connect(self.fs)
        self.button_3.setGeometry(160, 60, 60, 20)  #位置，大小

        self.label1 = QLabel('调节阀', self)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setGeometry(100, 180, 80, 20)  #位置，大小

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
        
        #self.llock1.lock()                       #锁住自建的全局变量 
        xxxx=gl.get_value(str(self.x+"fs"))         #从全局变量获取值,用于更新子窗口的数据
        self.label.setText(xxxx)                    #更新反馈

        xxx=gl.get_value(str(self.x+"kz"))   #更新控制
        self.la.setText(xxx)                    #更新上次给定

       
        #self.llock1.unlock()



    
    def fs(self):
        x1=self.ip1.text()
        #gl.set_value('score',self.x+"kz"+"+"+x1)  #向主程序发送值
        self.q.put(self.x+"+"+x1)       #将控制消息写入队列


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
            
            
            
            

            
            

