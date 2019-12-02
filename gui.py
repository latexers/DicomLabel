import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1200, 900)
        self.setWindowTitle("Dicom Label")
        self.setWindowIcon(QIcon('./Images/icon.png'))
        self.show()
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        toolBar = self.addToolBar('Exit')

        fileMenu.addAction(exitAction)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())