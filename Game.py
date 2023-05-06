from Player import Player
from Human import Human
from AI import AI
import interface as ui
import random


class Game:

    def __init__(self):
        self.player_one:Player("test")  
        self.player_two:Player("test") 
        pass

    def run_game(self): 
        self.game_type()
        self.display_rules()
        self.player_rolls()
        self.winner_check()
        self.winner_check()
        

    def display_rules():
        print("Games Rules:\n \nRock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock Smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock \n")
    
   
    def game_type(self):
        user_selection = ui.validate_to_int("""
        Please select from the options below:
        Press 1 for Human vs Human
        Press 2 for Human vs AI
        Press 3 for AI vs AI
        """)
           
        if user_selection == 1:
            self.player_one = Human("Player 1")
            self.player_two = Human("Player 2") 
        elif user_selection == 2:
            self.player_one = Human("Player 1")
            self.player_two = AI("Player 2")
        elif user_selection == 3:
            self.player_one = AI("Player 1")
            self.player_two = AI("Player 2") 
            pass
        
    def player_rolls(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        pass


    
    def winner_check(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.player_rolls()
            pass

    def victory_message(self):
        pass
            

    # def play_game(self):        
    #     options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    #     while True:
    #         try:
    #             turns = int(input("Best out of (3 or 5): "))
    #             if turns == 3 or turns == 5:
    #                 break
    #             continue
    #         except ValueError:
    #             print("Invalid choice.")

    #     necessary_wins = int(turns/2) + 1

    #     player_wins = 0
    #     computer_wins = 0

    #     while True:

    #         while True:
    #             player = input(">>> rock, paper, scissors, lizard, spock: ")
    #             if player in options:
    #                 break

    #         computer = random.choice(options)

    #         if player == computer:
    #             print('It is a tie')    
    #         elif player == 'rock' and computer == 'scissors':
    #             print('You win, rock crushes scissors')
    #             player_wins += 1
    #         elif player == 'rock' and computer == 'lizard':
    #             print('You win, rock crushes lizard')
    #             player_wins += 1
    #         elif player == 'rock' and computer == 'paper':
    #             print('Computer wins, paper covers rock')
    #             computer_wins += 1
    #         elif player == 'rock' and computer == 'spock':
    #             print('Computer wins, Spock vaporizes rock')
    #             computer_wins += 1
    #         elif player == 'paper' and computer == 'rock':
    #             print('You win, paper covers rock')
    #             player_wins += 1
    #         elif player == 'paper' and computer == 'spock':
    #             print('You win, paper disproves Spock')
    #             player_wins += 1
    #         elif player == 'paper' and computer == 'scissors':
    #             print('Computer wins, scissors cut paper')
    #             computer_wins += 1
    #         elif player == 'paper' and computer == 'lizard':
    #             print('Computer wins, lizard eats paper')
    #             computer_wins += 1
    #         elif player == 'scissors' and computer == 'paper':
    #             print('You win, scissors cut paper')
    #             player_wins += 1
    #         elif player == 'scissors' and computer == 'lizard':
    #             print('You win, scissors decapitates lizard')
    #             player_wins += 1
    #         elif player == 'scissors' and computer == 'rock':
    #             print('Computer wins, rock crushes scissors')
    #             computer_wins += 1
    #         elif player == 'scissors' and computer == 'spock':
    #             print('Computer wins, Spock smashes scissors')
    #             computer_wins += 1
    #         elif player == 'lizard' and computer == 'paper':
    #             print('You win, lizard eats paper')
    #             player_wins += 1
    #         elif player == 'lizard' and computer == 'spock':
    #             print('You win, lizard poisons Spock')
    #             player_wins += 1
    #         elif player == 'lizard' and computer == 'rock':    
    #             print('Computer wins, Spock smashes scissors')
    #             computer_wins += 1
    #         elif player == 'lizard' and computer == 'scissors':
    #             print('Computer wins, scissors decapitate lizard')
    #             computer_wins += 1
    #         elif player == 'spock' and computer == 'scissors':
    #             print('You win, Spock smashes scissors')
    #             player_wins += 1
    #         elif player == 'spock' and computer == 'rock':
    #             print('You win, Spock vaporizes rock')
    #             player_wins += 1
    #         elif player == 'spock' and computer == 'paper':
    #             print('Computer wins, paper disproves Spock')
    #             computer_wins += 1
    #         elif player == 'spock' and computer == 'lizard':
    #             print('Computer wins, lizard poisons Spock')
    #             computer_wins += 1

    #         if player_wins == necessary_wins or computer_wins == necessary_wins:
    #             sleep(3)
    #             break

    #     if player_wins > computer_wins:
    #         print(f'>>> You win! <<<')

    #     else:
    #         print(f'>>> Computer wins! <<<')

    #     print(f'>>> You scored: {player_wins} point(s) \n\nThanks for playing! \n\n<<<')





               

