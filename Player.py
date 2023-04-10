import random
from time import sleep

class Player:

    def __init__(self, name):
        self.name = name
        
    pass

    def choose_gesture(self):
            self.chosen_gesture = str(random.randint(0,4))
            gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
            sleep(1)
            print(f"{self.name} has picked {gesture_list [int(self.choose_gesture)]}")

    pass