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
    

class Board():
    """
    A board is initialized as an empty grid with the specified number of rows and columns.
    """

    def __init__(self,num_rows, num_cols):
        self.num_rows = num_cols
        self.num_cols =  num_cols
        self.grid = {}
    
    def place_stone(self,player,point):
        
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        adjacent_same_color = []
        adjacent_opposite_color = []
        liberties = []

        for neighbor in point.neighbors():
            if not self.is_on_grid(neighbor):
                continue
            neighbor_string= self._grid.get(neighbor)
            if neighbor_string is None:
                liberties.append(neighbor)
            elif neighbor_string.color == player:

                if neighbor_string not in adjacent_same_color:
                    adjacent_same_color.append(neighbor_string)
            else:
                if neighbor_string not in adjacent_opposite_color:
                    adjacent_opposite_color.append(neighbor_string)

        new_string = GoString(player,[point],liberties)

        #Merge any adjacent strings of the same color.
        for same_color_string in adjacent_same_color:  
            new_string = new_string.merged_with(same_color_string)
        for new_string_point in new_string.stones:
            self._grid[new_string_point] = new_string
        #Reduce liberties of any adjacent strings of the opposite color.
        for other_color_string in adjacent_opposite_color:  
            other_color_string.remove_liberty(point)
        #If any opposite­color strings now have zero liberties, remove them.
        for other_color_string in adjacent_opposite_color: 
            if other_color_string.num_liberties == 0:
                self._remove_string(other_color_string)

    def is_on_grid(self,point):
        return 1 <= point.row <= self.num_rows and   1 <= point.col <= self.num_cols

    """
    Returns the content of a point on the board: a Player if a stone is on that point, or else None
    """
    def get(self,point):
        string = self._grid.get(point)
        if string is None:
            return None
        return string.color

    """
    Returns the entire string of stones at a point: a GoString if a stone is on that point, or else None
    """
    def get_go_string(self,point):
        string = self._grid.get(point)
        if string is None:

            return None
        return string


        



        




       

    


    


       

    

        