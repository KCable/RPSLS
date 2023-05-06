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
        self.compare_gestures()
        winner = self.winner_check()
        self.victory_message(self.winner_check())
    
   
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


    def display_rules(self):
        print("""
        Games Rules:

        Rock crushes Scissors
        Scissors cuts Paper
        Paper covers Rock
        Rock crushes Lizard
        Lizard poisons Spock
        Spock Smashes Scissors
        Scissors decapitates Lizard
        Lizard eats Paper
        Paper disproves Spock
        Spock vaporizes Rock 

        """)
        pass


    def player_rolls(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        self.compare_gestures()
        pass

    
    def winner_check(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.player_rolls()
        if self.player_one.score >= 3:
            return self.player_one
        return self.player_two
        pass


    def compare_gestures(self):    

        if self.player_one.current_gesture == self.player_two.current_gesture:
            print('It is a tie')  

        elif self.player_one.current_gesture == self.player_one.gesture_list[0]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[2]): 
                print('Player 1 wins, rock crushes scissors')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[0]: 
            if (self.player_two.current_gesture == self.player_one.gesture_list[3]):
                print('Player 1 wins, rock crushes lizard')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[0]: 
            if (self.player_two.current_gesture == self.player_one.gesture_list[1]):
                print('Player 2 wins, paper covers rock')
            self.player_two.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[4]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[0]): 
                print('Player 2 wins, Spock vaporizes rock')
            self.player_two.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[1]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[0]):
                print('Player 1 wins, paper covers rock')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[1]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[5]):
                print('Player 1 wins, paper disproves Spock')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[1]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[2]):            
                print('Player 2 wins, scissors cut paper')
            self.player_two.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[1]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[4]):
                print('Player 2 wins, lizard eats paper')
            self.player_two.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[2]:
            if (self.player_two.current_gesture == self.player_two.gesture_list[1]):
                print('Player 1 wins, scissors cut paper')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[2]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[3]):
                print('Player 1 wins, scissors decapitates lizard')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[2]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[0]):
                print('Player 2 wins, rock crushes scissors')
            self.player_two.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[2]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[5]):
                print('Player 2 wins, Spock smashes scissors')
            self.player_two.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[3]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[1]):
                print('Player 1 wins, lizard eats paper')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[3]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[5]):
                print('Player 1 wins, lizard poisons Spock')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[3]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[0]):
                print('Player 2 wins, Spock smashes scissors')
            self.player_two.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[3]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[2]):
                print('Player 2 wins, scissors decapitate lizard')
            self.player_two.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[4]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[2]):
                print('Player 1 wins, Spock smashes scissors')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[4]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[0]):
                print('Player 1 wins, Spock vaporizes rock')
            self.player_one.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[4]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[1]):
                print('Player 2 wins, paper disproves Spock')
            self.player_two.score += 1
        elif self.player_one.current_gesture == self.player_one.gesture_list[4]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[3]):
                print('Player 2 wins, lizard poisons Spock')
            self.player_two.score += 1

             
    def victory_message(self, obj):
        print(f"{obj.name} is the winner! \nThanks for Playing!")
        pass
            



               

