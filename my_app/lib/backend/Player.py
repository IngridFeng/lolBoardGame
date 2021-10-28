class Player:
    def __init__(self, money=INITIAL_BUY_IN):
        self.money = money
        self.hands = None

    def addHands(self, hands):
        self.hands = hands        

    def actionFold(self):
        self.hands = None
    
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