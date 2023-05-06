from Player import Player
from Human import Human
from AI import AI
import interface as ui
import random


class Game:

    def __init__(self):
        self.player_one:Player()  
        self.player_two:Player() 
        pass

    def run_game(self): 
        self.game_type()
        self.display_rules()
        self.player_rolls()
        # self.compare_gestures()
        self.winner_check()
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
        self.player_one.current_gesture.compare(self.player_one, self.player_two)
        pass

    
    def winner_check(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            print(f"{self.player_one.name}'s score is {self.player_one.score}")
            print(f"{self.player_two.name}'s score is {self.player_two.score}")
            self.player_rolls()
        if self.player_one.score >= 3:
            return self.player_one
        return self.player_two
        pass


    # def compare_gestures(self):    

        if self.player_one.current_gesture == self.player_two.current_gesture:
            print('It is a tie')  

        elif self.player_one.current_gesture == self.player_one.gesture_list[0]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[2]): 
                print('Player 1 wins, Rock crushes Scissors')
            
            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[0]: 
            if (self.player_two.current_gesture == self.player_one.gesture_list[3]):
                print('Player 1 wins, Rock crushes Lizard')
            
            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[0]: 
            if (self.player_two.current_gesture == self.player_one.gesture_list[1]):
                print('Player 2 wins, Paper covers Rock')
            
            self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[0]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[4]): 
                print('Player 2 wins, Spock vaporizes rock')
                
            self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[1]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[0]):
                print('Player 1 wins, Paper covers Rock')

            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[1]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[5]):
                print('Player 1 wins, Paper disproves Spock')

            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[1]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[2]):            
                print('Player 2 wins, Scissors cut Paper')

            self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[1]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[4]):
                print('Player 2 wins, Lizard eats Paper')

            self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[2]:
            if (self.player_two.current_gesture == self.player_two.gesture_list[1]):
                print('Player 1 wins, Scissors cut Paper')

            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[2]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[3]):
                print('Player 1 wins, Scissors decapitates Lizard')

            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[2]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[0]):
                print('Player 2 wins, Rock crushes Scissors')

            self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[2]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[4]):
                print('Player 2 wins, Spock smashes Scissors')

            self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[3]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[1]):
                print('Player 1 wins, Lizard eats Paper')
               
            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[3]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[4]):
                print('Player 1 wins, Lizard poisons Spock')

            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[3]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[0]):
                print('Player 2 wins, Rock crushes Lizard')

            self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[3]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[2]):
                print('Player 2 wins, Scissors decapitate Lizard')

            self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[4]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[2]):
                print('Player 1 wins, Spock smashes Scissors')

            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[4]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[0]):
                print('Player 1 wins, Spock vaporizes Rock')

            self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[4]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[1]):
                print('Player 2 wins, Paper disproves Spock')

            self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gesture_list[4]:
            if (self.player_two.current_gesture == self.player_one.gesture_list[3]):
                print('Player 2 wins, Lizard poisons Spock')

            self.player_two.score += 1

             
    def victory_message(self, obj):
        print(f"\n{obj.name} is the winner!\n \nThanks for Playing!\n  \n ")
        pass
            



               

