from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
import os


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(925, 578)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.frame_2 = QtWidgets.QFrame(self.centralwidget)
		self.frame_2.setGeometry(QtCore.QRect(0, 0, 60, 578))
		self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: #EEEEEE;\n"
"}")
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.frame_3 = QtWidgets.QFrame(self.frame_2)
		self.frame_3.setGeometry(QtCore.QRect(12, 40, 38, 38))
		self.frame_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.frame_3.setStyleSheet("")
		self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.label = QtWidgets.QLabel(self.frame_3)
		self.label.setGeometry(QtCore.QRect(8, 9, 22, 20))
		self.label.setStyleSheet("border: none;")
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap(":/images/Images/chat.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")
		self.frame_4 = QtWidgets.QFrame(self.frame_2)
		self.frame_4.setGeometry(QtCore.QRect(12, 510, 38, 38))
		self.frame_4.setStyleSheet("QFrame{\n"
"    background-color: #D8D8D8;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #4B7BEC;\n"
"}")
		self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_4.setObjectName("frame_4")
		self.label_2 = QtWidgets.QLabel(self.frame_4)
		self.label_2.setGeometry(QtCore.QRect(8, 8, 22, 22))
		self.label_2.setStyleSheet("border: none;")
		self.label_2.setText("")
		self.label_2.setPixmap(QtGui.QPixmap(":/images/Images/settings.png"))
		self.label_2.setScaledContents(True)
		self.label_2.setObjectName("label_2")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(60, 0, 861, 578))
		self.frame.setStyleSheet("QFrame{\n"
"    background-color: #F5F5F5;\n"
"}")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.pushButton = QtWidgets.QPushButton(self.frame)
		self.pushButton.setGeometry(QtCore.QRect(60, 50, 152, 35))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(9)
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(50)
		font.setStrikeOut(False)
		self.pushButton.setFont(font)
		self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.pushButton.setStyleSheet("QPushButton {\n"
"  background-color: transparent;\n"
"  border: 2px solid #1A1A1A;\n"
"  border-radius: 10px;\n"
"  color: #3B3B3B;\n"
"  margin: 0;\n"
"  min-width: 0;\n"
"  outline: none;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: #fff;\n"
"  background-color: #1A1A1A;\n"
"}")
		self.pushButton.setAutoDefault(False)
		self.pushButton.setDefault(False)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.upload_templates)
		
		self.pushButton_1 = QtWidgets.QPushButton(self.frame)
		self.pushButton_1.setGeometry(QtCore.QRect(230, 50, 152, 35))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(9)
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(50)
		font.setStrikeOut(False)
		self.pushButton_1.setFont(font)
		self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.pushButton_1.setStyleSheet("QPushButton {\n"
"  background-color: transparent;\n"
"  border: 2px solid #1A1A1A;\n"
"  border-radius: 10px;\n"
"  color: #3B3B3B;\n"
"  margin: 0;\n"
"  min-width: 0;\n"
"  outline: none;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: #fff;\n"
"  background-color: #1A1A1A;\n"
"}")
		self.pushButton_1.setAutoDefault(False)
		self.pushButton_1.setDefault(False)
		self.pushButton_1.setObjectName("pushButton_1")
		# self.pushButton_1.clicked.connect()

		self.label_3 = QtWidgets.QLabel(self.frame)
		self.label_3.setGeometry(QtCore.QRect(10, 10, 111, 31))
		font = QtGui.QFont()
		font.setFamily("Inter Semi Bold")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.frame_9 = QtWidgets.QFrame(self.frame)
		self.frame_9.setGeometry(QtCore.QRect(42, 110, 332, 100))
		self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_9.setObjectName("frame_9")
		
		self.frame_5 = QtWidgets.QFrame(self.frame_9)
		self.frame_5.sender = self.frame_5
		self.frame_5.setGeometry(QtCore.QRect(0, 0, 152, 100))
		self.frame_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_5.setObjectName("frame_5")
		self.frame_6 = QtWidgets.QFrame(self.frame_5)
		self.frame_6.setGeometry(QtCore.QRect(19, 9, 111, 61))
		self.frame_6.setStyleSheet("QFrame{\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
		self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_6.setObjectName("frame_6")
		self.label_4 = QtWidgets.QLabel(self.frame_5)
		self.label_4.setGeometry(QtCore.QRect(4, 80, 144, 13))
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.label_4.setStyleSheet("border: none;")
		self.frame_7 = QtWidgets.QFrame(self.frame_9)
		self.frame_7.setGeometry(QtCore.QRect(180, 0, 152, 100))
		self.frame_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_7.setObjectName("frame_7")
		self.frame_8 = QtWidgets.QFrame(self.frame_7)
		self.frame_8.setGeometry(QtCore.QRect(19, 9, 111, 61))
		self.frame_8.setStyleSheet("QFrame{\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: #1b1c1f;\n"
"}")
		self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_8.setObjectName("frame_8")
		self.label_5 = QtWidgets.QLabel(self.frame_7)
		self.label_5.setGeometry(QtCore.QRect(4, 80, 144, 13))
		self.label_5.setStyleSheet("border: none;")
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Добавить шаблоны"))
		self.pushButton_1.setText(_translate("MainWindow", "Собрать новые письма"))
		self.label_3.setText(_translate("MainWindow", "Настройки"))
		self.label_4.setText(_translate("MainWindow", "Светлая тема"))
		self.label_5.setText(_translate("MainWindow", "Темная тема"))
	
	def upload_templates(self):
		if not os.path.exists("Templates"):
			os.makedirs("Templates")
		option = QtWidgets.QFileDialog.Option()
		# option |= QtWidgets.QFileDialog.DontUseNativeDialog
		dialog = QtWidgets.QFileDialog()
		dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
		fileName, _ = dialog.getOpenFileNames(None, "Выберите файл", "", "Microsoft Word (*.docx *.doc)", options=option)
		for name in fileName:
			shutil.copy(name, "Templates")


import resources_rc
