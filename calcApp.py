from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

class CalcUi(QtWidgets.QMainWindow):
    def __init__(self):
        '''constructor method'''
        super(CalcUi, self).__init__()
        uic.loadUi('calc_window.ui', self)
        self.OutputLbl.setAlignment(QtCore.Qt.AlignRight)
        self.show()
        #add button event listeners here
        self.current = ""
        self.display = ""
        self.Button0.clicked.connect(lambda: self.numButton("0"))
        self.Button1.clicked.connect(lambda: self.numButton("1"))
        self.Button2.clicked.connect(lambda: self.numButton("2"))
        self.Button3.clicked.connect(lambda: self.numButton("3"))
        self.Button4.clicked.connect(lambda: self.numButton("4"))
        self.Button5.clicked.connect(lambda: self.numButton("5"))
        self.Button6.clicked.connect(lambda: self.numButton("6"))
        self.Button7.clicked.connect(lambda: self.numButton("7"))
        self.Button8.clicked.connect(lambda: self.numButton("8"))
        self.Button9.clicked.connect(lambda: self.numButton("9"))
        
    def numButton(self,param):
        '''Handles button click'''
        self.current = self.current+str(param)
        self.OutputLbl.setText(self.current)
        self.display = self.display+str(param)
        self.currentCalc.setText(self.display)


def mainApplication():
    app = QtWidgets.QApplication(sys.argv)
    window = CalcUi()
    app.exec_()
    app.quit()
    sys.exit(app.exec_()) #execute the application event loop
mainApplication()