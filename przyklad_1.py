import sys

import numpy as np

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib import pyplot as plt

import sympy as sy

# Zadanie 3
print("\n### Zadanie 3 ###\n")


class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = QWidget()
        self.setCentralWidget(self.main)

        layout = QHBoxLayout(self.main)

        # Zdefiniowanie canvasa na którym beda rysowane wykresy
        self.figure = Figure(figsize=(6, 6))
        self.ax = self.figure.subplots()

        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        side_layout = QVBoxLayout(self.main)
        layout.addLayout(side_layout)

        # zdefiniowanie textboxu FUNCTION
        self.label = QLabel('Function:', self)

        self.textbox_function = QLineEdit(self)
        self.textbox_function.move(20, 20)

        side_layout.addWidget(self.label)
        side_layout.addWidget(self.textbox_function)
        print(self.textbox_function)

        # zdefiniowanie textboxu MIN
        self.label = QLabel('Min:', self)

        self.spinbox_min = QDoubleSpinBox(self)
        self.spinbox_min.setRange(-100000, 100000)
        self.spinbox_min.setSingleStep(1)

        side_layout.addWidget(self.label)
        side_layout.addWidget(self.spinbox_min)

        # zdefiniowanie textboxu MAX
        self.label = QLabel('Max:', self)

        self.spinbox_max = QDoubleSpinBox(self)
        self.spinbox_max.setRange(-100000, 100000)
        self.spinbox_max.setSingleStep(1)

        side_layout.addWidget(self.label)
        side_layout.addWidget(self.spinbox_max)

        # zdefiniowanie textboxu STEP
        self.label = QLabel('Step:', self)

        self.spinbox_step = QDoubleSpinBox(self)
        self.spinbox_step.setRange(0, 100000)
        self.spinbox_step.setSingleStep(1)

        side_layout.addWidget(self.label)
        side_layout.addWidget(self.spinbox_step)

        # Zdefiniowanie przycisku i podlaczenie funkcji do niego
        self.calculate_button = QPushButton("Draw")
        self.calculate_button.clicked.connect(self.calculate_slot)
        side_layout.addWidget(self.calculate_button)

        side_layout.addStretch(1)

    def calculate_slot(self):
        self.ax.clear()

        func = self.textbox_function.text()
        print(f"Funkcja to: f(x)= {func}")

        s_min = int(self.spinbox_min.value())
        s_max = int(self.spinbox_max.value())
        s_step = int(self.spinbox_step.value())

        x = np.linspace(s_min, s_max, s_step)

        # Funkcja
        func_y = eval(func)

        self.ax.plot(x, func_y)
        self.ax.grid(linestyle="--", alpha=0.5)

        # Oznaczenie pola
        self.ax.fill_between(x, func_y, color="blue", alpha=0.5)

        self.figure.canvas.draw()

        # Calka nieoznaczone funkcji
        integral_func = sy.integrate(func)

        # Calka oznaczone funkcji
        x_symbol = sy.Symbol("x")
        definite_integral_func = sy.integrate(func, (x_symbol, s_min, s_max))


if __name__ == '__main__':
    qapp = QApplication.instance()
    if not qapp:
        qapp = QApplication(sys.argv)

    app = ApplicationWindow()
    app.setWindowTitle("Aplikacja")
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()