import Constants
import Cards
import Player
import Round

class Game:
    def __init__(self, hostUsername):
        self.hostUsername = hostUsername
        self.players = {}
        self.addPlayer(hostUsername)
        self.rounds = []
    
    def addPlayer(self, username):
        self.players[username] = Player()
        
    def start(self):
        if len(self.players) + 1 != Constants.NUMBER_OF_PLAYERS:
            raise ValueError("Incorrect number of players!")
    
    def newRound(self):
        newRound = Round(self.players)
        self.rounds.append(newRound)
        return newRound
        
    def end(self):
        return sorted(players, key=lambda x: x.money, reversed=True)
    
class Games:
    def __init__(self):
        self.games = []
    
    def new(self):
        newGame = Game()
        self.games.append(newGame)
        return newGame
    
    def getAllGames(self):
        return self.games