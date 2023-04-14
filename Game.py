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
        self.display_rules()
        self.player_count("Player_list", "player_count")
        self.Player_list()
        self.choose_gesture()
        self.display_winner()
        

    def display_rules(self):
        print("Games Rules\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock\nSpock Smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock \n ")
       
    def Player_list(self, player_count, Player_list):
        self.Player_list = Player_list
        self.player_count = player_count
        pass
        
    def player_count(self, Player_list, player_count):
        self.player_count = input("How many players?:\n1 or 2 ")
        self.Player_list = ["Human", "AI"]
        if (player_count) <= 2:
            while True:
                if player_count == 1:
                    Player_list = [0]
                if player_count == 2:
                    Player_list = [1]            
                if player_count >= 2:
                    input("What is your name?" )
                    Player_list[0] = input 
                else:
                    print("There must be at least one player")
        else:
            input("Please select 1 or 2: ")
        pass            
       

    def choose_gesture(self):
        self.gesture = str(random.randint(0,4))
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        sleep(1)
        print(f"{self.player_count} has chosen {self.gesture_list[int(self.gesture)]}")  
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

                
            pass

    
    def display_winner(self, Player_list):
        self.Player_list = Player_list
        print(f"The winner is {Player_list.name}!")
        pass



               

