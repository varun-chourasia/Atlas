from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
import sys
from gui.dashboard import Dashboard
from PyQt5.QtGui import QKeySequence

class AtlasWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Dashboard()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AtlasWindow()
    window.showFullScreen()      # or .showMaximized() if you prefer
    sys.exit(app.exec_())
