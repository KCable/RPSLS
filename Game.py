from Player import Player
from Human import Human
from AI import AI
from time import sleep
import random


class Game:

    def __init__(self, name):
        self.name = name
        
    pass

    def run_game(self):
        self.display_rules
        self.choose_gesture
        self.display_winner
    pass

    def display_rules(self):
        print("Games Rules\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock\nSpock Smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock ")

    pass
    def choose_gesture(self, gesture_list):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

        "Rock"[0] > "Scissors"[2]
        "Scissors"[2] > "Paper"[1]
        "Paper"[1] > "Rock"[0]
        "Rock"[0] > "Lizard"[3]
        "Lizard"[3] > "Spock"[4]
        "Spock"[4] > "Scissors"[2]
        "Scissors"[2] > "Lizard"[3]
        "Lizard"[3] > "Paper"[1]
        "Paper"[1] > "Spock"[4]
        "Spock"[4] > "Rock"[0] 

    
if [0] > [2]:
    print("Rock crushes Scissors")
elif [2] > [1]:
    print("Scissors cuts Paper")
elif [1] > [0]:
    print("Paper covers Rock")
elif [0] > [3]:
    print("Rock crushes Lizard")
elif [3] > [4]:
    print("Lizard poisons Spock")
elif [4] > [2]:
    print("Spock Smashes Scissors")
elif [2] > [3]:
    print("Scissors decapitates Lizard")
elif [3] > [1]:
    print("Lizard eats Paper")
elif [1]> [4]:
    print("Paper disproves Spock")
elif [4] > [0]:
    print("Spock vaporizes Rock")
    

            
        
    


    def display_winner(self):
        print(f"The winner is ")
    pass



