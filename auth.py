

# importing libraries 

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys 
import os


 
 
class WelcomeWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it 
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label.resize(200, 20) 
        self.label.move(190, 50)
        self.label.setText("Welcome")
  
        # setting geometry 
        self.setGeometry(100, 100, 600, 600) 
  
        # calling method 
  
        self.UiComponents() 
        # showing all the widgets 
        self.show() 
    def UiComponents(self): 
        
        #YELLOW
        # creating a push button 
        yellow_btn = QPushButton("yellow", self) 
 
        # setting geometry of button 
        yellow_btn.setGeometry(200, 200, 100, 100) 
  
        # adding action to a button 
  
        # setting image to the button 
        yellow_btn.setStyleSheet("background-image : url(yellow.jpg);") 
  
      
        

 
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
        # setting title 
        self.setWindowTitle("Image Password ") 
        self.label_1 = QLabel(self)
        self.label_1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label_1.resize(200, 20) 
        self.label_1.move(190, 50)
        self.label_1.setText("Select PassImages")
  
        # setting geometry 
        self.setGeometry(100, 100, 600, 600) 
  
        # calling method 
        self.UiComponents() 
  
        # showing all the widgets 
        self.show() 



  
    # method for widgets 
    def UiComponents(self): 
        
        #YELLOW
        # creating a push button 
        yellow_btn = QPushButton("yellow", self) 
 
        # setting geometry of button 
        yellow_btn.setGeometry(200, 200, 100, 100) 
  
        # adding action to a button 
        yellow_btn.clicked.connect(self.clickme) 
  
        # setting image to the button 
        yellow_btn.setStyleSheet("background-image : url(yellow.jpg);") 
  
        #BLUE
        # creating a push button 
        blue_btn = QPushButton("blue", self) 
  
        # setting geometry of button 
        blue_btn.setGeometry(100, 100, 100, 100) 
  
        # adding action to a button 
        blue_btn.clicked.connect(self.clickme) 
  
        # setting image to the button 
        blue_btn.setStyleSheet("background-image : url(blue.jpg);") 
       

        #GREEN
        # creating a push button 
        green_btn = QPushButton("green", self) 
  
        # setting geometry of button 
        green_btn.setGeometry(100, 200, 100, 100) 
  
        # adding action to a button 
        green_btn.clicked.connect(self.clickme) 
        # setting image to the button 
        green_btn.setStyleSheet("background-image : url(green.jpg);") 

        #WHITE
        # creating a push button 
        white_btn = QPushButton("white", self) 
 
        # setting geometry of button 
        white_btn.setGeometry(200, 100, 100, 100) 
  
        # adding action to a button 
        white_btn.clicked.connect(self.clickme) 
  
        # setting image to the button 
        white_btn.setStyleSheet("background-image : url(white.jpg);") 
        #BLACK
        # creating a push button 
        black_btn = QPushButton("black", self) 
 
        # setting geometry of button 
        black_btn.setGeometry(300, 200, 100, 100) 
  
        # adding action to a button 
        black_btn.clicked.connect(self.clickme) 
  
        # setting image to the button 
        black_btn.setStyleSheet("background-image : url(black.jpg);") 
        #PURPLE
        # creating a push button 
        purple_btn = QPushButton("purple", self) 
 
        # setting geometry of button 
        purple_btn.setGeometry(300, 100, 100, 100) 
  
        # adding action to a button 
        purple_btn.clicked.connect(self.clickme) 
  
        # setting image to the button 
        purple_btn.setStyleSheet("background-image : url(purple.jpg);") 
  
        #RED
        # creating a push button 
        red_btn = QPushButton("red", self) 
 
        # setting geometry of button 
        red_btn.setGeometry(300, 300, 100, 100) 
  
        # adding action to a button 
        red_btn.clicked.connect(self.clickme) 
  
        # setting image to the button 
        red_btn.setStyleSheet("background-image : url(red.jpg);") 
  
        #ORANGE
        # creating a push button 
        orange_btn = QPushButton("orange", self) 
 
        # setting geometry of button 
        orange_btn.setGeometry(200, 300, 100, 100) 
  
        # adding action to a button 
        orange_btn.clicked.connect(self.clickme) 
  
        # setting image to the button 
        orange_btn.setStyleSheet("background-image : url(orange.jpg);") 
 
        #GREY
        # creating a push button 
        grey_btn = QPushButton("grey", self) 

        # setting geometry of button 
        grey_btn.setGeometry(100, 300, 100, 100) 
  
        # adding action to a button 
        grey_btn.clicked.connect(self.clickme) 
  
        # setting image to the button 
        grey_btn.setStyleSheet("background-image : url(grey.jpg);") 
  

        # CHECK PASSWORD

        check_btn = QPushButton("Check my password", self)
        check_btn.setGeometry(150,450, 200,30)
        check_btn.clicked.connect(self.check)


 

    
    

    def showdialog():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(msgbtn)
	
        retval = msg.exec_()


  
    # action method 
    def check(self):
       
        valid = False

        pass_file = open("pass_file.txt","r")
        check_file = open("check.txt","r")
        Lines_pass = pass_file.readlines()
        Lines_check = check_file.readlines()

        if Lines_pass == Lines_check:
            print("correct")
            valid = True
        else:
            print("sad :(")

        os.remove("check.txt")
        if valid == True:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("WELCOME")
	
            retval = msg.exec_()

            self.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Wrong Password Try again")
	
            retval = msg.exec_()

            self.show()

    

    def clickme(self): 
        
        sender = self.sender()
        # printing pressed 
        print(sender.text() + " pressed") 
        pass_file = open("check.txt","a")
        pass_file.write(sender.text()+" pressed\n")
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 
