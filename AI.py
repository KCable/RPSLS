from Player import Player
from random import choice

class AI(Player):
    
    def __init__(self, name):
        super().__init__(name)
        pass

    def choose_gesture(self):
        self.current_gesture = choice(self.gesture_list)     
        print(f"{self.name} chose {self.current_gesture.name}!")
        pass