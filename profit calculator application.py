
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 P&L calculator'
        self.left = 50
        self.top = 50
        self.width = 500
        self.height = 500
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #create a label
        self.titleLabel = QLabel(self)
        self.titleLabel.setText("P&L calculator")
        self.titleLabel.move(100,10)
        self.titleLabel.setLineWidth(100)

        #create Buy label
        self.buyLabel = QLabel(self)
        self.buyLabel.setText("buy Price")
        self.buyLabel.move(10,60)
        self.buyLabel.setLineWidth(100)


        # Create buy Price  textbox
        self.buyPriceBox = QLineEdit(self)
        self.buyPriceBox.windowTitle = "buy"
        self.buyPriceBox.move(100, 60)
        self.buyPriceBox.resize(100,40)


         # Create sell Price  textbox
        self.sellPriceBox = QLineEdit(self)
        self.sellPriceBox.windowTitle = "sell"
        self.sellPriceBox.move(100, 120)
        self.sellPriceBox.resize(100,40)

        #create Buy label
        self.sellPricelabel = QLabel(self)
        self.sellPricelabel.setText("sell Price")
        self.sellPricelabel.move(10,120)
        self.sellPricelabel.setLineWidth(100)


         #create Result label
        self.Resultlabel = QLabel(self)
        self.Resultlabel.setText("Percent:")
        self.Resultlabel.move(10,250)
        self.Resultlabel.setLineWidth(100)

        #create Result percent label
        self.ResultPercentlabel = QLabel(self)
        self.ResultPercentlabel.setText("")
        self.ResultPercentlabel.move(90,250)
        self.ResultPercentlabel.setLineWidth(100)




        
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,200)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        buyPrice = float(self.buyPriceBox.text()) 
        sellPrice = float(self.sellPriceBox.text())
        PLpercent = ((sellPrice - buyPrice) / buyPrice )*100.00
        diff = sellPrice - buyPrice
        result = str(PLpercent)
        
        self.ResultPercentlabel.setText(str(result))
        
        #QMessageBox.question(self, 'Message - pythonspot.com', "pl percent = : " +  str(result) , QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())