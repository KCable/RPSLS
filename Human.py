from Player import Player
import interface as ui

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass


    def choose_gesture(self):
        user_selection = ui.validate_to_int(f"""
        {self.name}, please select from the options below:
        Press 1 for {self.gesture_list[0].name}
        Press 2 for {self.gesture_list[1].name}
        Press 3 for {self.gesture_list[2].name}
        Press 4 for {self.gesture_list[3].name}
        Press 5 for {self.gesture_list[4].name}
        """)
        self.current_gesture = self.gesture_list[user_selection-1]           
        print(f"{self.name} chose {self.current_gesture.name}!")
        pass


