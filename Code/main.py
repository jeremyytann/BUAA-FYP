import os
import json
import sys

from application import *
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    QMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
  
    self.show()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  
  window = MainWindow()
  window.show()
  
  app.exec()
  
