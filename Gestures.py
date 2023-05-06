# Parent Class

class Gesture:
    def __init__(self, name, w1, w2, l1, l2):
        self.name = name
        self.wins = [w1, w2]
        self.losses = [l1, l2]
        pass

    def compare(self, owner, opponent):
        if opponent.current_gesture.name == self.name:
            print("It's a tie!")
        elif opponent.current_gesture.name in self.wins:
            owner.score += 1

        elif opponent.current_gesture.name in self.losses:
            opponent.score += 1
        pass

class Rock(Gesture):
    def __init__(self):
        super().__init__("Rock", "Scissors", "Lizard", "Spock", "Paper")

class Paper(Gesture):
    def __init__(self):
        super().__init__("Paper", "Spock", "Rock", "Scissors", "Lizard")

class Scissors(Gesture):
    def __init__(self):
        super().__init__("Scissors", "Lizard", "Paper", "Spock", "Rock")        

class Lizard(Gesture):
    def __init__(self):
        super().__init__( "Lizard", "Spock", "Paper", "Scissors", "Rock")        

class Spock(Gesture):
    def __init__(self):
        super().__init__( "Spock", "Scissors", "Rock", "Lizard", "Paper")        

