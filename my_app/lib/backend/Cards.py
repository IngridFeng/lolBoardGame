import random

import Constants

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

class Cards:
  def __init__(self):
      self.deck = list(range(1, 53))
      self.shuffle()
  
  def getOneCard(self):
      if not self.deck:
          raise ValueError("Cards deck is empty!")
      card = self.deck.pop()
      color = Constants.Colors(card // 4)
      number = card % 4
      return Card(color, number)
  
  def getTwoCards(self):
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
