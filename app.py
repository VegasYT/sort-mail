import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QCursor
from parse import Parse
import resources_rc
import auth
import main
import settings
import os


class Parsing(QThread):
	operationCompleted = pyqtSignal()
	errorOccurred = pyqtSignal(str)

	def __init__(self, email, password):
		super().__init__()
		self.email = email
		self.password = password

	def run(self):
		try:
			Parse(self.email, self.password).parse_messages("UNSEEN")
			self.operationCompleted.emit()
		except Exception as e:
			self.errorOccurred.emit(str(e))


class AuthWindow(QtWidgets.QMainWindow, auth.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)


class SettingsWindow(QtWidgets.QMainWindow, settings.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)


class StackedWidget(QtWidgets.QStackedWidget):
	def __init__(self, settings, parent=None):
		super().__init__(parent)

		self.settings = settings

		self.auth_win = AuthWindow()
		self.main_win = MainWindow()
		self.settings_win = SettingsWindow()

		self.addWidget(self.auth_win)
		self.addWidget(self.main_win)
		self.addWidget(self.settings_win)

		self.currentChanged.connect(self.on_current_changed)
		self.auth_win.pushButton.clicked.connect(self.change_to_main)
		self.main_win.frame_4.mousePressEvent = lambda event: self.setCurrentIndex(2)
		self.settings_win.frame_3.mousePressEvent = lambda event: self.setCurrentIndex(1)
		self.settings_win.frame_5.mousePressEvent = self.change_light_theme
		self.settings_win.frame_7.mousePressEvent = self.change_dark_theme
		self.settings_win.pushButton_1.clicked.connect(self.upload_messages)
		self.main_win.pushButton.clicked.connect(self.upload_interface)

		if self.settings.value("theme", "light") == "light":
			self.settings_win.frame_5.setStyleSheet("QFrame{ border: 2px solid #4B7BEC; border-radius: 15px; }")
		else:
			QtCore.QCoreApplication.processEvents()
			self.change_dark_theme_settings()
			self.change_dark_theme_main()
			self.settings_win.frame_7.setStyleSheet("QFrame{ border: 2px solid #4B7BEC; border-radius: 15px; }")

	def on_current_changed(self, index):
		widget = self.widget(index)
		self.setFixedSize(widget.width(), widget.height())
	
	def change_to_main(self):
		self.email = self.auth_win.lineEdit.text()
		self.password = self.auth_win.lineEdit_2.text()
		if self.email != "" and self.password != "":
			self.longOperationThread = Parsing(self.email, self.password)
			self.longOperationThread.operationCompleted.connect(self.parsing_good)
			self.longOperationThread.errorOccurred.connect(self.parsing_error)
			self.longOperationThread.start()
			self.auth_win.pushButton.setEnabled(False)
			self.show_notification_loading()
	
	def parsing_error(self):
		self.hide_notification_loading()
		self.show_notification_error()
	
	def parsing_good(self):
		self.settings.setValue("login", self.email)
		self.settings.setValue("password", self.password)
		self.setCurrentIndex(1)
		
	def show_notification_error(self):
		self.animation1 = QtCore.QPropertyAnimation(self.auth_win.frame_4, b"geometry")
		self.animation1.setDuration(300)
		self.animation1.setStartValue(self.auth_win.frame_4.geometry())
		self.animation1.setEndValue(QtCore.QRect(634, 328, 201, 30))
		self.animation1.finished.connect(lambda: (self.auth_win.pushButton.setEnabled(True), QtCore.QTimer.singleShot(2000, self.hide_notification_error)))
		self.animation1.start()
	
	def hide_notification_error(self):
		self.animation1 = QtCore.QPropertyAnimation(self.auth_win.frame_4, b"geometry")
		self.animation1.setDuration(300)
		self.animation1.setStartValue(self.auth_win.frame_4.geometry())
		self.animation1.setEndValue(QtCore.QRect(634, 358, 201, 30))
		self.animation1.start()
	
	def show_notification_loading(self):
		self.animation2 = QtCore.QPropertyAnimation(self.auth_win.frame_6, b"geometry")
		self.animation2.setDuration(300)
		self.animation2.setStartValue(self.auth_win.frame_6.geometry())
		self.animation2.setEndValue(QtCore.QRect(634, 328, 201, 30))
		self.animation2.start()
	
	def hide_notification_loading(self):
		self.animation2 = QtCore.QPropertyAnimation(self.auth_win.frame_6, b"geometry")
		self.animation2.setDuration(300)
		self.animation2.setStartValue(self.auth_win.frame_6.geometry())
		self.animation2.setEndValue(QtCore.QRect(634, 358, 201, 30))
		self.animation2.start()
	
	def change_light_theme(self, event):
		self.change_light_theme_settings()
		self.change_light_theme_main()
		self.settings.setValue("theme", "light")
	
	def change_dark_theme(self, event):
		self.change_dark_theme_settings()
		self.change_dark_theme_main()
		self.settings.setValue("theme", "dark")
	
	def change_dark_theme_settings(self):
		self.settings_win.frame_5.setStyleSheet("")
		self.settings_win.frame_7.setStyleSheet("QFrame{ border: 2px solid #4B7BEC; border-radius: 15px; }")
		self.settings_win.frame.setStyleSheet("QFrame{ background-color: #3d3d3c; }")
		self.settings_win.frame_6.setStyleSheet("QFrame{ background-color: #F5F5F5; border: 2px solid white; border-radius: 10px; }")
		self.settings_win.label_4.setStyleSheet("color: white; border: none;")
		self.settings_win.label_5.setStyleSheet("border: none; color: white;")
		self.settings_win.frame_8.setStyleSheet("QFrame{ border: 2px solid white; border-radius: 10px; background-color: #1b1c1f; }")
		self.settings_win.label_3.setStyleSheet("color: white;")
		self.settings_win.pushButton.setStyleSheet("QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; color: #3B3B3B; margin: 0; min-width: 0; outline: none; text-align: center; text-decoration: none; color: #fff; } QPushButton:hover { color: black; background-color: white; }")
		self.settings_win.pushButton_1.setStyleSheet("QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; color: #3B3B3B; margin: 0; min-width: 0; outline: none; text-align: center; text-decoration: none; color: #fff; } QPushButton:hover { color: black; background-color: white; }")
		self.settings_win.frame_2.setStyleSheet("QFrame{ background-color: #292928; }")
		self.settings_win.frame_4.setStyleSheet("QFrame{ background-color:  #3d3d3c; border-radius: 10px; border: 2px solid #4B7BEC; }")
		self.settings_win.label.setPixmap(QPixmap(":/images/Images/chat_dark.png"))
		self.settings_win.label_2.setPixmap(QPixmap(":/images/Images/settings_dark.png"))

	def change_light_theme_settings(self):
		self.settings_win.frame_5.setStyleSheet("QFrame{ border: 2px solid #4B7BEC; border-radius: 15px; }")
		self.settings_win.frame_7.setStyleSheet("")
		self.settings_win.frame.setStyleSheet("QFrame{ background-color: #F5F5F5; }")
		self.settings_win.frame_2.setStyleSheet("QFrame{ background-color: #EEEEEE; }")
		self.settings_win.frame_4.setStyleSheet("QFrame{ background-color: #D8D8D8; border-radius: 10px; border: 2px solid #4B7BEC; }")
		self.settings_win.label_3.setStyleSheet("color: black;")
		self.settings_win.pushButton.setStyleSheet("QPushButton { background-color: transparent; border: 2px solid #1A1A1A; border-radius: 10px; color: #3B3B3B; margin: 0; min-width: 0; outline: none; text-align: center; text-decoration: none; } QPushButton:hover { color: #fff; background-color: #1A1A1A; }")
		self.settings_win.pushButton_1.setStyleSheet("QPushButton { background-color: transparent; border: 2px solid #1A1A1A; border-radius: 10px; color: #3B3B3B; margin: 0; min-width: 0; outline: none; text-align: center; text-decoration: none; } QPushButton:hover { color: #fff; background-color: #1A1A1A; }")
		self.settings_win.frame_6.setStyleSheet("QFrame{ border: 2px solid black; border-radius: 10px; }")
		self.settings_win.label_4.setStyleSheet("color: black; border: none;")
		self.settings_win.label_5.setStyleSheet("border: none; color: black;")
		self.settings_win.frame_8.setStyleSheet("QFrame{ border: 2px solid black; border-radius: 10px; background-color: #1b1c1f; }")
		self.settings_win.label.setPixmap(QPixmap(":/images/Images/chat.png"))
		self.settings_win.label_2.setPixmap(QPixmap(":/images/Images/settings.png"))

	def change_dark_theme_main(self):
		self.main_win.frame.setStyleSheet("QFrame{ background-color: #3d3d3c; }")
		self.main_win.frame_2.setStyleSheet("QFrame{ background-color: #292928; }")
		self.main_win.frame_3.setStyleSheet("QFrame{ background-color:  #3d3d3c; border-radius: 10px; border: 2px solid #4B7BEC; }")
		self.main_win.frame_16.setStyleSheet("QFrame{ background: none; }")
		self.main_win.label.setPixmap(QPixmap(":/images/Images/chat_dark.png"))
		self.main_win.label_2.setPixmap(QPixmap(":/images/Images/settings_dark.png"))
		self.main_win.frame_5.setStyleSheet("QFrame{ background-color: #292928; }")
		self.main_win.label_3.setStyleSheet("color: #e0e0e0;")
		self.main_win.lineEdit.setStyleSheet("border: none; border-radius: 4px; background-color: #3d3d3c; color: white;")
		self.main_win.listView.verticalScrollBar().setStyleSheet("QScrollBar:vertical { background: #121212; width: 10px; } QScrollBar::handle:vertical { border-radius: 3px; background: #8c8c8c; } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{ background: #4f4f4f; }")
		for i in range(self.main_win.listView.count()):
			item = self.main_win.listView.item(i)
			frame_widget = self.main_win.listView.itemWidget(item)
			frame_widget.findChild(QtWidgets.QLabel, "label_7").setStyleSheet("color: #e8e8e8")
			frame_widget.findChild(QtWidgets.QLabel, "label_8").setStyleSheet("color: #e8e8e8")
			frame_widget.findChild(QtWidgets.QFrame, "frame_8").setStyleSheet("QFrame { background-color: #424242; border-radius: 10px }")
			frame_widget.findChild(QtWidgets.QLabel, "label_9").setPixmap(QPixmap(":/images/Images/profile_dark.png"))
		self.main_win.listView_2.verticalScrollBar().setStyleSheet("QScrollBar:vertical { background: #121212; width: 10px; } QScrollBar::handle:vertical { border-radius: 3px; background: #8c8c8c; } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{ background: #4f4f4f; }")
		self.main_win.scrollArea.setStyleSheet("background-color: #3d3d3c; border: none;")
		self.main_win.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar::handle:vertical{border-radius:3px; background:#8c8c8c;} QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:#4f4f4f;} QScrollBar:vertical{width:10px}")
		self.main_win.frame_theme = "#333333"
		self.main_win.label_theme = "#e8e8e8"
		self.main_win.profile_theme = "profile_dark.png"
		self.main_win.pushButton.setStyleSheet("QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; color: #3B3B3B; margin: 0; min-width: 0; outline: none; text-align: center; text-decoration: none; color: #fff; } QPushButton:hover { color: black; background-color: white; }")
		try:
			self.main_win.frame_14.setStyleSheet("QFrame { background-color: #333333; border-radius: 12px; }")
			self.main_win.label_16.setPixmap(QPixmap(":/images/Images/profile_dark.png"))
			self.main_win.label_17.setStyleSheet("color: #e8e8e8")
			self.main_win.label_18.setStyleSheet("color: #e8e8e8; background-color: none;")
		except:
			pass
		for i in range(self.main_win.grid.count()):
			child_widget = self.main_win.grid.itemAt(i).widget()
			if isinstance(child_widget, main.MyFrame) or isinstance(child_widget, main.MyFrameBack):
				child_widget.set_color("white")
			child_widget.findChild(QtWidgets.QLabel, "label_11").setStyleSheet("color: white;")
		self.main_win.folder_name_theme = "white"
		for i in range(self.main_win.listView_2.count()):
			item = self.main_win.listView_2.item(i)
			frame_widget = self.main_win.listView_2.itemWidget(item)
			frame_widget.findChild(QtWidgets.QLabel, "label_12").setStyleSheet("color: white;")
		self.main_win.select_theme = "#3d3d3c"
		try:
			self.main_win.currentWidget.setStyleSheet("background-color: #3d3d3c;")
		except:
			pass

	def change_light_theme_main(self):
		self.main_win.frame.setStyleSheet("QFrame{ background-color: #F5F5F5; }")
		self.main_win.frame_2.setStyleSheet("QFrame{ background-color: #EEEEEE; }")
		self.main_win.frame_3.setStyleSheet("QFrame{ background-color:  #D8D8D8; border-radius: 10px; border: 2px solid #4B7BEC; }")
		self.main_win.label.setPixmap(QPixmap(":/images/Images/chat.png"))
		self.main_win.label_2.setPixmap(QPixmap(":/images/Images/settings.png"))
		self.main_win.frame_5.setStyleSheet("QFrame{ background-color: #EEEEEE; }")
		self.main_win.label_3.setStyleSheet("color: #1E1E1E;")
		self.main_win.lineEdit.setStyleSheet("border: none; border-radius: 4px; background-color: #F5F5F5;")
		self.main_win.listView.verticalScrollBar().setStyleSheet("QScrollBar:vertical { background:#f0f0f0; width: 10px; } QScrollBar::handle:vertical{border-radius:3px; background:#8c8c8c;} QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:#f0f0f0;}")
		for i in range(self.main_win.listView.count()):
			item = self.main_win.listView.item(i)
			frame_widget = self.main_win.listView.itemWidget(item)
			frame_widget.findChild(QtWidgets.QLabel, "label_7").setStyleSheet("color: #262626")
			frame_widget.findChild(QtWidgets.QLabel, "label_8").setStyleSheet("color: #262626;")
			frame_widget.findChild(QtWidgets.QFrame, "frame_8").setStyleSheet("QFrame { background-color: #C4C4C4; border-radius: 10px }")
			frame_widget.findChild(QtWidgets.QLabel, "label_9").setPixmap(QPixmap(":/images/Images/profile.png"))
		self.main_win.listView_2.verticalScrollBar().setStyleSheet("QScrollBar:vertical { background:#f0f0f0; width: 10px; } QScrollBar::handle:vertical{border-radius:3px; background:#8c8c8c;} QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:#f0f0f0;}")
		self.main_win.scrollArea.setStyleSheet("background-color: #F5F5F5; border: none;")
		self.main_win.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar::handle:vertical{border-radius:3px; background:#8c8c8c;} QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:#f0f0f0;} QScrollBar:vertical{width:10px}")
		self.main_win.frame_theme = "#C4C4C4"
		self.main_win.label_theme = "#262626"
		self.main_win.profile_theme = "profile.png"
		self.main_win.pushButton.setStyleSheet("QPushButton { background-color: transparent; border: 2px solid #1A1A1A; border-radius: 10px; color: #3B3B3B; margin: 0; min-width: 0; outline: none; text-align: center; text-decoration: none; } QPushButton:hover { color: #fff; background-color: #1A1A1A; }")
		try:
			self.main_win.frame_14.setStyleSheet("QFrame { background-color: #C4C4C4; border-radius: 12px; }")
			self.main_win.label_16.setPixmap(QPixmap(":/images/Images/profile.png"))
			self.main_win.label_17.setStyleSheet("color: #262626")
			self.main_win.label_18.setStyleSheet("color: #262626; background-color: none;")
		except:
			pass
		for i in range(self.main_win.grid.count()):
			child_widget = self.main_win.grid.itemAt(i).widget()
			if isinstance(child_widget, main.MyFrame) or isinstance(child_widget, main.MyFrameBack):
				child_widget.set_color("black")
			child_widget.findChild(QtWidgets.QLabel, "label_11").setStyleSheet("color: black;")
		self.main_win.folder_name_theme = "black"
		for i in range(self.main_win.listView_2.count()):
			item = self.main_win.listView_2.item(i)
			frame_widget = self.main_win.listView_2.itemWidget(item)
			frame_widget.findChild(QtWidgets.QLabel, "label_12").setStyleSheet("color: black;")
		self.main_win.select_theme = "#F5F5F5"
		try:
			self.main_win.currentWidget.setStyleSheet("background-color: #F5F5F5;")
		except:
			pass

	def upload_messages(self):
		self.longOperation = Parsing(self.settings.value("login"), self.settings.value("password"))
		self.longOperation.operationCompleted.connect(self.upload_interface)
		self.longOperation.start()
	
	def upload_interface(self):
		self.main_win.listView.clear()
		self.main_win.listView_2.clear()
		for i in reversed(range(self.main_win.grid.count())):
				widgets = self.main_win.grid.itemAt(i).widget()
				widgets.setParent(None)
				widgets.hide()
		for i in self.main_win.frame_13.children():
			if i is not self.main_win.pushButton:
				i.setParent(None)
				i.hide()

		""" self.main_win.pushButton = QtWidgets.QPushButton(self.main_win.frame_13)
		self.main_win.pushButton.setGeometry(QtCore.QRect(490, 6, 135, 30))
		font = QFont()
		font.setFamily("Inter")
		font.setPointSize(9)
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(50)
		font.setStrikeOut(False)
		self.main_win.pushButton.setFont(font)
		self.main_win.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
		self.main_win.pushButton.setStyleSheet("QPushButton {\n"
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
		self.main_win.pushButton.setAutoDefault(False)
		self.main_win.pushButton.setDefault(False)
		self.main_win.pushButton.setObjectName("pushButton")
		self.main_win.pushButton.setText("Обновить интерфейс")
		self.main_win.pushButton.clicked.connect(self.upload_interface)
		self.main_win.pushButton.show() """

		self.main_win.listView.setGeometry(QtCore.QRect(0, 66, 231, 512))
		users = [d for d in os.listdir("Messages") if os.path.isdir(os.path.join("Messages", d))]
		ll = len(users)
		if ll > 9:
			self.main_win.listView.setGeometry(QtCore.QRect(0, 56, 236, 522))
		for i in range(ll):
			itemN = QtWidgets.QListWidgetItem()
			widget = QtWidgets.QWidget()
			widget.setFixedSize(231, 56)
			label_7 = QtWidgets.QLabel(widget)
			label_7.setGeometry(QtCore.QRect(50, 26, 181, 16))
			font = QFont()
			font.setFamily("Inter")
			label_7.setFont(font)
			label_7.setStyleSheet("color: #262626")
			label_7.setObjectName("label_7")
			label_7.setText(f"{users[i]}")
			label_8 = QtWidgets.QLabel(widget)
			label_8.setGeometry(QtCore.QRect(50, 12, 181, 16))
			font = QFont()
			font.setFamily("Inter Semi Bold")
			font.setPointSize(10)
			font.setBold(True)
			font.setWeight(75)
			label_8.setFont(font)
			label_8.setStyleSheet("color: #262626;")
			label_8.setObjectName("label_8")
			name = self.main_win.database.get_user_name(f"{users[i]}")
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
			label_9.setPixmap(QPixmap(":/images/Images/profile.png"))
			label_9.setScaledContents(True)
			label_9.setObjectName("label_9")
			itemN.setSizeHint(QtCore.QSize(229, 56))
			self.main_win.listView.addItem(itemN)
			self.main_win.listView.setItemWidget(itemN, widget)
		
		if	self.settings.value("theme", "light") == "dark":
			self.change_dark_theme_main()


def check_folders():
	if not os.path.exists("Messages"):
		os.makedirs("Messages")
	
	if not os.path.exists("Templates"):
		os.makedirs("Templates")

def app():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyleSheet('QStackedWidget { border: 1px solid black; }')

	check_folders()

	# app.setQuitOnLastWindowClosed(False)
	settings = QSettings("AuditVella", "Audit")

	settings.remove("login")
	settings.remove("password")

	stacked = StackedWidget(settings)

	if settings.value("login") == None or settings.value("password") == None:
		stacked.setCurrentIndex(0)
		stacked.setFixedSize(AuthWindow().width(), AuthWindow().height())
	else:
		stacked.setCurrentIndex(1)
		stacked.setFixedSize(MainWindow().width(), MainWindow().height())

	icon = QIcon(":/images/Images/logo.png")
	stacked.setWindowIcon(icon)
	stacked.setWindowTitle("Audit")

	stacked.move(100, 100)
	stacked.show()
	
	app.exec_()

if __name__ == '__main__':
	app()