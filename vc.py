from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtTest
from PIL import Image
import random
import numpy

import sys, os

class Okno(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Okno, self).__init__(*args,*kwargs)
        self.setWindowTitle("Visual Cryptography")
        
        titleText = QLabel()
        titleText.setText("VISUAL")
        titleText.setAlignment(Qt.AlignCenter)
        titleText.setFont(QFont('Comic Sans',50))
        titleText.setStyleSheet("QLabel {color : #cae8d5}")

        titleText2 = QLabel()
        titleText2.setText("ENCRYPT")
        titleText2.setAlignment(Qt.AlignCenter)
        titleText2.setFont(QFont('Comic Sans',50))
        titleText2.setStyleSheet("QLabel {color : #cae8d5}")

        self.subtitleText = QLabel()
        self.subtitleText.setText(" ")
        self.subtitleText.setAlignment(Qt.AlignCenter)
        self.subtitleText.setFont(QFont('Comic Sans',20))
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")

        self.infoButton = QPushButton()
        self.infoButton.setText("Info")
        self.infoButton.setFont(QFont('Comic Sans',12))
        self.infoButton.setStyleSheet("QPushButton {background : #3b6978}")
        self.infoButton.setStyleSheet("QPushButton {color : #cae8d5}")
        self.infoButton.clicked.connect(self.infoClicked)

        self.ImagePath = QLineEdit()
        self.ImagePath.setReadOnly(True)
        self.ImagePath.setText("")
        self.ImagePath.setAlignment(Qt.AlignCenter)
        self.ImagePath.setFont(QFont('Comic Sans',10))
        self.ImagePath.setStyleSheet("QLineEdit {color : #84a9ac}")

        self.imageFromFileButton = QFileDialog()
        self.imageFromFileButton.setNameFilter("Images (*.png *.jpg)")
        self.imageFromFileButton.hide()

        ImageButton = QPushButton()
        ImageButton.setText("Get File")
        ImageButton.setFont(QFont('Comic Sans',12))
        ImageButton.setStyleSheet("QPushButton {background : #3b6978}")
        ImageButton.setStyleSheet("QPushButton {color : #cae8d5}")
        ImageButton.clicked.connect(self.imageFileClicked)

        ImageLayout = QHBoxLayout()
        ImageLayout.addWidget(self.ImagePath)
        ImageLayoutW = QWidget()
        ImageLayoutW.setLayout(ImageLayout)

        encryptButton = QPushButton()
        encryptButton.setText("Encrypt")
        encryptButton.setFont(QFont('Comic Sans',12))
        encryptButton.setStyleSheet("QPushButton {background : #3b6978}")
        encryptButton.setStyleSheet("QPushButton {color : #cae8d5}")
        encryptButton.clicked.connect(self.encryptClicked)

        encryptLayout = QHBoxLayout()
        encryptLayout.addWidget(encryptButton)
        encryptLayout.addWidget(ImageButton)
        encryptLayoutW = QWidget()
        encryptLayoutW.setLayout(encryptLayout)

        self.Image1Path = QLineEdit()
        self.Image1Path.setReadOnly(True)
        self.Image1Path.setText("")
        self.Image1Path.setAlignment(Qt.AlignCenter)
        self.Image1Path.setFont(QFont('Comic Sans',10))
        self.Image1Path.setStyleSheet("QLineEdit {color : #84a9ac}")

        self.Image2Path = QLineEdit()
        self.Image2Path.setReadOnly(True)
        self.Image2Path.setText("")
        self.Image2Path.setAlignment(Qt.AlignCenter)
        self.Image2Path.setFont(QFont('Comic Sans',10))
        self.Image2Path.setStyleSheet("QLineEdit {color : #84a9ac}")

        ImageDecryptLayout = QHBoxLayout()
        ImageDecryptLayout.addWidget(self.Image1Path)
        ImageDecryptLayout.addWidget(self.Image2Path)
        ImageDecryptLayoutW = QWidget()
        ImageDecryptLayoutW.setLayout(ImageDecryptLayout)

        Image1Button = QPushButton()
        Image1Button.setText("Get File 1")
        Image1Button.setFont(QFont('Comic Sans',12))
        Image1Button.setStyleSheet("QPushButton {background : #3b6978}")
        Image1Button.setStyleSheet("QPushButton {color : #cae8d5}")
        Image1Button.clicked.connect(self.imageFile1Clicked)

        Image2Button = QPushButton()
        Image2Button.setText("Get File 2")
        Image2Button.setFont(QFont('Comic Sans',12))
        Image2Button.setStyleSheet("QPushButton {background : #3b6978}")
        Image2Button.setStyleSheet("QPushButton {color : #cae8d5}")
        Image2Button.clicked.connect(self.imageFile2Clicked)

        ImageButtons = QHBoxLayout()
        ImageButtons.addWidget(Image1Button)
        ImageButtons.addWidget(Image2Button)
        ImageButtonsW = QWidget()
        ImageButtonsW.setLayout(ImageButtons)

        decryptButton = QPushButton()
        decryptButton.setText("Decrypt")
        decryptButton.setFont(QFont('Comic Sans',12))
        decryptButton.setStyleSheet("QPushButton {background : #3b6978}")
        decryptButton.setStyleSheet("QPushButton {color : #cae8d5}")
        decryptButton.clicked.connect(self.decryptClicked)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(decryptButton)
        buttonsLayout.addWidget(self.infoButton)
        buttonsLayoutW = QWidget()
        buttonsLayoutW.setLayout(buttonsLayout)

        self.cleanButton = QRadioButton("Clean")
        self.noiseButton = QRadioButton("Noise")
        self.noiseButton.setChecked(True)

        chooseLayout = QHBoxLayout()
        chooseLayout.setAlignment(Qt.AlignHCenter)
        chooseLayout.addWidget(self.cleanButton)
        chooseLayout.addWidget(self.noiseButton)
        chooseLayoutW = QWidget()
        chooseLayoutW.setLayout(chooseLayout)

        self.squareButton = QRadioButton("Square")
        self.rectangleButton = QRadioButton("Rectangle")
        self.squareButton.setChecked(True)

        sizeLayout = QHBoxLayout()
        sizeLayout.setAlignment(Qt.AlignHCenter)
        sizeLayout.addWidget(self.squareButton)
        sizeLayout.addWidget(self.rectangleButton)
        sizeLayoutW = QWidget()
        sizeLayoutW.setLayout(sizeLayout)

        #Main Layout
        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(titleText)
        mainMenu.addWidget(titleText2)
        mainMenu.addWidget(self.subtitleText)
        mainMenu.addWidget(ImageLayoutW)
        mainMenu.addWidget(encryptLayoutW)
        mainMenu.addWidget(ImageDecryptLayoutW)
        mainMenu.addWidget(ImageButtonsW)
        mainMenu.addWidget(buttonsLayoutW)
        mainMenu.addWidget(chooseLayoutW)
        mainMenu.addWidget(sizeLayoutW)

        mainMenuW = QWidget()
        mainMenuW.setLayout(mainMenu)

        self.setCentralWidget(mainMenuW)
    
    def stateOfMode(self):
        if self.noiseButton.isChecked():
            return True
        else:
            return False
    
    def sizeMode(self):
        if self.squareButton.isChecked():
            return True
        else:
            return False
    
    def encryptClicked(self):
        if(self.sizeMode()):
            self.encryptSquareClicked()
        else:
            self.encryptRectangleClicked()
    
    def saveClicked(self):
        f = open("result.txt", "w",encoding="utf-8")
        f.write("Encrypted text: "+self.encryptedText.text())
        f.write("\nDecrypted text: "+self.decryptedText.text())
        f.write("\nKey: "+self.genKey())
        f.close()

    def infoClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Info")
        info.setStyleSheet("QMessageBox {background-color : #cae8d5}")
        f = open("info.txt", "r", encoding="utf-8")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier',12))
        info.exec_()

    def imageFileClicked(self):
        self.imageFromFileButton.show()
        if self.imageFromFileButton.exec():
            files = self.imageFromFileButton.selectedFiles()
            self.ImagePath.setText(files[0])
    
    def imageFile1Clicked(self):
        self.imageFromFileButton.show()
        if self.imageFromFileButton.exec():
            files = self.imageFromFileButton.selectedFiles()
            self.Image1Path.setText(files[0])

    def imageFile2Clicked(self):
        self.imageFromFileButton.show()
        if self.imageFromFileButton.exec():
            files = self.imageFromFileButton.selectedFiles()
            self.Image2Path.setText(files[0])
 
    def encryptSquareClicked(self):
        self.subtitleText.setText("Running")
        QtTest.QTest.qWait(10)
        imagePath = self.ImagePath.text()
        image = Image.open(imagePath)
        image = image.convert('1')
        out1 = Image.new('1', [size*2 for size in image.size])
        out2 = Image.new('1', [size*2 for size in image.size])

        for i in range(0, image.size[0], 1):
            for j in range(0, image.size[1], 1):
                pixel = image.getpixel((i,j))
                x = random.randint(0,1)
                if pixel == 0:
                    if x == 0:
                        out1.putpixel((i*2, j*2),255)
                        out1.putpixel((i*2+1, j*2), 0)
                        out1.putpixel((i*2, j*2+1), 255)
                        out1.putpixel((i*2+1, j*2+1), 0)

                        out2.putpixel((i * 2, j * 2), 0)
                        out2.putpixel((i * 2 + 1, j * 2), 255)
                        out2.putpixel((i * 2, j * 2 + 1), 0)
                        out2.putpixel((i * 2 + 1, j * 2 + 1), 255)
                    else:
                        out1.putpixel((i * 2, j * 2), 0)
                        out1.putpixel((i * 2 + 1, j * 2), 255)
                        out1.putpixel((i * 2, j * 2 + 1), 0)
                        out1.putpixel((i * 2 + 1, j * 2 + 1), 255)

                        out2.putpixel((i * 2, j * 2), 255)
                        out2.putpixel((i * 2 + 1, j * 2), 0)
                        out2.putpixel((i * 2, j * 2 + 1), 255)
                        out2.putpixel((i * 2 + 1, j * 2 + 1), 0)
                if pixel == 255:
                    if x == 0:
                        out1.putpixel((i * 2, j * 2), 255)
                        out1.putpixel((i * 2 + 1, j * 2), 0)
                        out1.putpixel((i * 2, j * 2 + 1), 255)
                        out1.putpixel((i * 2 + 1, j * 2 + 1), 0)

                        out2.putpixel((i * 2, j * 2), 255)
                        out2.putpixel((i * 2 + 1, j * 2), 0)
                        out2.putpixel((i * 2, j * 2 + 1), 255)
                        out2.putpixel((i * 2 + 1, j * 2 + 1), 0)
                    else:
                        out1.putpixel((i * 2, j * 2), 0)
                        out1.putpixel((i * 2 + 1, j * 2), 255)
                        out1.putpixel((i * 2, j * 2 + 1), 0)
                        out1.putpixel((i * 2 + 1, j * 2 + 1), 255)

                        out2.putpixel((i * 2, j * 2), 0)
                        out2.putpixel((i * 2 + 1, j * 2), 255)
                        out2.putpixel((i * 2, j * 2 + 1), 0)
                        out2.putpixel((i * 2 + 1, j * 2 + 1), 255)

        filename = QFileDialog.getSaveFileName(self, "Open Image File", os.path.abspath(os.getcwd()), "Images (*.png *.jpg)")
        if filename[0] != '':
            out1.save(filename[0])
            filename = QFileDialog.getSaveFileName(self, "Open Image File", os.path.abspath(os.getcwd()), "Images (*.png *.jpg)")
            if filename[0] != '':
                out2.save(filename[0])
                self.subtitleText.setStyleSheet('color: green')
                self.subtitleText.setText("ENCRYPT DONE")
                QtTest.QTest.qWait(2000)
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")
        self.subtitleText.setText("")
    
    def encryptRectangleClicked(self):
        self.subtitleText.setText("Running")
        QtTest.QTest.qWait(10)
        imagePath = self.ImagePath.text()
        image = Image.open(imagePath)
        image = image.convert('1')
        out1 = Image.new('1', [image.size[0]*2, image.size[1]])
        out2 = Image.new('1', [image.size[0]*2, image.size[1]])

        for i in range(0, image.size[0], 1):
            for j in range(0, image.size[1], 1):
                pixel = image.getpixel((i,j))
                x = random.randint(0,1)
                if pixel == 0: 
                    if x == 0:
                        out1.putpixel((i*2, j),255)
                        out1.putpixel((i*2+1, j), 0)

                        out2.putpixel((i * 2, j), 0)
                        out2.putpixel((i * 2 + 1, j), 255)
                    else:
                        out1.putpixel((i * 2, j), 0)
                        out1.putpixel((i * 2 + 1, j), 255)

                        out2.putpixel((i * 2, j), 255)
                        out2.putpixel((i * 2 + 1, j), 0)
                if pixel == 255: 
                    if x == 0:
                        out1.putpixel((i * 2, j), 255)
                        out1.putpixel((i * 2 + 1, j), 0)

                        out2.putpixel((i * 2, j), 255)
                        out2.putpixel((i * 2 + 1, j), 0)
                    else:
                        out1.putpixel((i * 2, j), 0)
                        out1.putpixel((i * 2 + 1, j), 255)

                        out2.putpixel((i * 2, j), 0)
                        out2.putpixel((i * 2 + 1, j), 255)

        filename = QFileDialog.getSaveFileName(self, "Open Image File", os.path.abspath(os.getcwd()), "Images (*.png *.jpg)")
        if filename[0] != '':
            out1.save(filename[0])
            filename = QFileDialog.getSaveFileName(self, "Open Image File", os.path.abspath(os.getcwd()), "Images (*.png *.jpg)")
            if filename[0] != '':
                out2.save(filename[0])
                self.subtitleText.setStyleSheet('color: green')
                self.subtitleText.setText("ENCRYPT DONE")
                QtTest.QTest.qWait(2000)
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")
        self.subtitleText.setText("")

    def decryptClicked(self):
        self.subtitleText.setText("Running")
        QtTest.QTest.qWait(10)

        inPath1 = self.Image1Path.text()
        in1 = Image.open(inPath1)
        inPath2 = self.Image2Path.text()
        in2 = Image.open(inPath2)

        if(self.stateOfMode()):
            image = self.noise(in1, in2)
        else:
            image = self.clean(in1, in2)

        filename = QFileDialog.getSaveFileName(self, "Open Image File", os.path.abspath(os.getcwd()), "Images (*.png *.jpg)")
        if filename[0] != '':
            image.save(filename[0])

            self.subtitleText.setStyleSheet('color: green')
            self.subtitleText.setText("DECRYPT DONE")
            QtTest.QTest.qWait(2000)
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")
        self.subtitleText.setText("")
    
    def noise(self, in1, in2):
        image = Image.new('1', [size for size in in1.size])
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                image.putpixel((x, y), min(in1.getpixel((x, y)), in2.getpixel((x, y))))
        return image

    def clean(self, in1, in2):
        image = Image.new('1', [int(size/2) for size in in1.size])
        for x in range(0, in1.size[0]-1, 2):
            for y in range(0, in1.size[1]-1, 2):
                if in1.getpixel((x, y)) == in2.getpixel((x, y)):
                    image.putpixel((int(x/2), int(y/2)),255)
                else:
                    image.putpixel((int(x/2), int(y/2)),0)
        return image

#MAIN
app = QApplication(sys.argv)
window = Okno()
window.setFixedSize(650,500)
window.setStyleSheet("background-color: #204051")
window.show()

app.exec_()