from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from magneto import Magneto

class Logan(QObject):
    #data = Magneto()
    @pyqtSlot(int, result=int)
    def compute(self, value):
        return value * 2

    @pyqtSlot()
    def quit(self):
        QApplication.quit()

    @pyqtSlot(str, str, result=str)
    def bind_login(self, username, password):
        try:
            print "Enter the credentials in the UI"
            print "Username : ", username
            print "Password : ", password
            username = str(username)
            password = str(password)
            if username or password is None:
                return "ENTERED_WASTE_CREDENTIALS"
            if self.data.is_valid_credential(username, password):
                return ""
        except Exception as e:
            return "ENTERED_WASTE_CREDENTIALS"