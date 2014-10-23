import pickle

from shared_objects.base_player import BasePlayer


class Message:
    WELCOME = 0
    CREATE_PLAYER = 1
    PLAYER_INFO = 2
    DESTROY_PLAYER = 3
    STATE_CHANGE = 4

    def serialize(self):
        return pickle.dumps(self)


class WelcomeMessage(Message):
    def __init__(self, data='welcome'):
        self.header = Message.WELCOME
        self.data = data


class StateChangeMessage(Message):
    def __init__(self, player_state=None, direction=None, x=None, y=None):
        self.header = Message.STATE_CHANGE
        self.player_state = player_state
        self.direction = direction


class PlayerPositionMessage(Message):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

class PlayerInfo(Message):
    def __init__(self, rect):
        self.rect = rect