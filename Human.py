from Player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0
        
    pass

