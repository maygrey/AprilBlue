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

#helper function to initialize globals
def new_game():
    random.shuffle(DECK)
    for i in range(8):
        EXPOSED.append(False)
    print EXPOSED
    
#define event handlers
def maouseclick(pos):
    """Game logic"""
    
    pass

def draw(canvas):
    pass

if __name__ == '__main__':
    
    qt_app = QApplication(sys.argv)

    widget = QWidget()
    widget.setWindowTitle('Memory Game')
    label = QLabel('Select two cards',widget)
    widget.setMinimumSize(QSize(800, 600))
    button = QPushButton('reset', widget)
    button.show()
    label.show()
    widget.show()
    """
    # create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# Always remember to review the grading rubric"""
    print(DECK)
    new_game()
    print(DECK)
    # Run the application's event loop
    qt_app.exec_()

    pass