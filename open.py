import sys
from PyQt5.QtWidgets import Qapplication, QWidget 

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()
        
if __name__ == '__main__':
    app = Qapplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    