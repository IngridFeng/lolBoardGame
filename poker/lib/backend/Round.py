from itertools import combinations

import Cards
import Constants
import Hands
import Player

class Round:
    def __init__(self, players):
        self.cards = Cards()
        self.players = players
        self.flopCards = None
        self.turnCard = None
        self.riverCard = None
        self.pot = 0

    def playerAction(self, username, action, money=0):
        if action == Constants.PlayerAction.FOLD:
            self.players.pop(username)
        elif action == Constants.PlayerAction.CHECK:
            pass
        elif action == Constants.PlayerAction.CALL:
            self.players[username].actionCall(money)
            self.pot += money
        elif action == Constants.PlayerAction.RAISE:
            self.players[username].actionRaise(money)
            self.pot += money
    
    def distributePlayerCards(self):
        for username, player in enumerate(self.players):
            player.setPlayerCards(self.cards.getPlayerCards())
    
    def flop(self):
        self.flopCards = self.cards.getFlopCards()
    
    def turn(self):
        self.turnCard = self.cards.getTurnCard()
    
    def river(self):
        self.riverCard = self.cards.getRiverCard()
    
    def getWinner(self):
        for player in self.players():
            highestSoFar = None
            allHands = player.getPlayerCards() + self.flopCards + self.turnCard + self.riverCard
            for hands in combinations(all_hands, 5):
                hands = Hands(list(hands))
                if not highestSoFar:
                    highestSoFar = hands
                elif hands > highestSoFar:
                    highestSoFar = hands
            player.setHighHands(highestSoFar)
        rank = sorted(self.players, key=lambds p: p.getHighHands(), reversed=True)
        winnerName = rank[0].getUsername()
        rank[0].actionWin(self.pot)
        return winnerName
