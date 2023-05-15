from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QSplitter

def boardWindow():
    global but11, but12, but13, but21, but22, but23, but31, but32, but33
    window = QWidget()
    window.setWindowTitle('Tic-tac-toe game')
    window.setFixedSize(600, 600)

    but11 = QPushButton(' ')
    but12 = QPushButton(' ')
    but13 = QPushButton(' ')
    but21 = QPushButton(' ')
    but22 = QPushButton(' ')
    but23 = QPushButton(' ')
    but31 = QPushButton(' ')
    but32 = QPushButton(' ')
    but33 = QPushButton(' ')

    but11.setMaximumSize(100, 100)
    but12.setMaximumSize(100, 100)
    but13.setMaximumSize(100, 100)
    but21.setMaximumSize(100, 100)
    but22.setMaximumSize(100, 100)
    but23.setMaximumSize(100, 100)
    but31.setMaximumSize(100, 100)
    but32.setMaximumSize(100, 100)
    but33.setMaximumSize(100, 100)

    vLeftLine = QVBoxLayout()
    vLeftLine.addWidget(but11)
    vLeftLine.addWidget(but21)
    vLeftLine.addWidget(but31)

    vCentLine = QVBoxLayout()
    vCentLine.addWidget(but12)
    vCentLine.addWidget(but22)
    vCentLine.addWidget(but32)

    vRightLine = QVBoxLayout()
    vRightLine.addWidget(but13)
    vRightLine.addWidget(but23)
    vRightLine.addWidget(but33)

    hLine = QHBoxLayout()
    hLine.addLayout(vLeftLine)
    hLine.addLayout(vCentLine)
    hLine.addLayout(vRightLine)

    window.setLayout(hLine)

    return window

def putOnBoard(x, y, symb):
    if x == 1:
        if y == 1:
            but11.setText(symb)
        if y == 2:
            but12.setText(symb)
        if y == 3:
            but13.setText(symb)
    if x == 2:
        if y == 1:
            but21.setText(symb)
        if y == 2:
            but22.setText(symb)
        if y == 3:
            but23.setText(symb)
    if x == 3:
        if y == 1:
            but31.setText(symb)
        if y == 2:
            but32.setText(symb)
        if y == 3:
            but33.setText(symb)

if __name__ == "__main__":
    app = QApplication([])
    boardWin = boardWindow()
    boardWin.show()
    app.exec_()
