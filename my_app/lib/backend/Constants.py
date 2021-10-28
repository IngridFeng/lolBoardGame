from enum import Enum

# Cards
class Colors(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4

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