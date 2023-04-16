from Player import Player
from Human import Human
from AI import AI
from time import sleep
import random
from Action import Action

class Game:

    def __init__(self, name):
        self.name = name
                
        pass

    def run_game(self):
        self.display_rules()
        self.player_count("Player_list", "selected_player")
        self.choose_gesture()
        self.determine_winner
        self.display_winner("player")
        

    def display_rules(self):
        print("Games Rules\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock\nSpock Smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock \n ")
       
    def player_count(self, Player_list, selected_player):
        selected_player = int(input("How many players?:\n1, 2 or 3 "))
        self.Player_list = ["AI", "Player_one", "Player_two"]
        if (selected_player) == 2 or (selected_player) == 3:
            while True:
                if selected_player == 1:
                    Player_list = ["AI"]
                    break
                if selected_player == 2:
                    Player_list = str["Human"] 
                    break  
                if selected_player == 3:
                    Player_list = str["Human"]
                else:
                    print("There must be at least one player")
        else:
            input("Please select 1 or 2: ")
                    
       

    def choose_gesture(self):
        self.gesture = str(random.randint(0,4))
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        sleep(1)
        chosen_gesture = self.gesture_list[int(self.gesture)]
        print(f"AI chose {chosen_gesture}")  
        self.gesture = str(random.randint(0,4))
        chosen_gesture = self.gesture_list[int(self.gesture)]
        print(f"Player one chose {chosen_gesture}")
        self.gesture = str(random.randint(0,4))
        chosen_gesture = self.gesture_list[int(self.gesture)]
        print(f"Player two chose {chosen_gesture}")


    def determine_winner(choose_gesture, computer_action):
        victories = {
            Action.Scissors: [Action.Lizard, Action.Paper],
            Action.Paper: [Action.Spock, Action.Rock],
            Action.Rock: [Action.Lizard, Action.Scissors],
            Action.Lizard: [Action.Spock, Action.Paper],
            Action.Spock: [Action.Scissors, Action.Rock]
        }

        defeats = victories[choose_gesture]
        if choose_gesture == computer_action:
            print(f"Both players selected {choose_gesture.name}. It's a tie!")
        elif computer_action in defeats:
            print(f"{choose_gesture.name} beats {computer_action.name}! You win!")
        else:
            print(f"{computer_action.name} beats {choose_gesture.name}! You lose.")
        


    def display_winner(self, player):
        print(f"The winner is {player.name}!")
        pass



               

