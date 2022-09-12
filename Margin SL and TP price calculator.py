
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

        self.xPosPLOffset = 150
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


        #create Buy QTY label
        


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
        self.Resultlabel.setText("PL Percent:")
        self.Resultlabel.move(self.xPosPLOffset -30 ,self.yPosPLOffset + 500)
        self.Resultlabel.setLineWidth(100)

        #create Result percent label
        self.ResultPercentlabel = QLabel(self)
        self.ResultPercentlabel.setText("")
        self.ResultPercentlabel.move(self.xPosPLOffset +60,self.yPosPLOffset + 500)
        self.ResultPercentlabel.setLineWidth(100)

        # Create a button in the window
        self.CalcPercentButton = QPushButton('Calculate PL percent', self)
        self.CalcPercentButton.setDefault = True
        self.CalcPercentButton.setAutoDefault = False
        self.CalcPercentButton.adjustSize()
        self.CalcPercentButton.move(self.xPosPLOffset - 40,self.yPosPLOffset + 400)


        self.marginSLTPxPosOffset = self.xPosPLOffset + 300;
        self.marginSLTPyPosOffset = self.yPosPLOffset;   

        #create a label
        self.MarginPriceCalcLabel = QLabel(self)
        self.MarginPriceCalcLabel.setText("Margin SL & TP price calculator")
        self.MarginPriceCalcLabel.adjustSize()
        self.MarginPriceCalcLabel.move(self.marginSLTPxPosOffset ,self.marginSLTPyPosOffset + 15)
        self.MarginPriceCalcLabel.setLineWidth(100)  

        #create Buy price for SL TP label
        self.buyLabelSLTP = QLabel(self)
        self.buyLabelSLTP.setText("Buy Price ")
        self.buyLabelSLTP.move(self.marginSLTPxPosOffset ,self.marginSLTPyPosOffset + 70 )
        self.buyLabelSLTP.setLineWidth(100)
        self.buyLabelSLTP.adjustSize()


        # Create buy Price  textbox
        self.buyPriceBoxSLTP = QLineEdit(self)
        self.buyPriceBoxSLTP.windowTitle = "buy"
        self.buyPriceBoxSLTP.move(self.marginSLTPxPosOffset  + 130, self.marginSLTPyPosOffset + 60)
        self.buyPriceBoxSLTP.resize(100,40)


         #create TP label
        self.TP = QLabel(self)
        self.TP.setText("TP USDT")
        self.TP.move(self.marginSLTPxPosOffset ,self.marginSLTPyPosOffset + 130 )
        self.TP.setLineWidth(100)
 
        # Create TP  textbox
        self.TPbox = QLineEdit(self)
        self.TPbox.windowTitle = "TP USDT"
        self.TPbox.move(self.marginSLTPxPosOffset  + 130, self.marginSLTPyPosOffset + 120)
        self.TPbox.resize(100,40)

        # create SL label
        self.TP = QLabel(self)
        self.TP.setText("SL USDT")
        self.TP.move(self.marginSLTPxPosOffset ,self.marginSLTPyPosOffset + 180 )
        self.TP.setLineWidth(100)
 
        # Create TP  textbox
        self.TPbox = QLineEdit(self)
        self.TPbox.windowTitle = "SL USDT"
        self.TPbox.move(self.marginSLTPxPosOffset  + 130, self.marginSLTPyPosOffset + 170)
        self.TPbox.resize(100,40)



        self.buyQTYLabel = QLabel(self)
        self.buyQTYLabel.setText("Buy Qty(USDT)")
        self.buyQTYLabel.move(self.marginSLTPxPosOffset ,self.marginSLTPyPosOffset + 230)
        self.buyQTYLabel.adjustSize()
        self.buyQTYLabel.setLineWidth(100)
        #create Buy Qty box
        self.TPpriceValue = QLabel(self)
        self.TPpriceValue.setText("")
        self.TPpriceValue.move(self.marginSLTPxPosOffset +60,self.marginSLTPyPosOffset + 500)
        self.TPpriceValue.setLineWidth(100)

        self.CalcPricesButton = QPushButton('Calculate prices for SL and TP', self)
        self.CalcPricesButton.setDefault = True
        self.CalcPricesButton.setAutoDefault = False
        self.CalcPricesButton.adjustSize()
        self.CalcPricesButton.move(self.marginSLTPxPosOffset - 10 ,self.marginSLTPyPosOffset + 400)

        self.TPpriceLabel = QLabel(self)
        self.TPpriceLabel.setText("Take profit price:")
        self.TPpriceLabel.adjustSize()
        self.TPpriceLabel.move(self.marginSLTPxPosOffset -15 ,self.marginSLTPyPosOffset + 460)
        self.TPpriceLabel.setLineWidth(100)

        #create Result percent label
        self.TPpriceValue = QLabel(self)
        self.TPpriceValue.setText("")
        self.TPpriceValue.move(self.marginSLTPxPosOffset +60,self.marginSLTPyPosOffset + 460)
        self.TPpriceValue.setLineWidth(100)

        self.SLpriceLabel = QLabel(self)
        self.SLpriceLabel.setText("Stop Loss price:")
        self.SLpriceLabel.adjustSize()
        self.SLpriceLabel.move(self.marginSLTPxPosOffset -15 ,self.marginSLTPyPosOffset + 500)
        self.SLpriceLabel.setLineWidth(100)

        



        #create  Margin Multiplier textbox
        self.buyQtyBox = QLineEdit(self)
        self.buyQtyBox.move(self.marginSLTPxPosOffset + 125, self.marginSLTPyPosOffset + 220)
        self.buyQtyBox.resize(100,40)




        # connect button to function on_click
        self.CalcPercentButton.pressed.connect(self.on_click)
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