from functools import total_ordering

import Constants

@total_ordering
class Hands:
    def __init__(self, hands):
        self.hands = hands
        self.numbers = sorted([card.getNumber().value for card in hands])
        self.countNumbers = self.countHands()
    
    def countHands(self):
        dic = {}
        for n in self.numbers:
            if n not in dic:
                dic[n] = 0
            else:
                dic[n] += 1
        return sorted(dic.values)

    def isRoyal(self):
        return getNumbers(hands) == [1, 10, 11, 12, 13]
    
    def isRoyalFlush(self):
        return self.isRoyal(hands) and self.isFlush(hands)

    def isStraightFlush(self):
        return self.isFlush(hands) and self.isStraight(hands)

    def isFourOfAKind(self):
        return countHands(getNumbers(hands)) == [1, 4]

    def isFullHouse(self):
        return countHands(getNumbers(hands)) == [2, 3]

    def isFlush(self):
        color = hands[0].getColor()
        for card in hands[1:]:
            if card.getColor() != color:
                return False
        return True

    def isStraight(self):
        numbers = getNumbers(hands)
        return numbers == list(range(min(numbers), max(numbers) + 1)) or numbers == [1, 10, 11, 12, 13]

    def isThreeOfAKind(self):
        return countHands(getNumbers(hands)) == [1, 1, 3]

    def isTwoPair(self):
        return countHands(getNumbers(hands)) == [1, 2, 2]

    def isOnePair(self):
        return countHands(getNumbers(hands)) == [1, 1, 1, 2]
    
    def getHandType(self):
        if self.isRoyalFlush():
            return Constants.HandType.ROYAL_FLUSH
        if self.isStraightFlush()
            return Constants.HandType.STRAIGHT_FLUSH
        if self.isFourOfAKind():
            return Constants.HandType.FOUR_OF_A_KIND
        if self.isFullHouse():
            return Constants.HandType.FULL_HOUSE
        if self.isFlush():
            return Constants.HandType.FLUSH
        if self.isStraight():
            return Constants.HandType.STRAIGHT
        if self.isThreeOfAKind():
            return Constants.HandType.THREE_OF_A_KIND
        if self.isTwoPair():
            return Constants.HandType.TWO_PAIR
        if self.isOnePair():
            return Constants.HandType.ONE_PAIR
        return Constants.HandType.HIGH_CARD
    
    def __eq__(self, other):
        return self.getHandType() == other.getHandType() and self.compareNumbers(hands1, hands2) == 0

    def __ne__(self, other):
        return self.getHandType() != other.getHandType() or self.compareNumbers(hands1, hands2) != 0

    def __lt__(self, other):
        if self.getHandType().value < other.getHandType().value:
            return True
        if self.getHandType().value > other.getHandType().value:
            return False
        return self.compareNumbers(hands1, hands2) == -1 

    def __repr__(self):
        res = ""
        res += "The hands have five cards:\n"
        for hand in self.hands:
            res += hand + "\n"
        res += "The hands have type %s:\n" % (self.getHandType())
        return 
        
    def compareNumbers(hands1, hands2):
        if len(hands1) != len(hands2):
            raise ValueError("Two hands have different number of cards!")
        hands1 = sorted(hands1)
        hands2 = sorted(hands2)
        while hands1 and hands2:
            h1 = hands1.pop()
            h2 = hands2.pop()
            if h1 > h2:
                return -1
            if h2 > h1:
                return 1
        return 0