#Simple base for the agent

class Agent:
    def __init__(self):
        pass

    def select(self,game_state):
        raise NotImplementedError()


       