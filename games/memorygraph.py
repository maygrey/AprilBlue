'''
Created on 14/11/2014

@author: rpe
'''
# Import the core and GUI elements of Qt
from PySide.QtCore import *
from PySide.QtGui import *

class MemoryMainWindow(QWidget):
    '''
    Graphic interface done with QT. Main window.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        QWidget.__init__(self)
        self.setMinimumSize(QSize(800, 300))
        self.setWindowTitle('Memory Game')
        self.label = QLabel('Select two cards',self)
        self.button = QPushButton('reset', self)
        
    def run(self):
        self.show()
        
class MemoryCard(QWidget):
    '''
    Graphic interface done with QT. Card
    '''
    def __init__(self):
        '''
        Constructor
        '''
        QWidget.__init__(self)
        self.setMinimumSize(QSize(100, 150))
        self.button = QPushButton('*', self)
        
    def run(self):
        self.show()


        