from PyQt5 import QtCore, QtGui, QtWidgets
import os
from database import Database


class MyFrameBack(QtWidgets.QFrame):
	def __init__(self, parent, label, grid, color, pat):
		super().__init__(parent)
		self.label = label
		self.grid = grid
		self.pat = pat
		self.color = color
		self.setObjectName("frame_11")
	
	def set_color(self, color):
		self.color = color

	def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
		if event.button() == QtCore.Qt.LeftButton:
			back = 0
			# self.pat = f"Messages/{self.label.text()}{self.pat}"
			if self.pat.startswith("//"):
				self.pat = self.pat[1:]
			self.pat = os.path.dirname(self.pat)

			for i in reversed(range(self.grid.count())):
				widgets = self.grid.itemAt(i).widget()
				widgets.setParent(None)
				widgets.hide()

			if self.pat != "/":
				back = 1
				frame_11 = MyFrameBack(None, self.label, self.grid, self.color, self.pat)
				frame_11.setFixedSize(110, 110)
				frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
				frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
				label_10 = QtWidgets.QLabel(frame_11)
				label_10.setGeometry(QtCore.QRect(30, 15, 50, 50))
				label_10.setText("")
				label_10.setPixmap(QtGui.QPixmap(":/images/Images/back.png"))
				label_10.setScaledContents(True)
				label_10.setObjectName("label_10")
				label_11 = QtWidgets.QLabel(frame_11)
				label_11.setGeometry(QtCore.QRect(0, 70, 110, 40))
				label_11.setAutoFillBackground(False)
				label_11.setScaledContents(False)
				label_11.setAlignment(QtCore.Qt.AlignCenter)
				label_11.setWordWrap(True)
				label_11.setObjectName("label_11")
				label_11.setStyleSheet(f"color: {self.color}")
				label_11.setMinimumHeight(50)
				label_11.setText(f"back")
					
				frame_11.setContentsMargins(0, 0, 0, 0)
				row, col = 0, 0
				self.grid.addWidget(frame_11, row, col, alignment=QtCore.Qt.AlignTop)

			folders = [d for d in os.listdir(f"Messages/{self.label.text()}{self.pat}") if os.path.isdir(os.path.join(f"Messages/{self.label.text()}{self.pat}", d))]
			files = [f for f in os.listdir(f"Messages/{self.label.text()}{self.pat}") if os.path.isfile(os.path.join(f"Messages/{self.label.text()}{self.pat}", f))]

			for i in range(len(folders)):
				frame_11 = MyFrame(None, self.label, self.grid, self.color, pat=self.pat)
				frame_11.setFixedSize(110, 110)
				frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
				frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
				label_10 = QtWidgets.QLabel(frame_11)
				label_10.setGeometry(QtCore.QRect(30, 15, 50, 50))
				label_10.setText("")
				label_10.setPixmap(QtGui.QPixmap(":/images/Images/folder.png"))
				label_10.setScaledContents(True)
				label_10.setObjectName("label_10")
				label_11 = QtWidgets.QLabel(frame_11)
				label_11.setGeometry(QtCore.QRect(0, 70, 110, 40))
				label_11.setAutoFillBackground(False)
				label_11.setScaledContents(False)
				label_11.setAlignment(QtCore.Qt.AlignCenter)
				label_11.setWordWrap(True)
				label_11.setObjectName("label_11")
				label_11.setStyleSheet(f"color: {self.color}")
				label_11.setMinimumHeight(50)
				label_11.setText(f"{folders[i]}")
				
				frame_11.setContentsMargins(0, 0, 0, 0)
				row, col = divmod(i+back, 3)
				self.grid.addWidget(frame_11, row, col, alignment=QtCore.Qt.AlignTop)
			
			for i in range(len(files)):
				frame_11 = MyFrameFile(None, self.label, pat=self.pat)
				frame_11.setFixedSize(110, 110)
				frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
				frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
				label_10 = QtWidgets.QLabel(frame_11)
				label_10.setGeometry(QtCore.QRect(30, 15, 50, 50))
				label_10.setText("")
				if files[i].endswith(".jpg") or files[i].endswith(".jpeg"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/jpeg.png"))
				elif files[i].endswith(".png"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/png.png"))
				elif files[i].endswith(".doc") or files[i].endswith(".docx"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/docx.png"))
				elif files[i].endswith(".pdf"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/pdf.png"))
				elif files[i].endswith(".txt") or files[i].endswith(".text"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/txt.png"))
				else:
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/file.png"))
				label_10.setScaledContents(True)
				label_10.setObjectName("label_10")
				label_11 = QtWidgets.QLabel(frame_11)
				label_11.setGeometry(QtCore.QRect(0, 70, 110, 40))
				label_11.setAutoFillBackground(False)
				label_11.setScaledContents(False)
				label_11.setAlignment(QtCore.Qt.AlignCenter)
				label_11.setWordWrap(True)
				label_11.setObjectName("label_11")
				label_11.setStyleSheet(f"color: {self.color}")
				label_11.setMinimumHeight(50)
				label_11.setText(f"{files[i]}")
				
				frame_11.setContentsMargins(0, 0, 0, 0)
				row, col = divmod(i+len(folders)+back, 3)
				self.grid.addWidget(frame_11, row, col, alignment=QtCore.Qt.AlignTop)


class MyFrameFile(QtWidgets.QFrame):
	def __init__(self, parent, label, pat=""):
		super().__init__(parent)
		self.label = label
		self.pat = pat
		self.setObjectName("frame_11")
	
	def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
		if event.button() == QtCore.Qt.LeftButton:
			os.startfile(os.path.normpath(f"Messages/{self.label.text()}{self.pat}/{self.findChild(QtWidgets.QLabel, 'label_11').text()}"))


class MyFrame(QtWidgets.QFrame):
	def __init__(self, parent, label, grid, color, pat=""):
		super().__init__(parent)
		self.label = label
		self.grid = grid
		self.pat = pat
		self.color = color
		self.setObjectName("frame_11")
	
	def set_color(self, color):
		self.color = color

	def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
		if event.button() == QtCore.Qt.LeftButton:
			self.pat += f"/{self.findChild(QtWidgets.QLabel, 'label_11').text()}"
			folders = [d for d in os.listdir(f"Messages/{self.label.text()}{self.pat}") if os.path.isdir(os.path.join(f"Messages/{self.label.text()}{self.pat}", d))]
			files = [f for f in os.listdir(f"Messages/{self.label.text()}{self.pat}") if os.path.isfile(os.path.join(f"Messages/{self.label.text()}{self.pat}", f))]
			for i in reversed(range(self.grid.count())):
				widgets = self.grid.itemAt(i).widget()
				widgets.setParent(None)
				widgets.hide()
			
			frame_11 = MyFrameBack(None, self.label, self.grid, self.color, self.pat)
			frame_11.setFixedSize(110, 110)
			frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
			frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
			label_10 = QtWidgets.QLabel(frame_11)
			label_10.setGeometry(QtCore.QRect(30, 15, 50, 50))
			label_10.setText("")
			label_10.setPixmap(QtGui.QPixmap(":/images/Images/back.png"))
			label_10.setScaledContents(True)
			label_10.setObjectName("label_10")
			label_11 = QtWidgets.QLabel(frame_11)
			label_11.setGeometry(QtCore.QRect(0, 70, 110, 40))
			label_11.setAutoFillBackground(False)
			label_11.setScaledContents(False)
			label_11.setAlignment(QtCore.Qt.AlignCenter)
			label_11.setWordWrap(True)
			label_11.setObjectName("label_11")
			label_11.setStyleSheet(f"color: {self.color}")
			label_11.setMinimumHeight(50)
			label_11.setText(f"back")
				
			frame_11.setContentsMargins(0, 0, 0, 0)
			row, col = 0, 0
			self.grid.addWidget(frame_11, row, col, alignment=QtCore.Qt.AlignTop)

			for i in range(len(folders)):
				frame_11 = MyFrame(None, self.label, self.grid, self.color, pat=self.pat)
				frame_11.setFixedSize(110, 110)
				frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
				frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
				label_10 = QtWidgets.QLabel(frame_11)
				label_10.setGeometry(QtCore.QRect(30, 15, 50, 50))
				label_10.setText("")
				label_10.setPixmap(QtGui.QPixmap(":/images/Images/folder.png"))
				label_10.setScaledContents(True)
				label_10.setObjectName("label_10")
				label_11 = QtWidgets.QLabel(frame_11)
				label_11.setGeometry(QtCore.QRect(0, 70, 110, 40))
				label_11.setAutoFillBackground(False)
				label_11.setScaledContents(False)
				label_11.setAlignment(QtCore.Qt.AlignCenter)
				label_11.setWordWrap(True)
				label_11.setObjectName("label_11")
				label_11.setStyleSheet(f"color: {self.color}")
				label_11.setMinimumHeight(50)
				label_11.setText(f"{folders[i]}")
				
				frame_11.setContentsMargins(0, 0, 0, 0)
				row, col = divmod(i+1, 3)
				self.grid.addWidget(frame_11, row, col, alignment=QtCore.Qt.AlignTop)
			
			for i in range(len(files)):
				frame_11 = MyFrameFile(None, self.label, pat=self.pat)
				frame_11.setFixedSize(110, 110)
				frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
				frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
				label_10 = QtWidgets.QLabel(frame_11)
				label_10.setGeometry(QtCore.QRect(30, 15, 50, 50))
				label_10.setText("")
				if files[i].endswith(".jpg") or files[i].endswith(".jpeg"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/jpeg.png"))
				elif files[i].endswith(".png"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/png.png"))
				elif files[i].endswith(".doc") or files[i].endswith(".docx"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/docx.png"))
				elif files[i].endswith(".pdf"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/pdf.png"))
				elif files[i].endswith(".txt") or files[i].endswith(".text"):
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/txt.png"))
				else:
					label_10.setPixmap(QtGui.QPixmap(":/images/Images/file.png"))
				label_10.setScaledContents(True)
				label_10.setObjectName("label_10")
				label_11 = QtWidgets.QLabel(frame_11)
				label_11.setGeometry(QtCore.QRect(0, 70, 110, 40))
				label_11.setAutoFillBackground(False)
				label_11.setScaledContents(False)
				label_11.setAlignment(QtCore.Qt.AlignCenter)
				label_11.setWordWrap(True)
				label_11.setObjectName("label_11")
				label_11.setStyleSheet(f"color: {self.color}")
				label_11.setMinimumHeight(50)
				label_11.setText(f"{files[i]}")
				
				frame_11.setContentsMargins(0, 0, 0, 0)
				row, col = divmod(i+len(folders)+1, 3)
				self.grid.addWidget(frame_11, row, col, alignment=QtCore.Qt.AlignTop)


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setFixedSize(921, 578)
		MainWindow.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		self.currentItem = None
		self.currentWidget = None
		self.settings = QtCore.QSettings("AuditA", "Audit")
		self.frame_theme = "#C4C4C4"
		self.label_theme = "#262626"
		self.select_theme = "#F5F5F5"
		self.profile_theme = "profile.png"
		self.folder_name_theme = "black"
		self.database = Database("database.db")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(0, 0, 921, 578))
		self.frame.setStyleSheet("QFrame{\n"
"    background-color: #F5F5F5;\n"
"}")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.frame_2 = QtWidgets.QFrame(self.frame)
		self.frame_2.setGeometry(QtCore.QRect(0, 0, 60, 578))
		self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: #EEEEEE;\n"
"}")
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.frame_3 = QtWidgets.QFrame(self.frame_2)
		self.frame_3.setGeometry(QtCore.QRect(12, 40, 38, 38))
		self.frame_3.setStyleSheet("QFrame{\n"
"    background-color: #D8D8D8;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #4B7BEC;\n"
"}")
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
		self.frame_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.frame_4.setGeometry(QtCore.QRect(12, 510, 38, 38))
		self.frame_4.setStyleSheet("")
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
		self.frame_5 = QtWidgets.QFrame(self.frame)
		self.frame_5.setGeometry(QtCore.QRect(60, 0, 231, 578))
		self.frame_5.setStyleSheet("QFrame{\n"
"    background-color: #EEEEEE;\n"
"}")
		self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_5.setObjectName("frame_5")
		self.label_3 = QtWidgets.QLabel(self.frame_5)
		self.label_3.setGeometry(QtCore.QRect(20, 20, 141, 16))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(9)
		self.label_3.setFont(font)
		self.label_3.setStyleSheet("color: #1E1E1E;")
		self.label_3.setObjectName("label_3")
		self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.setGeometry(QtCore.QRect(4, 42, 223, 21))
		self.lineEdit.setStyleSheet(u"border: none;\n"
"border-radius: 4px;\n"
"background-color: #F5F5F5;")
		self.lineEdit.clearFocus()
		self.lineEdit.textChanged.connect(self.editFilter)
		self.listView = QtWidgets.QListWidget(self.frame_5)
		self.listView.setGeometry(QtCore.QRect(0, 66, 231, 512))
		users = [d for d in os.listdir("Messages") if os.path.isdir(os.path.join("Messages", d))]
		ll = len(users)
		if ll > 9:
			self.listView.setGeometry(QtCore.QRect(0, 56, 236, 522))
		self.listView.setAutoFillBackground(False)
		self.listView.setStyleSheet("QListWidget{\n"
"    border: 0;\n"
"}\n")
		self.listView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
		self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.listView.verticalScrollBar().setStyleSheet("QScrollBar:vertical { background:#f0f0f0; width: 10px; } QScrollBar::handle:vertical{border-radius:3px; background:#8c8c8c;} QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:#f0f0f0;}")
		# self.listView.verticalScrollBar().setStyleSheet("QScrollBar::handle:vertical{border-radius:3px; background:#8c8c8c;} QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:#f0f0f0;} QScrollBar:vertical{width:14px}")
		self.listView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
		self.listView.setObjectName("listView")
		self.listView.setFocusPolicy(QtCore.Qt.NoFocus)
		self.listView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.listView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.listView.itemClicked.connect(self.selectUser)
		self.listView.setLayoutDirection(QtCore.Qt.RightToLeft)

		for i in range(ll):
			itemN = QtWidgets.QListWidgetItem()
			widget = QtWidgets.QWidget()
			widget.setFixedSize(231, 56)
			label_7 = QtWidgets.QLabel(widget)
			label_7.setGeometry(QtCore.QRect(50, 26, 181, 16))
			font = QtGui.QFont()
			font.setFamily("Inter")
			label_7.setFont(font)
			label_7.setStyleSheet("color: #262626")
			label_7.setObjectName("label_7")
			label_7.setText(f"{users[i]}")
			label_8 = QtWidgets.QLabel(widget)
			label_8.setGeometry(QtCore.QRect(50, 12, 181, 16))
			font = QtGui.QFont()
			font.setFamily("Inter Semi Bold")
			font.setPointSize(10)
			font.setBold(True)
			font.setWeight(75)
			label_8.setFont(font)
			label_8.setStyleSheet("color: #262626;")
			label_8.setObjectName("label_8")
			name = self.database.get_user_name(f"{users[i]}")
			if name == "":
				name = "Без названия"
			label_8.setText(f"{name}")
			frame_8 = QtWidgets.QFrame(widget)
			frame_8.setGeometry(QtCore.QRect(12, 12, 32, 32))
			frame_8.setStyleSheet("QFrame{\n"
	"    background-color: #C4C4C4;\n"
	"    border-radius: 10px;\n"
	"}")
			frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
			frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
			frame_8.setObjectName("frame_8")
			label_9 = QtWidgets.QLabel(frame_8)
			label_9.setGeometry(QtCore.QRect(6, 4, 20, 24))
			label_9.setText("")
			label_9.setPixmap(QtGui.QPixmap(":/images/Images/profile.png"))
			label_9.setScaledContents(True)
			label_9.setObjectName("label_9")
			itemN.setSizeHint(QtCore.QSize(229, 56))
			self.listView.addItem(itemN)
			self.listView.setItemWidget(itemN, widget)
		
		self.frame_13 = QtWidgets.QFrame(self.frame)
		self.frame_13.setGeometry(QtCore.QRect(291, 0, 630, 42))
		self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_13.setObjectName("frame_13")

		self.pushButton = QtWidgets.QPushButton(self.frame_13)
		self.pushButton.setGeometry(QtCore.QRect(490, 6, 135, 30))
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
		self.pushButton.setText("Обновить интерфейс")

		self.frame_15 = QtWidgets.QFrame(self.frame)
		self.frame_15.setGeometry(QtCore.QRect(740, 42, 180, 536))
		self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_15.setObjectName("frame_15")
		self.frame_16 = QtWidgets.QWidget(self.frame)
		self.frame_16.setGeometry(QtCore.QRect(291, 42, 450, 536))
		self.frame_16.setObjectName("frame_16")

		self.listView_2 = QtWidgets.QListWidget(self.frame_15)
		self.listView_2.setGeometry(QtCore.QRect(0, 0, 180, 536))
		self.listView_2.setAutoFillBackground(False)
		self.listView_2.setStyleSheet("QListWidget{\n"
"	 border: 0;\n"
"}\n"
"QListWidget::verticalScrollBar {\n"
"	 min-height: 50px;\n"
"}")
		self.listView_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
		self.listView_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.listView_2.verticalScrollBar().setStyleSheet("QScrollBar:vertical { background:#f0f0f0; width: 10px; } QScrollBar::handle:vertical{border-radius:3px; background:#8c8c8c;} QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:#f0f0f0;}")
		self.listView_2.verticalScrollBar().setMinimumHeight(50)
		self.listView_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
		self.listView_2.setObjectName("listView_2")
		self.listView_2.setFocusPolicy(QtCore.Qt.NoFocus)
		self.listView_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.listView_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.listView_2.setSpacing(10)
		# self.listView_2.setLayoutDirection(QtCore.Qt.RightToLeft)

		self.scrollArea = QtWidgets.QScrollArea(self.frame_16)
		self.scrollArea.setGeometry(QtCore.QRect(0, 0, 450, 536))
		self.scrollArea.setObjectName(u"scrollArea")
		self.scrollArea.setStyleSheet("background-color: #F5F5F5; border: none;")
		self.scrollAreaWidget = QtWidgets.QWidget()
		self.scrollArea.setWidget(self.scrollAreaWidget)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
		self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		# self.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar:vertical { background: transparent; width: 16px; margin: 16px 0 16px 0; } QScrollBar::handle:vertical{ background: #888; min-height: 20px; } QScrollBar::add-line:vertical { height: 16px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::sub-line:vertical{ height: 16px; subcontrol-position: top; subcontrol-origin: margin; } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; } QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { }")
		self.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar::handle:vertical{border-radius:3px; background:#8c8c8c;} QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:#f0f0f0;} QScrollBar:vertical{width:10px}")
		self.grid = QtWidgets.QGridLayout(self.scrollAreaWidget)

		self.grid.setContentsMargins(30, 0, 0, 0)
		self.grid.setAlignment(QtCore.Qt.AlignTop)
		self.grid.setHorizontalSpacing(30)
		self.grid.setVerticalSpacing(30)
		self.scrollAreaWidget.setGeometry(0, 0, 450, 536)

		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label_3.setText(_translate("MainWindow", "ВХОДЯЩИЕ ПИСЬМА"))
	
	def selectUser(self, item):
		widget = self.listView.itemWidget(item)
		widget.setStyleSheet(f"background-color: {self.select_theme};")

		if self.currentItem is not None and item != self.currentItem:
			try:
				self.currentWidget.setStyleSheet("")
			except:
				pass
		
		self.currentItem = item
		self.currentWidget = widget

		for i in self.frame_13.children():
			if i is not self.pushButton:
				i.setParent(None)
				i.hide()

		self.listView_2.clear()

		self.frame_14 = QtWidgets.QFrame(self.frame_13)
		self.frame_14.setGeometry(QtCore.QRect(10, 10, 24, 24))
		self.frame_14.setStyleSheet("QFrame{\n"
f"    background-color: {self.frame_theme};\n"
"    border-radius: 12px;\n"
"}")
		self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_14.setObjectName("frame_14")
		self.label_16 = QtWidgets.QLabel(self.frame_14)
		self.label_16.setGeometry(QtCore.QRect(7, 6, 10, 12))
		self.label_16.setText("")
		self.label_16.setPixmap(QtGui.QPixmap(f":/images/Images/{self.profile_theme}"))
		self.label_16.setScaledContents(True)
		self.label_16.setObjectName("label_16")
		self.label_17 = QtWidgets.QLabel(self.frame_13)
		self.label_17.setGeometry(QtCore.QRect(40, 10, 250, 16))
		font = QtGui.QFont()
		font.setFamily("Inter Semi Bold")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_17.setFont(font)
		self.label_17.setStyleSheet(f"color: {self.label_theme};")
		self.label_17.setObjectName("label_17")
		name = self.database.get_user_name(widget.findChild(QtWidgets.QLabel, 'label_7').text())
		if name == "":
			name = "Без названия"
		self.label_17.setText(f"{name}")
		self.label_18 = QtWidgets.QLabel(self.frame_13)
		self.label_18.setGeometry(QtCore.QRect(40, 20, 181, 16))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(7)
		self.label_18.setFont(font)
		self.label_18.setStyleSheet(f"color: {self.label_theme};\n"
"background-color: none;")
		self.label_18.setObjectName("label_18")
		self.label_18.setText(f"{widget.findChild(QtWidgets.QLabel, 'label_7').text()}")

		""" self.pushButton = QtWidgets.QPushButton(self.frame_13)
		self.pushButton.setGeometry(QtCore.QRect(490, 6, 135, 30))
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
		if self.folder_name_theme == "black":
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
		else:
			self.pushButton.setStyleSheet("QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; color: #3B3B3B; margin: 0; min-width: 0; outline: none; text-align: center; text-decoration: none; color: #fff; } QPushButton:hover { color: black; background-color: white; }")
		self.pushButton.setAutoDefault(False)
		self.pushButton.setDefault(False)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText("Обновить интерфейс") """

		self.frame_14.show()
		# self.pushButton.show()
		self.label_17.show()
		self.label_18.show()
		self.frame_13.update()

		for i in reversed(range(self.grid.count())):
			widgets = self.grid.itemAt(i).widget()
			widgets.setParent(None)
			widgets.hide()

		users = [d for d in os.listdir(f"Messages/{widget.findChild(QtWidgets.QLabel, 'label_7').text()}") if os.path.isdir(os.path.join(f"Messages/{widget.findChild(QtWidgets.QLabel, 'label_7').text()}", d))]

		for i in range(len(users)):
			frame_11 = MyFrame(None, self.label_18, self.grid, self.folder_name_theme)
			frame_11.setFixedSize(110, 110)
			frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
			frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
			label_10 = QtWidgets.QLabel(frame_11)
			label_10.setGeometry(QtCore.QRect(30, 15, 50, 50))
			label_10.setText("")
			label_10.setPixmap(QtGui.QPixmap(":/images/Images/folder.png"))
			label_10.setScaledContents(True)
			label_10.setObjectName("label_10")
			label_11 = QtWidgets.QLabel(frame_11)
			label_11.setGeometry(QtCore.QRect(0, 65, 110, 45))
			label_11.setAutoFillBackground(False)
			label_11.setScaledContents(False)
			label_11.setAlignment(QtCore.Qt.AlignCenter)
			label_11.setWordWrap(True)
			label_11.setStyleSheet(f"color: {self.folder_name_theme};")
			label_11.setMinimumHeight(50)
			label_11.setObjectName("label_11")
			label_11.setText(f"{users[i]}")
			
			frame_11.setContentsMargins(0, 0, 0, 0)
			row, col = divmod(i, 3)
			self.grid.addWidget(frame_11, row, col, alignment=QtCore.Qt.AlignTop)

		texts = [f for f in os.listdir(f"Messages/{widget.findChild(QtWidgets.QLabel, 'label_7').text()}/texts") if os.path.isfile(os.path.join(f"Messages/{widget.findChild(QtWidgets.QLabel, 'label_7').text()}/texts", f))]

		for i in range(len(texts)):
			itemN = QtWidgets.QListWidgetItem()
			widget1 = QtWidgets.QWidget()
			label_12 = QtWidgets.QLabel(widget1)
			font = QtGui.QFont()
			font.setFamily("Inter Semi Bold")
			font.setPointSize(9)
			font.setBold(True)
			font.setWeight(75)
			label_12.setFont(font)
			label_12.setFixedWidth(170)
			label_12.setStyleSheet("color: #262626;")
			label_12.setObjectName("label_12")
			label_12.setWordWrap(True)
			with open(f"Messages/{widget.findChild(QtWidgets.QLabel, 'label_7').text()}/texts/{texts[i]}", "r", encoding='utf-8') as text:
				content = text.read()
				if content.strip():
					label_12.setText(f"{content}")
					label_12.setStyleSheet(f"color: {self.folder_name_theme};")
					label_12.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
					label_12.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
					widget1.setFixedSize(170, label_12.sizeHint().height())
					itemN.setSizeHint(QtCore.QSize(170, widget1.height()))
					self.listView_2.addItem(itemN)
					self.listView_2.setItemWidget(itemN, widget1)
		
	def editFilter(self):
		filterText = self.lineEdit.text()
		for i in range(self.listView.count()):
			item = self.listView.item(i)
			frame_widget = self.listView.itemWidget(item)
			label_widget = frame_widget.findChild(QtWidgets.QLabel, 'label_8').text()

			if filterText.lower() in label_widget.lower():
				item.setHidden(False)
			else:
				item.setHidden(True)

import resources_rc
