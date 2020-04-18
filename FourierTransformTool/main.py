from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtGui import QIcon, QPalette, QColor , QPixmap , QImage
from PyQt5 import  QtGui
from PyQt5.QtCore import Qt, QSize
import pyqtgraph as pg
import MRI as ui
import sys
import os
import pandas as pd
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QMessageBox)
import numpy as np
from scipy import fftpack
from pyqtgraph import PlotWidget
from matplotlib import pyplot as plt
import cv2 as cv
import MRI as ui

class ApplicationWindow(ui.Ui_MainWindow):
	def __init__(self, mainApp):
		super(ApplicationWindow, self).setupUi(mainApp) 

		self.actionLoad.triggered.connect(self.load_image)
		self.comboBox.currentIndexChanged.connect(self.select_parameter)
		self.widgets=[self.widget,self.widget_2]
		for x in range(len (self.widgets)):
				self.widgets[x].ui.histogram.hide()
				self.widgets[x].ui.roiBtn.hide()
				self.widgets[x].ui.menuBtn.hide()
				self.widgets[x].ui.roiPlot.hide()
		self.loadCheck=0

	def load_image(self):
		self.load_img =QtWidgets.QFileDialog.getOpenFileName(None, "Open File")
		self.image=cv.cvtColor(cv.imread(self.load_img[0]), cv.COLOR_BGR2GRAY)


		if self.load_img[0]:
			if self.loadCheck == 0:
				self.widget.show()
				self.widget.setImage(((self.image)).T)
				self.comboBox.setEnabled(True)
				self.loadCheck=0
				self.dft = np.fft.fft2(self.image)
				self.real = np.real(self.dft)
				self.imaginary =1j*np.imag(self.dft)
				self.magnitude = np.abs(self.dft)
				self.phase = np.angle(self.dft)
				


	def select_parameter(self,currentIndex):
		self.dft = np.fft.fft2(self.image)
		self.real =np.real(self.dft)
		self.imaginary =1j*np.imag(self.dft)
		self.magnitude = np.abs(self.dft)
		self.phase = np.angle(self.dft)
		
		self.image_Data=[(20*np.log(np.fft.fftshift(self.magnitude))),((self.phase)),(20*np.log(self.real)),np.abs((self.imaginary))]
		self.widget_2.show()
		self.widget_2.setImage((self.image_Data[self.comboBox.currentIndex()]).T)


def main():
	app = QtWidgets.QApplication(sys.argv)
	application = QtWidgets.QMainWindow()
	Window = ApplicationWindow(application)
	
	app.setStyle("Fusion")

	# Fusion dark palette from https://gist.github.com/QuantumCD/6245215.
	palette = QPalette()
	palette.setColor(QPalette.Window, QColor(53, 53, 53))
	palette.setColor(QPalette.WindowText, Qt.white)
	palette.setColor(QPalette.Base, QColor(25, 25, 25))
	palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
	palette.setColor(QPalette.ToolTipBase, Qt.white)
	palette.setColor(QPalette.ToolTipText, Qt.white)
	palette.setColor(QPalette.Text, Qt.white)
	palette.setColor(QPalette.Button, QColor(53, 53, 53))
	palette.setColor(QPalette.ButtonText, Qt.white)
	palette.setColor(QPalette.BrightText, Qt.red)
	palette.setColor(QPalette.Link, QColor(42, 130, 218))
	palette.setColor(QPalette.Highlight, QColor(42, 0, 218))
	palette.setColor(QPalette.HighlightedText, Qt.black)
	app.setPalette(palette)
	app.setStyleSheet(
		"QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

	application.show()
	sys.exit(app.exec_())
	

if __name__ == "__main__":
	main()
