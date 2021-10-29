class Player:
    def __init__(self, username, money=INITIAL_BUY_IN):
        self.username = username
        self.money = money
        self.playerCards = None
        self.highHands = None
    
    def getUsername(self):
        return self.username

    def getMoney(self):
        return self.money
    
    def getPlayerCards(self):
        return self.hands
    
    def getHighHands(self):
        return self.highHands

    def setPlayerCards(self, playerCards):
        self.playerCards = playerCards   
    
    def setHighHands(self, highHands):
        self.highHands = highHands

    def actionFold(self):
        self.playerCards = None
    
    def actionCheck(self):
        pass
    
    def actionCall(self, money):
        if money > self.money:
            raise ValueError("Insufficient fund!")
        self.money -= money
    
    def actionRaise(self, money):
        if money > self.money:
            raise ValueError("Insufficient fund!")
        self.money -= money
    
    def actionWin(self, money):
        self.money += money