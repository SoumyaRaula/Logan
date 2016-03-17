"""
@ Author : rsoumyassdi
@ Date : 11 Mar 2016
"""
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from raven import Logan


class Window(QWidget):
    def __init__(self):
        """
        1. Create the web view.
        2. Create the window box layout.
        3. Attach the Window object to the Java code to call the QT Method.
        4. Load the URL using QURL.
        """
        super(Window, self).__init__()
        # Create the web view
        view = QWebView(self)
        layout = QVBoxLayout(self)
        layout.addWidget(view)

        self.logan = Logan(self)
        view.page().mainFrame().addToJavaScriptWindowObject("logan", self.logan)
        view.load(QUrl("batman/login.html"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    # Make the window size 1024 * 800
    window.resize(1024, 800)
    # This shows the window on screen
    window.show()
    # Executes the QT application
    app.exec_()