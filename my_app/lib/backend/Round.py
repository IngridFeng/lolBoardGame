class Round:
    def __init__(self, players):
        self.cards = Cards()
        self.players = players
        self.pot = 0
    
    def distributePlayerCards(self):
        for username, player in enumerate(self.players):
            player.addHands(self.cards.getTwoCards())

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
    
    def getWinner(self):
        # TODO: CompareHandsLogic
        winnerName = self.players.keys[0]
        self.players[winnerName] += pot
        return winnerName
