import sys
from PyQt5.QtWidgets import *
# QWidget, QMessageBox, QApplication,QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from time import sleep


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)       
        self.initUI()


    # 登录界面
    def initUI(self):  
        '''登录界面'''             

        self.resize(637,313)      
            #将主窗口放在屏幕中间
        screen = QDesktopWidget().screenGeometry()  #计算屏幕大小
        size = self.geometry() #获取QWidget窗口大小
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2) #将窗口移动到屏幕中间
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint)  #禁止窗口最大化
        self.setFixedSize(self.width(), self.height())   #禁止窗口拉伸
        self.setWindowFlags(Qt.FramelessWindowHint)  #取消窗口边框
        
        #添加窗口背景图片
        palette1 = QPalette() 
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('E:\wanghongfei\three\捕获.PNG')))
        self.setPalette(palette1)

        #添加关闭按钮
        self.Clooo=QPushButton('x',self)
        self.Clooo.setGeometry(610,10,17,15)
        self.Clooo.clicked.connect(self.on_pushButton_clicked)
        # self.on_pushButton_clicked()
        #添加最小化按钮
        self.Minnn=QPushButton('-',self)
        self.Minnn.setGeometry(590,10,17,15)
        self.Minnn.clicked.connect(self.on_pushButton_2_clicked)
        

        nameLb1 = QLabel('账号:',self)
        nameLb2 = QLabel('密码:',self)
        nameLb3 = QLabel('注册账号',self)
        nameLb4 = QLabel('修改密码',self)
        self.nameEd1 = QLineEdit(self)     #账号输入框
        self.nameEd1.setGeometry(280,90,120,30) #文本框大小和位置
        self.nameEd2 = QLineEdit(self)     #密码输入框
        self.nameEd2.setGeometry(280,125,120,30) #文本框大小和位置
        # self.WAccount=self.nameEd1.text()
        # self.WPassword=self.nameEd2.text() # 获取文本框内容 :密码
        nameLb1.move(240,90)
        nameLb2.move(240,125)
        # nameEd1.move(310,60)
        # nameEd2.move(310,95)
        nameLb3.move(230,165)
        nameLb4.move(350,165)
        self.nameEd1.setPlaceholderText('账号')   #输入框浮显文字
        self.nameEd2.setPlaceholderText('密码')
        self.nameEd1.setMaxLength(16)      #输入最大字符16位
        self.nameEd2.setMaxLength(16)
        self.nameEd2.setEchoMode(QLineEdit.Password)  #密码掩码
        self.btn1=QPushButton('安全登录',self)
        self.btn1.setGeometry(237,240,160,40)
        self.btn1.clicked.connect(self.addNum)

    
    #将主窗口放在屏幕中间
    def center(self):
        screen = QDesktopWidget().screenGeometry()  #计算屏幕大小
        size = self.geometry() #获取QWidget窗口大小
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2) #将窗口移动到屏幕中间


    #鼠标可以拖动窗口 
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton: 
            self.m_flag=True 
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置 
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor)) #更改鼠标图标 
    def mouseMoveEvent(self, QMouseEvent): 
        if Qt.LeftButton and self.m_flag: 
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置 
            QMouseEvent.accept() 
    def mouseReleaseEvent(self, QMouseEvent): 
        self.m_flag=False 
        self.setCursor(QCursor(Qt.ArrowCursor))

    #重写关闭 和 最小化按钮
    def on_pushButton_clicked(self): 
        """ 关闭窗口 """ 
        self.close() 
    def on_pushButton_2_clicked(self): 
        """ 最小化窗口 """ 
        # self.showMinimized()
        self.showMinimized()  #无法实现！！！


   #获取文本框的 账号和密码 进行登录
    def addNum(self):
        self.WAccount=self.nameEd1.text()
        self.WPassword=self.nameEd2.text() # 获取文本框内容 :密码
        # print(type(self.WAccount),self.WPassword)

    #输入账号和密码 登录不同的界面
        # 经理登录
        if self.WAccount == '111111':
            if self.WPassword == '000000':
                # a = initUI2()
                # self.close
                # a = initUI2()     
                a = userForm()
                a.show()
                MainWindow.close()
                sys.exit(a.exec_())
            else:
                self.showdialog()
                
        # #管理员
        # elif self.WAccount == administratorName:
        #     if self.WPassword == administratorPassword:
        #         self.initUI3()
        #     else:
        #         self.showdialog()

        # #营业员
        # elif self.WAccount == employeesName:
        #     if self.WPassword == employeesPassword:
        #         self.initUI4()
        #     else:
        #         self.showdialog()


        #输入有误
        else:
            self.showdialog()

    #账号或密码输入有误，弹窗提示
    def showdialog(self): 
        reply = QMessageBox.information(self,'错误','您输入的账号或密码有误！',QMessageBox.Ok)



    #限制文本输入最少6个字符
    def Lblong(self,nameEd1):
        if len(nameEd1) < 6:
            pass                 


    def link_clicked():
        pass  #当鼠标点击...时触发事件
        

    def showMsg(self):
        QMessageBox.information(widget,'信息提示框','Ok 弹出测试信息',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)


    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
            "你确定退出吗?", QMessageBox.Yes| 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        



