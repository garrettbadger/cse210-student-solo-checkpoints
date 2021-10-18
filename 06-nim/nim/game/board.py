import random
class Board:

    def __init__(self):
        self.piles = []
        self.rows = 0
        self._prepare()
        


    def _prepare(self):
        self.rows = random.randint(2, 5)
        for i in range(self.rows):
            stones = random.randint(1, 9)
            self.piles.append(stones)





    def apply(self, move):
        pile = move.get_pile()
        stones = move.get_stones()
        self.piles[pile] = self.piles[pile] - stones
        


    def to_string(self):
        
        text =  "\n~~~~~~~~~~~~~~~~~~~~"
        for pile, stones in enumerate(self.piles):
            text += (f"\n{pile}: " + "0 " *stones)
        text +=  "\n~~~~~~~~~~~~~~~~~~~~"
        return text

            


    def is_empty(self):
        empty = [0] * len(self.piles) 
        return self.piles == empty 





