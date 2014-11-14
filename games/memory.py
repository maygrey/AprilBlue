'''
Memory Game
Created on 12/11/2014

@author: maygrey
'''

import sys
import random
# Import the core and GUI elements of Qt
from PySide.QtCore import *
from PySide.QtGui import *

DECK = range(0,8) + range(0,8)
EXPOSED = []
STATE = 0
PAIR =[]

#helper function to initialize globals
def new_game():
    global STATE
    random.shuffle(DECK)
    STATE = 0
    for i in range(16):
        EXPOSED.append(False)
    
#define event handlers
def mouseclick(pos):
    """
    Game logic: 
    pos is a tuple with the x and y of a position
    pair is the ith (index) of the flipped cards
    State 0, initial, no cards flipped. State 1: 1 card flipped. State 2: 2 cards flipped
    EXPOSED is the list of card states True/False flipped
    When STATE changes from 1 to 2 the game logic compares both cards
    """
    intpos = int(pos[1]/100)
    global STATE
    if STATE == 0:
        STATE = 1
        if (pos[1] < 150):
            EXPOSED[intpos] = True
        else:
            EXPOSED[intpos + 8] = True
    elif STATE == 1:
        STATE = 2
        if (pos[1] < 150):
            if (EXPOSED[intpos] != True):
                EXPOSED[intpos] = True
        else:
            if (EXPOSED[intpos + 8] != True):
                EXPOSED[intpos + 8] = True
        for i in range(16):
            if (EXPOSED[i] == True):
                PAIR.append(i)
        #if not the same back them to unexposed
        if (len(PAIR)> 1):
            if(DECK[PAIR[0]] != DECK[PAIR[1]]):
                EXPOSED[PAIR[0]] = False
                EXPOSED[PAIR[1]] = False

    else:
        #TODO
        STATE = 1

    pass

def draw(canvas):
    pass

if __name__ == '__main__':
    
    qt_app = QApplication(sys.argv)

    widget = QWidget()
    widget.setWindowTitle('Memory Game')
    label = QLabel('Select two cards',widget)
    widget.setMinimumSize(QSize(800, 300))
    button = QPushButton('reset', widget)
    button.show()
    label.show() 
    widget.show()

    print(DECK)
    new_game()
    print(DECK)
    position = (530,120)
    mouseclick(position)
    position = (530,120)
    mouseclick(position)
    # Run the application's event loop
    qt_app.exec_()

    pass