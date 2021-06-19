import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon


class NazwaNaszejKlasy(QMainWindow):
    # """
    # https://pythonspot.com/category/pyqt5/
    # https://doc.qt.io/qt-5/qwidget.html
    # https://doc.qt.io/qt-5/
    # """
    def __init__(self):
        super().__init__()
        self.licznik = 0
        self.title = 'Programowanie Obiektowe 2.0'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 180
        self.initUI()

    def initUI(self):
        buttonR = QMessageBox.question(self, "Nazwa", "Pytanie", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonR == QMessageBox.Yes:
            print("kliknieto YES")
            self.width = 1040
        else:
            print("Kliknieto NO")
            self.width = 440

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('StatusBar naszego okienka') # dziedziczenie po QWidget

        button = QPushButton('Nazwa przycisku', self)
        button.setToolTip('Podpowiedz - co oznacza klikniecie w ten przycisk')
        button.move(10,5)
        button.clicked.connect(self.on_click)


        self.show()

    @pyqtSlot()
    def on_click(self):
        self.licznik += 1
        print('klinknieto', self.licznik)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NazwaNaszejKlasy()
    sys.exit(app.exec_())
