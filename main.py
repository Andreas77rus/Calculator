import sys
from PyQt5 import QtWidgets, QtCore
import gui
from math import sqrt


class CalculatorApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.nums = '1234567890.'
        self.ops = '+/***200'
        self.setupUi(self)
        self.build()


    def build(self):
        self.clear.clicked.connect(self.clearSpace)

        self.equal.clicked.connect(self.getResult)

        self.num1.clicked.connect(lambda: self.ab('1'))
        self.zero.clicked.connect(lambda: self.ab('0'))
        self.num2.clicked.connect(lambda: self.ab('2'))
        self.num3.clicked.connect(lambda:self.ab('3'))
        self.num4.clicked.connect(lambda:self.ab('4'))
        self.num5.clicked.connect(lambda:self.ab('5'))
        self.num6.clicked.connect(lambda:self.ab('6'))
        self.num7.clicked.connect(lambda:self.ab('7'))
        self.num8.clicked.connect(lambda:self.ab('8'))
        self.num9.clicked.connect(lambda:self.ab('9'))
        self.dot.clicked.connect(lambda:self.ab('.'))
        self.doublezero.clicked.connect(lambda: self.abOP('00'))


        self.plus.clicked.connect(lambda: self.abOP('+'))
        self.devision.clicked.connect(lambda: self.abOP('/'))
        self.umn.clicked.connect(lambda: self.abOP('*'))
        self.inDouble.clicked.connect(lambda: self.abOP('**2'))
        self.koren.clicked.connect(lambda: self.ab('√'))
        self.minus.clicked.connect(lambda: self.ab('-'))


    def ab(self, s):
        if self.result.text() != '':
            self.clearSpace()
        self.Exercise.setText(str(self.Exercise.text()) + s)

    def abOP(self, s):
        if self.result.text() != '':
            self.clearSpace()
        if self.Exercise.text() == '':
            s = ''
        else:
            self.Exercise.setText(str(self.Exercise.text()) + s)
        try:
            if self.Exercise.text()[-1] in self.ops:
                s = ''
            else:
                self.Exercise.setText(str(self.Exercise.text()) + s)

        except Exception:
            pass



    def clearSpace(self):
        self.result.clear()
        self.Exercise.clear()


    def getResult(self):
        ex = str(self.Exercise.text())

        if '√' in ex:
            indexOfSim = ex.index('√')

            finishIndex = indexOfSim+1
            while True:
                try:
                    if ex[finishIndex] in self.nums:

                        finishIndex+=1
                    elif not ex[finishIndex] in self.nums:
                        break
                except Exception:
                    break

            snum = sqrt(float(ex[indexOfSim+1:finishIndex]))
            ex = ex.replace(ex[indexOfSim:finishIndex], str(snum))
        try:
            res = eval(ex)
        except Exception:
            res = ''

        self.result.setText(str(res))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
