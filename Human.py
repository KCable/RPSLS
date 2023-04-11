from Player import Player
import random
from time import sleep

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = Human
        self.score = 0
        
    pass

    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        sleep(1)
        print(f"{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}")

    pass