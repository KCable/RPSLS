import random
from time import sleep


    
class Player:
        
    def __init__(self, name):
        self.name:str = name
        self.score:int = 0
        self.gesture_list:list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.current_gesture:str = ""

    
    def choose_gesture(self): 
        #children do what you want with this action!
        pass


