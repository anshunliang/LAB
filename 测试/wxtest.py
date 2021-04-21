from PyQt5 import QtWidgets,QtCore,QtGui
import tushare as ts
import pyqtgraph as pg
import sys
import datetime
import traceback
import numpy as np
 
class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CPU使用率监控 - 州的先生https://zmister.com")
        self.main_widget = QtWidgets.QWidget()  # 创建一个主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建一个网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置主部件的布局为网格
        self.setCentralWidget(self.main_widget)  # 设置窗口默认部件
 
        self.plot_widget = QtWidgets.QWidget()  # 实例化一个widget部件作为K线图部件
        self.plot_layout = QtWidgets.QGridLayout()  # 实例化一个网格布局层
        self.plot_widget.setLayout(self.plot_layout)  # 设置线图部件的布局层
        self.plot_plt = pg.PlotWidget()  # 实例化一个绘图部件
        self.plot_plt.showGrid(x=True,y=True) # 显示图形网格
        self.plot_layout.addWidget(self.plot_plt)  # 添加绘图部件到线图部件的网格布局层
        # 将上述部件添加到布局层中
        self.main_layout.addWidget(self.plot_widget, 1, 0, 3, 3)
 
        self.setCentralWidget(self.main_widget)
 
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())
 
 
if __name__ == '__main__':
    main()
 