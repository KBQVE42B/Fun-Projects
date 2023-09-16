# This is a program for making funny moments
# It's an OOP(object oriented programming) project

import os
import random

from PyQt5 import QtCore, QtGui, QtWidgets

from playsound import playsound
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class Ui_gay(QtWidgets.QWidget):
	# The auto screen sizing for qt with os library
	os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

	# The setup ui code block(I create this block with Qt designer)
	def setupUi(self, gay):
		gay.setObjectName("gay")
		gay.resize(500, 300)
		gay.setMinimumSize(QtCore.QSize(500, 300))
		gay.setMaximumSize(QtCore.QSize(500, 300))
		gay.setStyleSheet("background-color: #393E46;\n"
	"color: rgb(233, 102, 160);")
		self.centralwidget = QtWidgets.QWidget(gay)
		self.centralwidget.setObjectName("centralwidget")
		self.title = QtWidgets.QFrame(self.centralwidget)
		self.title.setGeometry(QtCore.QRect(-1, -10, 501, 71))
		self.title.setStyleSheet("background-color: #2B2730;\n"
	"border-radius: 7px;\n"
	"border-bottom: 1px solid #9575DE;")
		self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.title.setFrameShadow(QtWidgets.QFrame.Raised)
		self.title.setObjectName("title")
		self.question = QtWidgets.QLabel(self.title)
		self.question.setGeometry(QtCore.QRect(133, 20, 271, 41))
		self.question.setStyleSheet("padding-left: 25%;\n"
	"padding-right: 25%;\n"
	"border:None;\n"
	"font: 14pt \"Ravie\";\n"
	"")
		self.question.setObjectName("question")
		self.yes = QtWidgets.QPushButton(self.centralwidget)
		self.yes.setGeometry(QtCore.QRect(170, 160, 56, 17))
		self.yes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.yes.setStyleSheet("background-color: rgb(101, 84, 175);\n"
	"border-radius: 5px;\n"
	"border: 1px dashed #2B2730;\n"
	"font: 700 italic 9pt \"Calibri\";")
		self.yes.setObjectName("yes")
		self.no = QtWidgets.QPushButton(self.centralwidget)
		self.no.setGeometry(QtCore.QRect(260, 160, 56, 17))
		self.no.setStyleSheet("background-color: rgb(101, 84, 175);\n"
	"border-radius: 5px;\n"
	"border: 1px dashed #2B2730;\n"
	"font: 700 italic 9pt \"Calibri\";")
		self.no.setObjectName("no")

		# adding the hover event to our 'no' button
		self.no.installEventFilter(self)

		gay.setCentralWidget(self.centralwidget)

		self.retranslateUi(gay)
		self.yes.clicked.connect(self.sound_play) # if this button clicked then call sound_play function
		QtCore.QMetaObject.connectSlotsByName(gay)


	# This function : If button hovered call change position function
	def eventFilter(self, obj, event):
		if obj == self.no and event.type() == QtCore.QEvent.HoverEnter:
			self.change_pos()

		return super(Ui_gay, self).eventFilter(obj, event)


	# The main part is here
	# Changing the 'no' button geometry and position
	def change_pos(self):		
		while True:
			# getting random positions
			distancex = random.randrange(0, 444, 20)
			distancey = random.randrange(71, 283, 20)
			
			# if my button not stay at its position do break
			if abs(distancex - self.no.geometry().x()) >= 20:
				break
		
		# set the 'no' button geometry
		self.no.setGeometry(QtCore.QRect(distancex, distancey, 56, 17))


	def sound_play(self):
		# getting the current speakers
		speakers = AudioUtilities.GetSpeakers()
		interface = speakers.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
		
		# getting the volume and change it to maximum volume
		volume = cast(interface, POINTER(IAudioEndpointVolume))
		volume.SetMasterVolumeLevel(0, None)

		# playing gay sound effect
		playsound('sound.mp3')


	def retranslateUi(self, gay):
		_translate = QtCore.QCoreApplication.translate
		gay.setWindowTitle(_translate("gay", "Gay or No"))
		self.question.setText(_translate("gay", "Are You Gay ?"))
		self.yes.setText(_translate("gay", "Yes"))
		self.no.setText(_translate("gay", "No"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	gay = QtWidgets.QMainWindow()
	ui = Ui_gay()
	ui.setupUi(gay)
	gay.show()
	sys.exit(app.exec_())