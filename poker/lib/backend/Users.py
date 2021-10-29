import Constants

class Users:
    def __init__(self):
        self.users = {}
    
    def registerUser(self, username, password):
        if username in self.users:
            return Constants.RegistrationError.USERNAME_ALREADY_EXISTS
        if len(password) < 6:
            return Constants.RegistrationError.PASSWORD_TOO_SHORT
        self.users[username] = password
    
    def validatePasswordForUser(self, username, password):
        return self.users[username] == password
    
