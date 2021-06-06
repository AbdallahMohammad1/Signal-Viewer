# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sv.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtGui import QFileDialog
from PyQt5.QtWidgets import QFileDialog
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import pandas as pd
from matplotlib.animation import FuncAnimation
import time
import numpy as np
from matplotlib.figure import Figure
import csv




class Ui_SignalViewer(object):
    def setupUi(self, SignalViewer):
        SignalViewer.setObjectName("SignalViewer")
        SignalViewer.resize(1100, 888)
        SignalViewer.setStyleSheet("background-color: rgb(230, 230, 230);")
        ################################################
        self.figureecg = Figure()
        self.canvasecg = FigureCanvas(self.figureecg)
        ################################################
        self.figureemg = Figure()
        self.canvasemg = FigureCanvas(self.figureemg)
        ################################################
        self.figureeeg = Figure()
        self.canvaseeg = FigureCanvas(self.figureeeg)
        ################################################
        self.centralwidget = QtWidgets.QWidget(SignalViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 1101, 261))
        self.verticalWidget.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"color: rgb(218, 218, 0);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(self.verticalWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.line = QtWidgets.QFrame(self.verticalWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_2.setGeometry(QtCore.QRect(0, 260, 1101, 261))
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(1101, 231))
        self.verticalWidget_2.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"color: rgb(233, 235, 61);\n"
