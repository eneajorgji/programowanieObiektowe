import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDoubleSpinBox

import sys

class MyApp(QWidget):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)

        dsbox = QDoubleSpinBox(self)
        dsbox.setDecimals(1)
        dsbox.setValue(100.00)
        dsbox.setMinimum(1.00)
        dsbox.setMaximum(3500.00)
        dsbox.setSingleStep(1.00)
        dsbox.setSuffix("mm")

        dsbox.valueChanged.connect(self.on_value_changed)

        self.show()

    def on_value_changed(self):
        print("You are now in the sub function.")
        print (self.dsbox.value()) #Problem is hier

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())