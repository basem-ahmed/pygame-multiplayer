class Player(object):
    STATE_IDLE  = 1
    STATE_MOVE  = 2
    STATE_SWING = 3
    STATE_HURT  = 4

    def __init__(self):
        self.connected = False
        self.name = "Test_1"
        self.connection_uid = None

        self.state = None  # last known state
        self.time = None  # Time of last update
        self.latency = None  # Half of roundtrip latency in ms

        self.pos_x = 0
        self.pos_y = 0
        self.direction = 0  # Angle facing
        self.speed = 0.0  # Movement speed
