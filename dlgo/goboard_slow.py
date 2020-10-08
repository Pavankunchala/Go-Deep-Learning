import copy
from dlgo.gotypes import Player

#there are three moves in the game of Go
# play ,pass , Resign

class Move():
    def __init__(self,point = None,is_pass = False,is_resign = False):
        " Any action a player can play on a turn—is_play, is_pass, or is_resign— will be set."
        assert(point is not None)^ is_pass ^ is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls,point):
        return Move(point= point)

    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)

    @classmethod
    def resign(cls):
        return Move(is_resign=True)

# Go strings are a chain of connected stones of the same color.
class GoString():

    def __init__(self,color, stones ,liberties):
        self.color = color
        self.stones= set(stones)
        self.liberties = set(liberties)

    #Removing a libertiy
    def remove_libertiy(self,point):
        self.liberties.remove(point)
    #adding a libertiy
    def add_libertiy(self,point):
        self.liberties.add(point)

    def merged_with(self,go_string):
        assert go_string.color == self.color
        combined_stones = self.stones | go_string.stones

        return GoString(
            self.color,
            combined_stones,
            (self.liberties | go_string.liberties) - combined_stones
        )
    @property
    def num_liberties(self):
        return len(self.liberties)

    def __eq__(self, other):

        return isinstance(other, GoString) and \
            self.color == other.color and \
            self.stones == other.stones and \
            self.liberties == other.liberties


    


       

    

        