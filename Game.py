from Player import Player
from Human import Human
from AI import AI
import time
from random import choice
from random import choices
# from Action import Action
import os
from time import sleep
import random
import sys


class Game:

    def __init__(self, name):
        self.name = name  
        
        pass

    def run_game(self):
        self.display_rules()
        self.player_count('player_list', 'selected_player')
        # self.set_name("")
        self.play_game()
        

    def display_rules(self):
        print("Games Rules:\n \nRock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock Smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock \n")
    
   
    def player_count(self, Player_list, selected_player):
        selected_player = int(input("How many players?:\n1 or 2 "))
        Player_list = ["AI", "player"]
        if (selected_player) == 1:
            while True:
                if selected_player == 0:
                    Player_list = ["AI"]
                    break
                if selected_player == 1:
                    Player_list = input("Player's name:\n ")
                    break  
                                   
                           
                # if selected_player == 2:
                #     Player_list = ["player_one","player_two"]
                #     break
                # if selected_player == 1:
                #     Player_list = input("Player's name:\n ")
                #     break       
                # # self.name = input("Creating second human player \n")
                # self.player_two[2] = input("")
        pass
    
    # def set_name(self, player):
    #         self.name = input(player)
        

    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    cls() 
    
    sleep(1)

    print("Let's play!")

    
    def play_game(self):        
        options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

        while True:
            try:
                turns = int(input("Best out of (3 or 5): "))
                if turns == 3 or turns == 5:
                    break
                continue
            except ValueError:
                print("Invalid choice.")

        necessary_wins = int(turns/2) + 1

        player_wins = 0
        computer_wins = 0

        while True:

            while True:
                player = input(">>> rock, paper, scissors, lizard, spock: ")
                if player in options:
                    break

            computer = random.choice(options)

            if player == computer:
                print('It is a tie')    
            elif player == 'rock' and computer == 'scissors':
                print('You win, rock crushes scissors')
                player_wins += 1
            elif player == 'rock' and computer == 'lizard':
                print('You win, rock crushes lizard')
                player_wins += 1
            elif player == 'rock' and computer == 'paper':
                print('Computer wins, paper covers rock')
                computer_wins += 1
            elif player == 'rock' and computer == 'spock':
                print('Computer wins, Spock vaporizes rock')
                computer_wins += 1
            elif player == 'paper' and computer == 'rock':
                print('You win, paper covers rock')
                player_wins += 1
            elif player == 'paper' and computer == 'spock':
                print('You win, paper disproves Spock')
                player_wins += 1
            elif player == 'paper' and computer == 'scissors':
                print('Computer wins, scissors cut paper')
                computer_wins += 1
            elif player == 'paper' and computer == 'lizard':
                print('Computer wins, lizard eats paper')
                computer_wins += 1
            elif player == 'scissors' and computer == 'paper':
                print('You win, scissors cut paper')
                player_wins += 1
            elif player == 'scissors' and computer == 'lizard':
                print('You win, scissors decapitates lizard')
                player_wins += 1
            elif player == 'scissors' and computer == 'rock':
                print('Computer wins, rock crushes scissors')
                computer_wins += 1
            elif player == 'scissors' and computer == 'spock':
                print('Computer wins, Spock smashes scissors')
                computer_wins += 1
            elif player == 'lizard' and computer == 'paper':
                print('You win, lizard eats paper')
                player_wins += 1
            elif player == 'lizard' and computer == 'spock':
                print('You win, lizard poisons Spock')
                player_wins += 1
            elif player == 'lizard' and computer == 'rock':    
                print('Computer wins, Spock smashes scissors')
                computer_wins += 1
            elif player == 'lizard' and computer == 'scissors':
                print('Computer wins, scissors decapitate lizard')
                computer_wins += 1
            elif player == 'spock' and computer == 'scissors':
                print('You win, Spock smashes scissors')
                player_wins += 1
            elif player == 'spock' and computer == 'rock':
                print('You win, Spock vaporizes rock')
                player_wins += 1
            elif player == 'spock' and computer == 'paper':
                print('Computer wins, paper disproves Spock')
                computer_wins += 1
            elif player == 'spock' and computer == 'lizard':
                print('Computer wins, lizard poisons Spock')
                computer_wins += 1

            if player_wins == necessary_wins or computer_wins == necessary_wins:
                sleep(3)
                break

        if player_wins > computer_wins:
            print(f'>>> You win! <<<')

        else:
            print(f'>>> Computer wins! <<<')

        print(f'>>> You scored: {player_wins} point(s) \n\nThanks for playing! \n\n<<<')

        sleep(3)
            




               

