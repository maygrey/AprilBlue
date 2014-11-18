'''
Created on 18/11/2014

@author: rpe
'''

class MemoryCard():
    '''
    A card to play memory
    '''
    def __init__(self, state, value):
        self.state = state
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
    def flip(self):
        self.state = not(self.state)