"gridline-color: rgb(131, 131, 131);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_3.setGeometry(QtCore.QRect(0, 520, 1101, 271))
        self.verticalWidget_3.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        ##################################################################
        self.verticalLayout.addWidget(self.canvasecg)
        self.verticalLayout_2.addWidget(self.canvasemg)
        self.verticalLayout_3.addWidget(self.canvaseeg)
        ##################################################################
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 790, 1075, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Playback = QtWidgets.QPushButton(self.groupBox)
        self.Playback.setGeometry(QtCore.QRect(60, 10, 51, 28))
        self.Playback.setObjectName("Playback")
        self.shift_left = QtWidgets.QPushButton(self.groupBox)
        self.shift_left.setGeometry(QtCore.QRect(110, 10, 51, 28))
        self.shift_left.setStyleSheet("font: 75 12pt \"MS Sans Serif\";")
        self.shift_left.setObjectName("shift_left")
        self.shift_right = QtWidgets.QPushButton(self.groupBox)
        self.shift_right.setGeometry(QtCore.QRect(160, 10, 51, 28))
        self.shift_right.setStyleSheet("font: 75 12pt \"MS Sans Serif\";")
        self.shift_right.setObjectName("shift_right")
        self.zin = QtWidgets.QPushButton(self.groupBox)
        self.zin.setGeometry(QtCore.QRect(260, 10, 51, 28))
        self.zin.setStyleSheet("font: 75 12pt \"MS Sans Serif\";")
        self.zin.setObjectName("zin")
        self.zout = QtWidgets.QPushButton(self.groupBox)
        self.zout.setGeometry(QtCore.QRect(210, 10, 51, 28))
        self.zout.setObjectName("zout")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(860, 10, 92, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_choose = QtWidgets.QLabel(self.groupBox)
        self.label_choose.setGeometry(QtCore.QRect(960, 10, 71, 21))
        self.label_choose.setText("")
        self.label_choose.setObjectName("label_choose")
        SignalViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignalViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 31))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuexport_PDF = QtWidgets.QMenu(self.menubar)
        self.menuexport_PDF.setObjectName("menuexport_PDF")
        SignalViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignalViewer)
        self.statusbar.setObjectName("statusbar")
        SignalViewer.setStatusBar(self.statusbar)
        self.open_source1 = QtWidgets.QAction(SignalViewer)
        self.open_source1.setObjectName("open_source1")
        self.open_source2 = QtWidgets.QAction(SignalViewer)
        self.open_source2.setObjectName("open_source2")
        self.actioopen_source3 = QtWidgets.QAction(SignalViewer)
        self.actioopen_source3.setObjectName("actioopen_source3")
        self.actionexport_PDF = QtWidgets.QAction(SignalViewer)
        self.actionexport_PDF.setObjectName("actionexport_PDF")
        self.menufile.addAction(self.open_source1)
        self.menufile.addAction(self.open_source2)
        self.menufile.addAction(self.actioopen_source3)
        self.menuexport_PDF.addAction(self.actionexport_PDF)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuexport_PDF.menuAction())
        ls= ["ECG","EMG","EEG"]
        self.comboBox.addItems(ls)
        self.open_source1.triggered.connect(self.imp_ecg)
        self.open_source2.triggered.connect(self.imp_emg)
        self.actioopen_source3.triggered.connect(self.imp_eeg)
        self.Playback.clicked.connect(self.pb)
        self.shift_left.clicked.connect(self.backword)
        self.shift_right.clicked.connect(self.forword)
        self.zin.clicked.connect(self.zoomin)
        self.zout.clicked.connect(self.zoomout)
        self.actionexport_PDF.triggered.connect(self.report)
        self.figureecg.set_facecolor((0.29,0.29,0.29))
        self.figureemg.set_facecolor((0.29,0.29,0.29))
        self.figureeeg.set_facecolor((0.29,0.29,0.29))

        self.retranslateUi(SignalViewer)
        QtCore.QMetaObject.connectSlotsByName(SignalViewer)

    def retranslateUi(self, SignalViewer):
        _translate = QtCore.QCoreApplication.translate
        SignalViewer.setWindowTitle(_translate("SignalViewer", "MainWindow"))
        self.verticalWidget.setToolTip(_translate("SignalViewer", "<html><head/><body><p><br/></p></body></html>"))
        self.verticalWidget_2.setToolTip(_translate("SignalViewer", "<html><head/><body><p><br/></p></body></html>"))
        self.verticalWidget_3.setToolTip(_translate("SignalViewer", "<html><head/><body><p><br/></p></body></html>"))
        self.Playback.setText(_translate("SignalViewer", "►"))
        self.Playback.setShortcut(_translate("SignalViewer", "W"))
        self.shift_left.setText(_translate("SignalViewer", "<"))
        self.shift_left.setShortcut(_translate("SignalViewer", "E"))
        self.shift_right.setText(_translate("SignalViewer", ">"))
        self.shift_right.setShortcut(_translate("SignalViewer", "R"))
        self.zin.setText(_translate("SignalViewer", "+"))
        self.zin.setShortcut(_translate("SignalViewer", "Y"))
        self.zout.setText(_translate("SignalViewer", "-"))
        self.zout.setShortcut(_translate("SignalViewer", "T"))
        self.menufile.setTitle(_translate("SignalViewer", "file"))
        self.menuexport_PDF.setTitle(_translate("SignalViewer", "print"))
        self.open_source1.setText(_translate("SignalViewer", "open ECG"))
        self.open_source1.setShortcut(_translate("SignalViewer", "1"))
        self.open_source2.setText(_translate("SignalViewer", "open EMG"))
        self.open_source2.setShortcut(_translate("SignalViewer", "2"))
        self.actioopen_source3.setText(_translate("SignalViewer", "open EEG"))
        self.actioopen_source3.setShortcut(_translate("SignalViewer", "3"))
        self.actionexport_PDF.setText(_translate("SignalViewer", "export PDF"))
        self.actionexport_PDF.setShortcut(_translate("SignalViewer", "4"))


    def imp_ecg(self):
        self.path_ecg = QFileDialog.getOpenFileName(None, 'Open CSV ', '/home', "CSV (*.csv)")[0]
        ds_ecg= pd.read_csv(self.path_ecg)
        self.x_ecg=ds_ecg.iloc[0:-1,0].values
        self.y_ecg=ds_ecg.iloc[0:-1,1].values
        self.comboBox.setCurrentText("ECG")
        #self.path_ecg=0
        self.frame_counter_ecg=25
        self.flag_ecg =False
        #self.x_ecg=0
        #self.y_ecg=0
        ###############################
        
        #print(axis[60:80])
        ###############################
        


    def imp_emg(self):
        self.path_emg = QFileDialog.getOpenFileName(None, 'Open CSV ', '/home', "CSV (*.csv)")[0]
        ds_emg= pd.read_csv(self.path_emg)
        self.y_emg=ds_emg.iloc[0:-1,0].values
        self.axis_emg=np.linspace(0,len(self.y_emg)-1,len(self.y_emg))
        self.comboBox.setCurrentText("EMG")
        self.frame_counter_emg=25
        self.flag_emg =False
        self.pb()
    def imp_eeg(self):
        self.path_eeg = QFileDialog.getOpenFileName(None, 'Open CSV ', '/home', "CSV (*.csv)")[0]
        ds_eeg= pd.read_csv(self.path_eeg)
        self.y_eeg=ds_eeg.iloc[0:-1,0].values
        self.axis_eeg=np.linspace(0,len(self.y_eeg)-1,len(self.y_eeg))
        self.comboBox.setCurrentText("EEG")
        self.frame_counter_eeg=25
        self.flag_eeg =False
        self.pb()
    
    def pb(self):
        content = self.comboBox.currentText()
        if content=="ECG":
            if self.flag_ecg == False:
                self.flag_ecg =True
                c=self.frame_counter_ecg
                self.figureecg.clear()
                lines = [ax.plot([],[])[0] for ax in self.figureecg.axes]
                def update(i):
                    if not self.flag_ecg:
                        self.ani_ecg.event_source.stop()
                        self.canvasecg.flush_events()

                    else:
                        self.frame_counter_ecg=i+c
                        range_min=2*int(((self.frame_counter_ecg-25)+abs(self.frame_counter_ecg-25))/2)
                        xa=self.x_ecg[range_min:2*self.frame_counter_ecg]
                        y1=self.y_ecg[range_min:2*self.frame_counter_ecg]
                        ax=self.figureecg.gca()
                        ax.cla()
                        ax.set_ylim(min(self.y_ecg),max(self.y_ecg))
                        ax.set_facecolor((0.29,0.29,0.29))
                        ax.grid(True)
                        #ax.ylim(min(ym),max(ym))
                        ax.plot(xa,y1)
                        self.canvasecg.draw()
                    self.canvasecg.flush_events()
                    return lines
                self.ani_ecg = FuncAnimation(self.figureecg, update,frames=np.arange(0,int(len(self.x_ecg)/2)-25),interval=50,blit=True)
            else:
                self.flag_ecg=False
        elif content=="EMG":
            if self.flag_emg == False:
                self.flag_emg =True
                c=self.frame_counter_emg
                self.figureemg.clear()
                lines = [ax.plot([],[])[0] for ax in self.figureemg.axes]
                def update(i):
                    if not self.flag_emg:
                        self.ani_emg.event_source.stop()
                        self.canvasemg.flush_events()

                    else:
                        self.frame_counter_emg=i+c
                        range_min=2*int(((self.frame_counter_emg-25)+abs(self.frame_counter_emg-25))/2)
                        xa=self.axis_emg[range_min:self.frame_counter_emg*2]
                        y1=self.y_emg[range_min:2*self.frame_counter_emg]
                        ax=self.figureemg.gca()
                        ax.cla()
                        #ax.set_ylim(min(self.y_emg),max(self.y_emg))
                        ax.set_facecolor((0.29,0.29,0.29))
                        ax.grid(True)
                        #ax.set_ylim(min(self.y_emg),max(self.y_emg))
                        ax.plot(xa,y1)
                        self.canvasemg.draw()
                    self.canvasemg.flush_events()
                    return lines
                self.ani_emg = FuncAnimation(self.figureemg, update,frames=np.arange(0,int(len(self.y_emg)/2)-25),interval=50,blit=True)
            else:
                self.flag_emg=False
        elif content=="EEG":
            if self.flag_eeg == False:
                self.flag_eeg =True
                c=self.frame_counter_eeg
                self.figureeeg.clear()
                lines = [ax.plot([],[])[0] for ax in self.figureeeg.axes]
                def update(i):
                    if not self.flag_eeg:
                        self.ani_eeg.event_source.stop()
                        self.canvaseeg.flush_events()

                    else:
                        self.frame_counter_eeg=i+c
                        range_min=2*int(((self.frame_counter_eeg-25)+abs(self.frame_counter_eeg-25))/2)
                        xa=self.axis_eeg[range_min:self.frame_counter_eeg*2]
                        y1=self.y_eeg[range_min:2*self.frame_counter_eeg]
                        ax=self.figureeeg.gca()
                        ax.cla()     
                        #ax.set_ylim(min(self.y_eeg),max(self.y_eeg))
                        ax.set_facecolor((0.29,0.29,0.29))
                        ax.grid(True)                   
                        #ax.set_ylim(min(self.y_eeg),max(self.y_eeg))
                        ax.plot(xa,y1)
                        self.canvaseeg.draw()
                    self.canvaseeg.flush_events()
                    return lines
                self.ani_eeg = FuncAnimation(self.figureeeg, update,frames=np.arange(0,int(len(self.y_eeg)/2)-25),interval=50,blit=True)
            else:
                self.flag_eeg=False

    def backword(self):
        content = self.comboBox.currentText()
        if content=="ECG":
            if self.frame_counter_ecg>35:
                self.frame_counter_ecg=self.frame_counter_ecg-10
                range_min=2*int(((self.frame_counter_ecg-25)+abs(self.frame_counter_ecg-25))/2)
                xa=self.x_ecg[range_min:2*self.frame_counter_ecg]
                ya=self.y_ecg[range_min:2*self.frame_counter_ecg]
                self.figureecg.clear()
                ax=self.figureecg.add_subplot(111)
                ax.set_ylim(min(self.y_ecg),max(self.y_ecg))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.grid(True)
                #ax.set_ylim(min(self.y_ecg),max(self.y_ecg))
                ax.plot(xa,ya)
                self.canvasecg.draw()
                self.canvasecg.flush_events()
        elif content=="EMG":
            if self.frame_counter_emg>35:
                self.frame_counter_emg=self.frame_counter_emg-10
                range_min=2*int(((self.frame_counter_emg-25)+abs(self.frame_counter_emg-25))/2)
                xa=self.axis_emg[range_min:self.frame_counter_emg*2]
                ya=self.y_emg[range_min:2*self.frame_counter_emg]
                self.figureemg.clear()
                ax=self.figureemg.add_subplot(111)                        
                ax.set_ylim(min(self.y_emg),max(self.y_emg))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.grid(True)
                #ax.set_ylim(min(self.y_emg),max(self.y_emg))
                ax.plot(xa,ya)
                self.canvasemg.draw()
                self.canvasemg.flush_events()
        elif content=="EEG":
            if self.frame_counter_eeg>35:
                self.frame_counter_eeg=self.frame_counter_eeg-10
                range_min=2*int(((self.frame_counter_eeg-25)+abs(self.frame_counter_eeg-25))/2)
                xa=self.axis_eeg[range_min:self.frame_counter_eeg*2]
                ya=self.y_eeg[range_min:2*self.frame_counter_eeg]
                self.figureeeg.clear()
                ax=self.figureeeg.add_subplot(111)                        
                ax.set_ylim(min(self.y_eeg),max(self.y_eeg))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.grid(True)
                #ax.set_ylim(min(self.y_eeg),max(self.y_eeg))
                ax.plot(xa,ya)
                self.canvaseeg.draw()
                self.canvaseeg.flush_events()

    def forword(self):
        content = self.comboBox.currentText()
        if content=="ECG":
            if self.frame_counter_ecg<(len(self.x_ecg)/2-10):
                self.frame_counter_ecg=self.frame_counter_ecg+10
                range_min=2*int(((self.frame_counter_ecg-25)+abs(self.frame_counter_ecg-25))/2)
                xa=self.x_ecg[range_min:2*self.frame_counter_ecg]
                ya=self.y_ecg[range_min:2*self.frame_counter_ecg]
                self.figureecg.clear()
                ax=self.figureecg.add_subplot(111)                        
                ax.set_ylim(min(self.y_ecg),max(self.y_ecg))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.grid(True)
                #ax.set_ylim(min(self.y_ecg),max(self.y_ecg))
                ax.plot(xa,ya)
                self.canvasecg.draw()
                self.canvasecg.flush_events()
        elif content=="EMG":
            if self.frame_counter_emg<(len(self.y_emg)/2-10):
                self.frame_counter_emg=self.frame_counter_emg+10
                range_min=2*int(((self.frame_counter_emg-25)+abs(self.frame_counter_emg-25))/2)
                xa=self.axis_emg[range_min:self.frame_counter_emg*2]
                ya=self.y_emg[range_min:2*self.frame_counter_emg]
                self.figureemg.clear()
                ax=self.figureemg.add_subplot(111)                        
                ax.set_ylim(min(self.y_emg),max(self.y_emg))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.grid(True)
                #ax.set_ylim(min(self.y_emg),max(self.y_emg))
                ax.plot(xa,ya)
                self.canvasemg.draw()                
                self.canvasemg.flush_events()
        elif content=="EEG":
            if self.frame_counter_eeg<(len(self.y_eeg)/2-10):
                self.frame_counter_eeg=self.frame_counter_eeg+10            
                range_min=2*int(((self.frame_counter_eeg-25)+abs(self.frame_counter_eeg-25))/2)
                xa=self.axis_eeg[range_min:self.frame_counter_eeg*2]
                ya=self.y_eeg[range_min:2*self.frame_counter_eeg]
                self.figureeeg.clear()
                ax=self.figureeeg.add_subplot(111)                        
                ax.set_ylim(min(self.y_eeg),max(self.y_eeg))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.grid(True)
                #ax.set_ylim(min(self.y_eeg),max(self.y_eeg))
                ax.plot(xa,ya)
                self.canvaseeg.draw()                
                self.canvaseeg.flush_events()

    def zoomin(self):
        content = self.comboBox.currentText()
        if content=="ECG":
            range_min=2*int(((self.frame_counter_ecg-25)+abs(self.frame_counter_ecg-25))/2)
            xa=self.x_ecg[range_min:2*self.frame_counter_ecg]
            ya=self.y_ecg[range_min:2*self.frame_counter_ecg]
            self.figureecg.clear()
            ax=self.figureecg.add_subplot(111)
            #ax.set_ylim(min(self.y_ecg),max(self.y_ecg))
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            #ax.set_ylim(min(self.y_ecg),max(self.y_ecg))
            ax.margins(x=-0.3,y=0.05)
            ax.plot(xa,ya)
            self.canvasecg.draw()                
            self.canvasecg.flush_events()
        elif content=="EMG":
            range_min=2*int(((self.frame_counter_emg-25)+abs(self.frame_counter_emg-25))/2)
            xa=self.axis_emg[range_min:self.frame_counter_emg*2]
            ya=self.y_emg[range_min:2*self.frame_counter_emg]
            self.figureemg.clear()
            ax=self.figureemg.add_subplot(111)                        
            #ax.set_ylim(min(self.y_emg),max(self.y_emg))
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            ax.margins(x=-0.2,y=0.05)
            ax.plot(xa,ya)
            self.canvasemg.draw()                
            self.canvasemg.flush_events()
        elif content=="EEG":
            range_min=2*int(((self.frame_counter_eeg-25)+abs(self.frame_counter_eeg-25))/2)
            xa=self.axis_eeg[range_min:self.frame_counter_eeg*2]
            ya=self.y_eeg[range_min:2*self.frame_counter_eeg]
            self.figureeeg.clear()
            ax=self.figureeeg.add_subplot(111)
            #ax.set_ylim(min(self.y_eeg),max(self.y_eeg))
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            ax.margins(x=-0.2,y=0.05)
            ax.plot(xa,ya)
            self.canvaseeg.draw()
            self.canvaseeg.flush_events()

    def zoomout(self):
        content = self.comboBox.currentText()
        if content=="ECG":
            range_min=2*int(((self.frame_counter_ecg-25)+abs(self.frame_counter_ecg-25))/2)
            xa=self.x_ecg[range_min:2*self.frame_counter_ecg]
            ya=self.y_ecg[range_min:2*self.frame_counter_ecg]
            self.figureecg.clear()
            ax=self.figureecg.add_subplot(111)
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            #ax.set_ylim(min(self.y_ecg),max(self.y_ecg))
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            ax.margins(x=0.05,y=2)
            ax.plot(xa,ya)
            self.canvasecg.draw()                
            self.canvasecg.flush_events()
        elif content=="EMG":
            range_min=2*int(((self.frame_counter_emg-25)+abs(self.frame_counter_emg-25))/2)
            xa=self.axis_emg[range_min:self.frame_counter_emg*2]
            ya=self.y_emg[range_min:2*self.frame_counter_emg]
            self.figureemg.clear()
            ax=self.figureemg.add_subplot(111)
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            ax.margins(x=0.05,y=2)
            ax.plot(xa,ya)
            self.canvasemg.draw()                
            self.canvasemg.flush_events()
        elif content=="EEG":
            range_min=2*int(((self.frame_counter_eeg-25)+abs(self.frame_counter_eeg-25))/2)
            xa=self.axis_eeg[range_min:self.frame_counter_eeg*2]
            ya=self.y_eeg[range_min:2*self.frame_counter_eeg]
            self.figureeeg.clear()
            ax=self.figureeeg.add_subplot(111)
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            ax.margins(x=0.05,y=10)
            ax.plot(xa,ya)
            self.canvaseeg.draw()                
            self.canvaseeg.flush_events()
    def report(self):
        ecg = pd.read_csv(self.path_ecg)
        x1=ecg.iloc[0:-1,0].values
        y1=ecg.iloc[0:-1,1].values

        eeg = pd.read_csv(self.path_eeg)
        y2=eeg.iloc[0:-1,0].values
        x2=[]
        for i in range (0,len(y2),1):
            x2.append(i)

        emg1 = pd.read_csv(self.path_emg)
        y3=emg1.iloc[0:-1,0].values
        x3=[]
        for i in range (0,len(y3),1):
            x3.append(i)
        fig=plt
        def Signalplot (a,b,c,d,e,f):
            plt.subplot(2, 3, 1)
            plt.title("ECG")
            plt.xlabel('Time')
            plt.ylabel('milivolt')
            plt.plot(a, b)

            # EEG
            plt.subplot(2, 3, 2)
            plt.title("EEG")
            plt.xlabel('Samples')
            plt.ylabel('Amplitude')
            plt.plot(c, d)
            # EMG
            plt.subplot(2, 3, 3)
            plt.title("EMG")
            plt.xlabel('Samples')
            plt.ylabel('Amplitude')
            plt.plot(e, f)
        def Spplot (a,b,c,):
            plt.subplot(2, 3, 4)
            powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(a)
            plt.xlabel('Time')
            plt.ylabel('Frequency')
            # EEG
            plt.subplot(2, 3, 5)
            powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(b)
            plt.xlabel('Time')
            plt.ylabel('Frequency')
            # EMG
            plt.subplot(2, 3, 6)
            plt.xlabel('Time')
            plt.ylabel('Frequency')
            powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(c)

        Signalplot(x1,y1,x2,y2,x3,y3)
        Spplot(y1,y2,y3)
        fig.tight_layout()
        print("printed")
        plt.savefig('Report_Team_2.pdf')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignalViewer = QtWidgets.QMainWindow()
    ui = Ui_SignalViewer()
    ui.setupUi(SignalViewer)
    SignalViewer.show()
    sys.exit(app.exec_())
