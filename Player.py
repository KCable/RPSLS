import random
from Gestures import Rock, Paper, Scissors, Lizard, Spock

    
class Player:
        
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gesture_list = [
            Rock(), 
            Paper(), 
            Scissors(), 
            Lizard(), 
            Spock()
        ]
        self.current_gesture = Rock()
        pass

    
    def choose_gesture(self): 
        #children do what you want with this action!
        pass


