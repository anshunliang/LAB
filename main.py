import sys,time
import random,queue,openpyxl,cgitb,threading
from functools import partial
from PyQt5.QtCore import *
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline
from PyQt5.QtWidgets import *
from PyQt5 import *

from kpas import kpa     #导入压力转换模块
import globalvar as gl   #导入自建的全局变量

from x import Ui_MainWindow   #导入主窗口
import bool,floatt    #导入开关阀和调节阀子窗口 
import tx
 
gl._init()            #全局变量初始化
cgitb.enable()        #异常捕捉



lock = QMutex()   #实例化锁,针对数据读取和数据刷新两个线程
lock1 = QMutex()   #实例化锁,针对自建的全局变量

q=queue.Queue()   #实例化队列，针对控制消息获取


#建立全局变量
xp=[]  #用于存储控件
xh=[]  #用于存储采集的现场信号
jp=[]    #存储控件对应的数值索引


class Main(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
    def prt(self):
        print("jjjj")
    
    
        



#读取配置表
data = openpyxl.load_workbook('F:\jiemian\AI.xlsx')
wsai = data.get_sheet_by_name('AI')
wsao = data.get_sheet_by_name('AO')
wsai_nrows = wsai.max_row  #获得AI行数
wsao_nrows = wsao.max_row  #获得AO行数
PZAI=[]                    #存储AI工位号
PZAO=[]                    #存储AO工位号
PZDI=[]
PZDO=[]
#读AI表格
for i in range(1,wsai_nrows):
    j= wsai.cell(row=i+1, column=1).value    #获取1+1行，第一列的值
    PZAI.append(j)
print(PZAI)
#读AO表格
for i in range(1,wsao_nrows):
    j= wsao.cell(row=i+1, column=1).value    #获取1+1行，第一列的值
    PZAO.append(j)

print(PZAO)

'''
#定义子窗口
class Child(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("使用教程")
        self.resize(250, 180)
        self.dk= QLabel(self)
        self.dk.setGeometry(30, 30, 100, 100)
        str='端口'
        self.dk.setText(str)
        
        
    def open(self):
        self.show()
'''


#首次运行时，根据配置表搜索前面板控件的函数，
def click_success():
    print("start qt5")
    
    global xp
    global PZAI
    global jp
    #for i in ["e1","e2","e3","e4",]:
    
    j1=0
    for i in PZAI:
        try:
            if MainWindow.findChild(QLineEdit,i):   #根据反馈工位号获取前面板控件
               xp.append(MainWindow.findChild(QLineEdit,i))
               jp.append(j1)
               j1+=1
            else:
                j1+=1
        except:
            pass
    j1=0
    print(xp)
    print(jp)



#读取信号线程
class Mythread(QThread):
    # 定义信号,定义参数为str类型
    breakSignal = pyqtSignal(object)
 
    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        a=1
        time.sleep(1)
        
        global xp
        global PZAI
        while True:
            time.sleep(0.1)
            
            #发送信号到刷新函数,触发界面刷新函数
            #self.breakSignal.emit(str(a))
            a+=1

            #模拟产生现场信号,用于刷新主界面
            lock.lock()
            global xh
            xh.clear()
            for i in range(10):
                xh.append(random.randint(0,2))
            

            #模拟从现场读取的控制信号，实际使用时，从 xh 这个列表里截取数组
            lock1.lock()
            try:
                for i in PZAI:
                    gl.set_value(i, str(random.randint(0,100)))     #设定值
                    
                for i in PZAO:
                    gl.set_value(i, ui.pc.text())     #设定值
            except:
                pass
            
            lock1.unlock()
            
            #发送信号到刷新函数,触发界面刷新函数
            self.breakSignal.emit(xh)
            if xh[1]==0:
                ui.pp1.setStyleSheet("background: rgb(0,255,0)")   #设置按钮背景颜色
                ui.pp2.setStyleSheet("background: rgb(0,255,0)")   #设置按钮背景颜色
            if xh[1]==1:
                ui.pp1.setStyleSheet("background: rgb(255,0,0)")   #设置按钮背景颜色
                ui.pp2.setStyleSheet("background: rgb(255,0,0)")   #设置按钮背景颜色
         
            lock.unlock()
            
            


#刷新界面线程
class Mythread1(QThread):
    # 定义信号,定义参数为int类型
    def __init__(self, parent=None):
        super().__init__(parent)
    global xh
    global jp
    def run(self):
        time.sleep(2)
        sd=0
        while True:
            lock.lock()
            for i in range(len(jp)):
                if xp[i]!=None:
                    xp[i].setText(str(xh[jp[i]]))
                    sd+=1
                    print(i)
                
            lock.unlock()
            time.sleep(0.1)    

   


#获取操作员命令，发送控制信号的线程,将控制信号发送到下位机
class Mythread2(QThread):
    # 定义信号,定义参数为int类型
    breakSigna2 = pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self): 
        while True:
            time.sleep(0.1)
            #此处获取操作员命令
            #xxx=gl.get_value('score') 
            if not q.empty():
                xxx=q.get()
                ui.ee.setText(str(xxx))

