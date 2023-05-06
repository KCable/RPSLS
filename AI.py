from Player import Player
from random import choice

class AI(Player):
    
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.current_gesture = choice(self.gesture_list)
        pass
        
        print(f"{self.name} chose {self.current_gesture}!")