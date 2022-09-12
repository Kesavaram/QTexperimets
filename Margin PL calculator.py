
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
        self.width = 750
        self.height = 750
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.xPosPLOffset = 225
        self.yPosPLOffset = 25

        #create a label
        self.titleLabel = QLabel(self)
        self.titleLabel.setText("P&L calculator")
        self.titleLabel.move(self.xPosPLOffset + 100,self.yPosPLOffset + 10)
        self.titleLabel.setLineWidth(100)

        #create Buy label
        self.buyLabel = QLabel(self)
        self.buyLabel.setText("Buy Price")
        self.buyLabel.move(self.xPosPLOffset + 10,self.yPosPLOffset + 60 )
        self.buyLabel.setLineWidth(100)


        # Create buy Price  textbox
        self.buyPriceBox = QLineEdit(self)
        self.buyPriceBox.windowTitle = "buy"
        self.buyPriceBox.move(self.xPosPLOffset + 100, self.yPosPLOffset + 60)
        self.buyPriceBox.resize(100,40)


         # Create sell Price  textbox
        self.sellPriceBox = QLineEdit(self)
        self.sellPriceBox.windowTitle = "sell"
        self.sellPriceBox.move(self.xPosPLOffset + 100, self.yPosPLOffset + 120)
        self.sellPriceBox.resize(100,40)

        #create sell price label
        self.sellPricelabel = QLabel(self)
        self.sellPricelabel.setText("Sell Price")
        self.sellPricelabel.move(self.xPosPLOffset + 10,self.yPosPLOffset + 120)
        self.sellPricelabel.setLineWidth(100)



        #create Margin Multiplier label
        self.marginMultLabel = QLabel(self)
        self.marginMultLabel.setText("Margin multiplier")
        self.marginMultLabel.move(self.xPosPLOffset - 25,self.yPosPLOffset + 185)
        self.marginMultLabel.adjustSize()
        self.marginMultLabel.setLineWidth(100)

        #create  Margin Multiplier textbox
        self.marginMultBox = QLineEdit(self)
        self.marginMultBox.move(self.xPosPLOffset + 100, self.yPosPLOffset + 180)
        self.marginMultBox.resize(100,40)


        #create fee percent label
        self.sellPricelabel = QLabel(self)
        self.sellPricelabel.setText("Fees percent")
        self.sellPricelabel.move(self.xPosPLOffset + 10,self.yPosPLOffset + 300)
        self.sellPricelabel.setLineWidth(100)

        #create fees percent textbox
        self.feesPercenteBox = QLineEdit(self)
        self.feesPercenteBox.windowTitle = "sell"
        self.feesPercenteBox.move(self.xPosPLOffset + 100, self.yPosPLOffset + 300)
        self.feesPercenteBox.resize(100,40)


         #create Result label
        self.Resultlabel = QLabel(self)
        self.Resultlabel.setText("Percent:")
        self.Resultlabel.move(self.xPosPLOffset + 10,self.yPosPLOffset + 500)
        self.Resultlabel.setLineWidth(100)

        #create Result percent label
        self.ResultPercentlabel = QLabel(self)
        self.ResultPercentlabel.setText("")
        self.ResultPercentlabel.move(self.xPosPLOffset + 90,self.yPosPLOffset + 500)
        self.ResultPercentlabel.setLineWidth(100)

        # Create a button in the window
        self.button = QPushButton('Calculate', self)
        self.button.setDefault = True
        self.button.setAutoDefault = False
        self.button.move(self.xPosPLOffset + 20,self.yPosPLOffset + 400)
        
        # connect button to function on_click
       
        self.button.pressed.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        buyPrice = float(self.buyPriceBox.text()) 
        sellPrice = float(self.sellPriceBox.text())
        feesPercent = float(self.feesPercenteBox.text())
        marginMultiplier = float(self.marginMultBox.text())
        diff = marginMultiplier*(sellPrice - buyPrice)
        tradingFees = marginMultiplier*feesPercent*(buyPrice + sellPrice)/100.00
        netAmt = diff - tradingFees
        PLpercent = ((netAmt) / buyPrice )*100.00 
        result = f'{PLpercent:.2f}' #formats output to 2 decimal places.
        
        self.ResultPercentlabel.setText(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())