#界面刷新函数，a是线程发送过来的信号，用于刷新界面
def chuli(a):
    pass
    '''
    global xp
    global xh
    sd=0
    print(a)
    for i in xp:
        #i.setText(a) 
        
        i.setText(str(a[sd]))
        sd+=1
        if sd>1:
            sd=0
    '''
    
  
    #xh.clear()

    '''
    xxx=gl.get_value('score') 
    ui.e7.setText(str(xxx))
    lock.acquire()
    xh.append(random.randint(0,9))
    lock.release()
    '''
   
    #xxx=gl.get_value('score')   #获取值
    #gl.set_value('e2', "23")     #设定值
    '''
    ui.e1.setText(a)
    ui.e2.setText(a)
    ui.e3.setText(a)
    '''


#p1按钮的事件函数
def convert( x,p):
    print(x)
    p.open()
    '''
    Ph.open()
    '''
    
   
    


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    
    #第一种打开子窗口的方式
    #实例化自定义窗口
    #实例化自定义子窗口
    child = QMainWindow()          
    child_ui = tx.Ui_MainWindow()
    child_ui.setupUi(child)
    #打开自定义子窗口
    ui.tx.clicked.connect( child.show ) 
    
    
   
    #第二种打开子窗口的方式
    #实例化阀门窗口
    eh=floatt.Demo("e2",q,lock1)         #"e2代表阀门号。q代表传入子窗口的队列，用于发送控制消息。lock1用于锁住自建全局变量"
    dh=bool.Demo("e1")

    #打开子窗口
    ui.p1.clicked.connect(dh.open)
    ui.p2.clicked.connect(eh.open)


    #第三种打开子窗口的方式
    #重新实例化子窗口
    #Ph=floatt.Demo("e2",q,lock1)         #"e2代表阀门号。q代表传入子窗口的队列，用于发送控制消息。lock1用于锁住自建全局变量"
    #Ph=floatt.Demo()
    #为p1控件绑定事件
    ui.p5.clicked.connect(partial(convert, "p5",floatt.Demo("p5",q,lock1)))
    ui.p6.clicked.connect(partial(convert, "p6",floatt.Demo("p6",q,lock1)))
    ui.p7.clicked.connect(partial(convert, "p7",floatt.Demo("p7",q,lock1)))






    
    #首次运行，根据配置表搜索前面板控件的函数
    click_success()
   
    
    # 创建线程,用于读取信号，自动后台运行
    thread = Mythread()
    thread.breakSignal.connect(chuli)
    thread.start()

    # 创建线程,用于刷新界面信号，自动后台运行
    thread1 = Mythread1()
    thread1.start()

    #创建线程，用于发送控制信号
    thread2 = Mythread2()
    thread2.breakSigna2.connect(chuli)
    thread2.start()



    MainWindow.show()
    sys.exit(app.exec_())