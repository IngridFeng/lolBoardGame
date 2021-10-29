from enum import Enum

# Cards
class Colors(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4

class Numbers(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13 

# Users
class RegistrationError(Enum):
    USERNAME_ALREADY_EXISTS = 1
    PASSWORD_TOO_SHORT = 2

# Games
NUMBER_OF_PLAYERS = 4
INITIAL_BUY_IN = 200

class PlayerAction(Enum):
    FOLD = 1
    CHECK = 2
    CALL = 3
    RAISE = 4

class HandType(Enum):
    ROYAL_FLUSH = 1
    STRAIGHT_FLUSH = 2
    FOUR_OF_A_KIND = 3
    FULL_HOUSE = 4
    FLUSH = 5
    STRAIGHT = 6
    THREE_OF_A_KIND = 7
    TWO_PAIR = 8
    ONE_PAIR = 9
    HIGH_CARD = 10