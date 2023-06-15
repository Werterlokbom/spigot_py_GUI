import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *


app = QApplication(sys.argv)

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1481, 920)
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*[myclass=help]{\n"
                                 "border:0px;\n"
                                 "color:rgb(14, 191, 255);\n"
                                 "}\n"
                                 "*[myclass=close]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(255, 0, 0);\n"
                                 "}\n"
                                 "*[myclass=min]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(134, 134, 134)\n"
                                 "}\n"
                                 "*[myclass=fullscreen]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(134, 134, 134)\n"
                                 "}\n"
                                 "*[myclass=help]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(134, 134, 134);\n"
                                 "color:rgb(79, 223, 255)\n"
                                 "}\n"
                                 "*[myclass=di_ceng]{\n"
                                 "background: rgb(85, 85, 85);\n"
                                 "}\n"
                                 "\n"
                                 "*[myclass=close]{\n"
                                 "image: url(:/gui/window_close_focus2x.png)\n"
                                 "}\n"
                                 "*[myclass=min]{\n"
                                 "image:url(:/gui/window_minimize_focus2x.png)\n"
                                 "}\n"
                                 "*[myclass=fullscreen]{\n"
                                 "image:url(:/gui/checkbox_unchecked_focus2x.png)\n"
                                 "}\n"
                                 "*[myclass=titlebar]{\n"
                                 "background: rgb(65, 65, 65);\n"
                                 "}\n"
                                 "*[myclass=searchbox]{\n"
                                 "border:0;\n"
                                 "background:rgb(94, 94, 94)\n"
                                 "}\n"
                                 "*[myclass=searchbox]:hover{\n"
                                 "border:0;\n"
                                 "background:rgb(198, 198, 198)\n"
                                 "}\n"
                                 "*[myclass=op]{\n"
                                 "background: rgb(65, 65, 65);\n"
                                 "}\n"
                                 "*"
                                 "[myclass=useravatar]{\n"
                                 "image:url(:/gui/OIP-C.jpg)\n"
                                 "}\n"
                                 "*[myclass=username]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 "background:rgb(52, 52, 52);\n"
                                 "}\n"
                                 "*[myclass=userinfo]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 "background:rgb(52, 52, 52);\n"
                                 "imge:url(:/gui/avatar.png);\n"
                                 "}\n"
                                 "*[myclass=userloginout]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 "background:rgb(52, 52, 52)\n"
                                 "}\n"
                                 "*[myclass=ctrlsever]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 "background:rgb(52, 52, 52)\n"
                                 "}\n"
                                 "*[myclass=history]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 "background:rgb(52, 52, 52)\n"
                                 "}\n"
                                 "*[myclass=settings]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 "background:rgb(52, 52, 52)\n"
                                 "}\n"
                                 "*[myclass=username]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 "}\n"
                                 "*[myclass=userinfo]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(0, 160, 163);\n"
                                 "}\n"
                                 "*[myclass=userloginout]:hover{\n"
                                 "border:0px;\n"
                                 "color:red;\n"
                                 "background:rgb(0, 160, 163);\n"
                                 "}\n"
                                 "*[myclass=ctrlsever]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(0, 160, 163);\n"
                                 "}\n"
                                 "*[myclass=hi"
                                 "story]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(0, 160, 163);\n"
                                 "}\n"
                                 "*[myclass=settings]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(0, 160, 163);\n"
                                 "}\n"
                                 "*[myclass=search]{\n"
                                 "border:0;\n"
                                 "color:rgb(0, 255, 255);\n"
                                 "background:rgb(94, 94, 94)\n"
                                 "}\n"
                                 "*[myclass=search]:hover{\n"
                                 "border:2 solid rgb(0, 255, 255);\n"
                                 "color:rgb(0, 255, 255);\n"
                                 "background:rgb(94, 94, 94)\n"
                                 "}\n"
                                 "*[myclass=guildtext]{\n"
                                 "color:rgb(170, 255, 255);\n"
                                 "}\n"
                                 "*[myclass=guildtext2]{\n"
                                 "color:rgb(0, 166, 255);\n"
                                 "}\n"
                                 "*[myclass=about]{\n"
                                 "color:rgb(89, 134, 131);\n"
                                 "}\n"
                                 "*[myclass=license]{\n"
                                 "color:rgb(89, 134, 131);\n"
                                 "}\n"
                                 "*[myclass=about]:hover{\n"
                                 "color:rgb(170, 255, 255);\n"
                                 "}\n"
                                 "*[myclass=license]:hover{\n"
                                 "color:rgb(170, 255, 255);\n"
                                 "}\n"
                                 "*[myclass=opear1]{\n"
                                 "image:url(:/gui/nosever.png)\n"
                                 "}\n"
                                 "*[myclass=tip1]{\n"
                                 "color:rgb(255, 255, 255);\n"
                                 "}\n"
                                 "*[myclass=open]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 "background:rgb(52, 52, 52)\n"
                                 "}\n"
                                 "*[myclass=book]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 ""
                                 "background:rgb(52, 52, 52)\n"
                                 "}\n"
                                 "*[myclass=feedback]{\n"
                                 "border:0px;\n"
                                 "color:white;\n"
                                 "background:rgb(52, 52, 52)\n"
                                 "}\n"
                                 "*[myclass=open]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(107, 107, 107);\n"
                                 "}\n"
                                 "*[myclass=book]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(107, 107, 107);\n"
                                 "}\n"
                                 "*[myclass=feedback]:hover{\n"
                                 "border:0px;\n"
                                 "background:rgb(107, 107, 107);\n"
                                 "}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.di_ceng = QWidget(self.centralwidget)
        self.di_ceng.setObjectName(u"di_ceng")
        self.di_ceng.setGeometry(QRect(0, 0, 1481, 931))
        self.titlebar = QFrame(self.di_ceng)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setGeometry(QRect(0, 0, 1481, 51))
        self.titlebar.setFrameShape(QFrame.StyledPanel)
        self.titlebar.setFrameShadow(QFrame.Raised)
        self.winbutton = QFrame(self.titlebar)
        self.winbutton.setObjectName(u"winbutton")
        self.winbutton.setGeometry(QRect(1280, 0, 201, 51))
        self.winbutton.setFrameShape(QFrame.StyledPanel)
        self.winbutton.setFrameShadow(QFrame.Raised)
        self.help = QPushButton(self.winbutton)
        self.help.setObjectName(u"help")
        self.help.setGeometry(QRect(0, 0, 51, 51))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(36)
        self.help.setFont(font1)
        self.help.setFlat(True)
        self.fullscreen = QPushButton(self.winbutton)
        self.fullscreen.setObjectName(u"fullscreen")
        self.fullscreen.setGeometry(QRect(50, 0, 51, 51))
        self.fullscreen.setCursor(QCursor(Qt.ArrowCursor))
        self.fullscreen.setFlat(True)
        self.min = QPushButton(self.winbutton)
        self.min.setObjectName(u"min")
        self.min.setGeometry(QRect(100, 0, 51, 51))
        self.min.setFlat(True)
        self.close = QPushButton(self.winbutton)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(150, 0, 51, 51))
        self.close.setStyleSheet(u"")
        self.close.setFlat(True)
        self.close.raise_()
        self.min.raise_()
        self.fullscreen.raise_()
        self.help.raise_()
        self.searchbox = QLineEdit(self.titlebar)
        self.searchbox.setObjectName(u"searchbox")
        self.searchbox.setGeometry(QRect(4, 4, 621, 43))
        self.searchbox.setFont(font)
        self.pushButton = QPushButton(self.titlebar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(625, 4, 61, 43))
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(16)
        font2.setItalic(True)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setFlat(False)
        self.main = QFrame(self.di_ceng)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(0, 50, 1481, 871))
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.op = QWidget(self.main)
        self.op.setObjectName(u"op")
        self.op.setGeometry(QRect(0, 0, 411, 871))
        self.useravatar = QLabel(self.op)
        self.useravatar.setObjectName(u"useravatar")
        self.useravatar.setGeometry(QRect(0, 0, 181, 161))
        self.username = QLabel(self.op)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(180, 0, 231, 61))
        self.username.setFont(font)
        self.userinfo = QPushButton(self.op)
        self.userinfo.setObjectName(u"userinfo")
        self.userinfo.setGeometry(QRect(180, 60, 231, 51))
        font3 = QFont()
        font3.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font3.setPointSize(14)
        self.userinfo.setFont(font3)
        self.userinfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.userloginout = QPushButton(self.op)
        self.userloginout.setObjectName(u"userloginout")
        self.userloginout.setGeometry(QRect(180, 110, 231, 51))
        self.userloginout.setFont(font)
        self.userloginout.setCursor(QCursor(Qt.PointingHandCursor))
        self.ctrlsrver = QPushButton(self.op)
        self.ctrlsrver.setObjectName(u"ctrlsrver")
        self.ctrlsrver.setGeometry(QRect(0, 160, 411, 101))
        font4 = QFont()
        font4.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font4.setPointSize(20)
        self.ctrlsrver.setFont(font4)
        self.ctrlsrver.setCursor(QCursor(Qt.PointingHandCursor))
        self.history = QPushButton(self.op)
        self.history.setObjectName(u"history")
        self.history.setGeometry(QRect(0, 361, 411, 101))
        self.history.setFont(font4)
        self.history.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings = QPushButton(self.op)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(0, 260, 411, 101))
        self.settings.setFont(font4)
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.guild = QFrame(self.op)
        self.guild.setObjectName(u"guild")
        self.guild.setGeometry(QRect(-1, 619, 411, 161))
        self.guild.setFrameShape(QFrame.StyledPanel)
        self.guild.setFrameShadow(QFrame.Raised)
        self.guildtext = QLabel(self.guild)
        self.guildtext.setObjectName(u"guildtext")
        self.guildtext.setGeometry(QRect(10, 10, 101, 31))
        font5 = QFont()
        font5.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font5.setPointSize(22)
        self.guildtext.setFont(font5)
        self.guildtext2 = QLabel(self.guild)
        self.guildtext2.setObjectName(u"guildtext2")
        self.guildtext2.setGeometry(QRect(10, 50, 401, 111))
        font6 = QFont()
        font6.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font6.setPointSize(26)
        font6.setBold(True)
        font6.setItalic(True)
        font6.setUnderline(True)
        font6.setWeight(75)
        font6.setKerning(True)
        self.guildtext2.setFont(font6)
        self.more = QFrame(self.op)
        self.more.setObjectName(u"more")
        self.more.setGeometry(QRect(0, 780, 411, 91))
        self.more.setFrameShape(QFrame.StyledPanel)
        self.more.setFrameShadow(QFrame.Raised)
        self.about = QLabel(self.more)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(10, 60, 41, 21))
        font7 = QFont()
        font7.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font7.setPointSize(11)
        font7.setUnderline(True)
        self.about.setFont(font7)
        self.about.setCursor(QCursor(Qt.PointingHandCursor))
        self.license = QLabel(self.more)
        self.license.setObjectName(u"license")
        self.license.setGeometry(QRect(220, 60, 61, 21))
        font8 = QFont()
        font8.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font8.setPointSize(12)
        font8.setUnderline(True)
        self.license.setFont(font8)
        self.license.setCursor(QCursor(Qt.PointingHandCursor))
        self.opear1 = QLabel(self.main)
        self.opear1.setObjectName(u"opear1")
        self.opear1.setGeometry(QRect(600, 0, 731, 491))
        self.tip1 = QLabel(self.main)
        self.tip1.setObjectName(u"tip1")
        self.tip1.setGeometry(QRect(530, 470, 851, 111))
        font9 = QFont()
        font9.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font9.setPointSize(48)
        self.tip1.setFont(font9)
        self.open = QPushButton(self.main)
        self.open.setObjectName(u"open")
        self.open.setGeometry(QRect(530, 590, 231, 251))
        font10 = QFont()
        font10.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font10.setPointSize(18)
        self.open.setFont(font10)
        self.open.setCursor(QCursor(Qt.PointingHandCursor))
        self.open.setFlat(True)
        self.book = QPushButton(self.main)
        self.book.setObjectName(u"book")
        self.book.setGeometry(QRect(820, 590, 231, 251))
        self.book.setMaximumSize(QSize(16777215, 16777215))
        self.book.setFont(font10)
        self.book.setCursor(QCursor(Qt.PointingHandCursor))
        self.book.setFlat(True)
        self.feedback = QPushButton(self.main)
        self.feedback.setObjectName(u"feedback")
        self.feedback.setGeometry(QRect(1110, 590, 231, 251))
        self.feedback.setFont(font10)
        self.feedback.setCursor(QCursor(Qt.PointingHandCursor))
        self.feedback.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MC_SEVER_GUI\u5ba2\u6237\u7aef", None))
        self.di_ceng.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"di_ceng", None))
        self.titlebar.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"titlebar", None))
        self.help.setText(QCoreApplication.translate(
            "MainWindow", u"  \uff1f", None))
        self.help.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"help", None))
        self.fullscreen.setText("")
        self.fullscreen.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"fullscreen", None))
        self.min.setText("")
        self.min.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"min", None))
        self.close.setText("")
        self.close.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"close", None))
        self.searchbox.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"\u641c\u7d22\u73a9\u5bb6,\u670d\u52a1\u5668...", None))
        self.searchbox.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"searchbox", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"\u641c\u7d22", None))
        self.pushButton.setProperty(
            "myclass", QCoreApplication.translate("MainWindow", u"search", None))
        self.main.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"main", None))
        self.op.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"op", None))
        self.useravatar.setText("")
        self.useravatar.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"useravatar", None))
        self.username.setText(QCoreApplication.translate(
            "MainWindow", u"    123456", None))
        self.username.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"username", None))
        self.userinfo.setText(QCoreApplication.translate(
            "MainWindow", u"        \u7528\u6237\u4fe1\u606f", None))
        self.userinfo.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"userinfo", None))
        self.userloginout.setText(QCoreApplication.translate(
            "MainWindow", u"        \u9000\u51fa\u767b\u5f55", None))
        self.userloginout.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"userloginout", None))
        self.ctrlsrver.setText(QCoreApplication.translate(
            "MainWindow", u"                  \u7ba1\u7406\u670d\u52a1\u5668", None))
        self.ctrlsrver.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"ctrlsever", None))
        self.history.setText(QCoreApplication.translate(
            "MainWindow", u"        \u8bbe\u7f6e", None))
        self.history.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"settings", None))
        self.settings.setText(QCoreApplication.translate(
            "MainWindow", u"               \u5386\u53f2\u8bb0\u5f55", None))
        self.settings.setProperty(
            "myclass", QCoreApplication.translate("MainWindow", u"history", None))
        self.guildtext.setText(QCoreApplication.translate(
            "MainWindow", u" \u5f53\u524d:", None))
        self.guildtext.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"guildtext", None))
        self.guildtext2.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e3b\u9875", None))
        self.guildtext2.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"guildtext2", None))
        self.about.setText(QCoreApplication.translate(
            "MainWindow", u"\u5173\u4e8e...", None))
        self.about.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"about", None))
        self.license.setText(QCoreApplication.translate(
            "MainWindow", u"\u8bb8\u53ef\u8bc1...", None))
        self.license.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"license", None))
        self.opear1.setText("")
        self.opear1.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"opear1", None))
        self.tip1.setText(QCoreApplication.translate(
            "MainWindow", u"emm....\u4f3c\u4e4e\u8fd9\u91cc\u6ca1\u6709\u5185\u5bb9...", None))
        self.tip1.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"tip1", None))
        self.open.setText(QCoreApplication.translate("MainWindow", u"\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "\u521b\u5efa/\u6253\u5f00\u672c\u5730\u670d\u52a1\u5668", None))
        self.open.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"open", None))
        self.book.setText(QCoreApplication.translate("MainWindow", u"\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "\u67e5\u770b\u6559\u7a0b", None))
        self.book.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"book", None))
        self.feedback.setText(QCoreApplication.translate("MainWindow", u"\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "\u53cd\u9988", None))
        self.feedback.setProperty("myclass", QCoreApplication.translate(
            "MainWindow", u"feedback", None))
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
    # retranslateUi


class MainWindow(QMainWindow):
    def __init__(self, parent=None, **kargs) -> None:
        super(MainWindow, self).__init__(parent)
        self.win = QMainWindow()
        self.main = Ui_MainWindow(self.win)
        # self.resize(500, 600)
        # self.setWindowTitle('测试')
        # self.setWindowIcon(QIcon(QPixmap.fromImage(kargs['icon'])))

    def start_win(self):
        self.win.show()
        sys.exit(app.exec_())
