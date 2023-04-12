import random
from time import sleep

class Player:

    def __init__(self, name):
        self.name = name
        
    pass

    def choose_gesture(self):
        self.gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        sleep(1)
        print(f"{self.name} has chosen {gesture_list[int(self.gesture)]}")

    pass


    def choose_gesture(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

        if "Rock"[0] >= "Scissors"[2]:
            print("Rock crushes Scissors")
        if "Scissors"[2] >= "Paper"[1]:
            print("Scissors cuts Paper")
        if "Paper"[1] >= "Rock"[0]:
            print("Paper covers Rock")
        if  "Rock"[0] >= "Lizard"[3]:
            print("Rock crushes Lizard")
        if  "Lizard"[3] >= "Spock"[4]:
            print("Lizard poisons Spock")
        if "Spock"[4] >= "Scissors"[2]:
            print("Spock Smashes Scissors")
        if "Scissors"[2] >= "Lizard"[3]:
            print("Scissors decapitates Lizard") 
        if "Lizard"[3] >= "Paper"[1]:
            print("Lizard eats Paper") 
        if "Paper"[1] >= "Spock"[4]:
            print("Paper disproves Spock") 
        if "Spock"[4] >= "Rock"[0]:
            print("Spock vaporizes Rock") 

   

