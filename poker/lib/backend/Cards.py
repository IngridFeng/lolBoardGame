import random
from functools import total_ordering

import Constants

@total_ordering
class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    def __eq__(self, other):
        return self.number == other.number 

    def __ne__(self, other):
        return self.number != other.number 

    def __lt__(self, other):
        selfNum = 14 if self.number.value == 1 else self.number.value
        otherNum = 14 if other.number.value == 1 else other.number.value
        return self.number.value > other.number.value
    
    def __repr__(self):
        return "%s %s" % (self.color.name, self.number.name)
    
    def getColor(self):
        return self.color
    
    def getNumber(self):
        return self.number

class Cards:
    def __init__(self):
      self.deck = list(range(52))
      self.shuffle()
  
    def getOneCard(self):
        if not self.deck:
            raise ValueError("Cards deck is empty!")
        card = self.deck.pop()
        color = Constants.Colors(card // 13 + 1)
        number = Constant.Colors(card % 13 + 1)
        return Card(color, number)
    
    def getPlayerCards(self):
        return [self.getOneCard() for _ in range(2)]

    def getFlopCards(self):
        self.getOneCard()
        return [self.getOneCard() for _ in range(3)]
    
    def getTurnCard(self):
        self.getOneCard()
        return [self.getOneCard() for _ in range(1)]
    
    def getRiverCard(self):
        self.getOneCard()
        return [self.getOneCard() for _ in range(1)]
    
    def shuffle(self):
        self.deck = random.shuffle(self.deck)
