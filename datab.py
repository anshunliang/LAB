# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datab.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,queue,time
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout,QLineEdit
import globalvar as gl
import gwh as gw
import shuju as sj

xp1=[]
xp1index=[]

class Ui_MainWindow(object):
    def __init__(self):          
        super(Ui_MainWindow, self).__init__() 
        self.sub_thread = subThread()
        self.sub_thread.sub_signal.connect(self.set_label_func)
    
    #重写打开事件
    def open(self):
        print("fffgddddddddddddg")
        global xp1index
        global xp1
        j1=0
        for i in gw.get():
            try:
                if self.findChild(QLineEdit,i):   #根据反馈AI工位号获取前面板控件
                    xp1.append(self.findChild(QLineEdit,i))
                    xp1index.append(j1)
                    j1+=1
                else:
                    j1+=1
            except:
                pass
        j1=0
        #自动开始线程
        self.sub_thread.is_on = True         # 5
        self.sub_thread.start()
        print("open")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)   #顶层显示
        self.showNormal()       #正常化显示，用于最小化窗口后，点击按钮，正常化显示窗口
        self.show()
        
    #重写关闭事件
    #重写关闭事件
    def closeEvent(self, event):
      
        self.sub_thread.is_on = False
        self.sub_thread.count = 0
        self.close()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1285, 825)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 31, 16))
        self.label_5.setObjectName("label_5")
        self.e9 = QtWidgets.QLineEdit(self.centralwidget)
        self.e9.setGeometry(QtCore.QRect(110, 100, 72, 24))
        self.e9.setObjectName("e9")
        self.e7 = QtWidgets.QLineEdit(self.centralwidget)
        self.e7.setGeometry(QtCore.QRect(110, 20, 72, 24))
        self.e7.setObjectName("e7")
        self.e10 = QtWidgets.QLineEdit(self.centralwidget)
        self.e10.setGeometry(QtCore.QRect(110, 140, 72, 24))
        self.e10.setObjectName("e10")
        self.e8 = QtWidgets.QLineEdit(self.centralwidget)
        self.e8.setGeometry(QtCore.QRect(110, 60, 72, 24))
        self.e8.setObjectName("e8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "e7"))
        self.label_3.setText(_translate("MainWindow", "e8"))
        self.label_4.setText(_translate("MainWindow", "e9"))
        self.label_5.setText(_translate("MainWindow", "e10"))


    
    #接收到子线程信号的处理函数,在子窗口显示反馈信息
    def set_label_func(self, fs0,fs1):
        h=gw.get()
        s=sj.get()

        
        global xp1index
        global xp1
        for i,j in zip(xp1,xp1index):
            i.setText(s[j])
      
        
#子窗口用于刷新信号的线程

class subThread(QThread):
    #定义线程传递的信号
    sub_signal = pyqtSignal(str,str)

    def __init__(self):
        super(subThread, self).__init__()

    def run(self):
        a=1
        while self.is_on:   # 2
            self.sub_signal.emit("world",str(a))  #发送获取的值,用于更新子窗口的数
            a=a+1
            time.sleep(0.3)