#经理
class initUI2(QWidget):
    def __init__(self):  
        '''经理界面'''     
        super().__init__()
        self.initUI()
        # try:
        #     sys.exit(self.w.exec_())
        # except:
        #     pass



    def initUI(self):
        abb = QApplication(sys.argv)
        self.w = QWidget()
        self.w.setGeometry(400, 300, 800, 800)        
        self.w.setWindowTitle('经理界面') 
        lab1=QLabel()  #添加背景图片
        lab1.setPixmap(QPixmap('E:\wanghongfei\three\捕获.PNG'))
        vbox=QVBoxLayout()
        vbox.addWidget(lab1)
        self.w.setLayout(vbox)
        self.w.show()
        sys.exit(abb.exec_())


#管理员
class initUI3(QWidget):
    def __init__(self):      
        super().__init__()
        self.initUI()



#营业员
class initUI4(QWidget):
    def __init__(self):      
        super().__init__()
        self.initUI()

    
    # def initUI4(self):  
    #     '''营业员界面'''  
    #     self.setGeometry(400, 300, 400, 260)        
    #     self.setWindowTitle('营业员界面') 
    #     lab1=QLabel()  #添加背景图片
    #     lab1.setPixmap(QPixmap('/home/tarena/wlbc/GUI/send.jpg'))
    #     vbox=QVBoxLayout()
    #     vbox.addWidget(lab1)
    #     self.setLayout(vbox)     


class userForm(QDialog):
    def __init__(self, parent = None):
        super(userForm, self).__init__(parent)
        usrName = QLabel("UserName")
        passWd = QLabel("PassWd")
        self.userNameLineEdit = QLineEdit()
        self.passWdLineEdit = QLineEdit()
        self.passWdLineEdit.setEchoMode(QLineEdit.Password)

        gridLayout = QGridLayout()
        gridLayout.addWidget(usrName, 0, 0, 1, 1)
        gridLayout.addWidget(passWd, 1, 0, 1, 1)
        gridLayout.addWidget(self.userNameLineEdit,0,1,1,3)
        gridLayout.addWidget(self.passWdLineEdit,1,1,1,3)

        okPushBtn = QPushButton("OK")
        cancelPushBtn = QPushButton("Cancle")
        btnLayout = QHBoxLayout()
        btnLayout.setSpacing(60)
        btnLayout.addWidget(okPushBtn)
        btnLayout.addWidget(cancelPushBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40,40,40,40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)
        self.setLayout(dlgLayout)
        self.setWindowTitle("user WinForm")
        self.resize(200,200)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    # ex2 = initUI2()
    ex.show()
    try:
        sys.exit(app.exec_())
    except:
        pass