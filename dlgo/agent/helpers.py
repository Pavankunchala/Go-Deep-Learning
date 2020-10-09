from dlgo.gotypes import Point

# An eye is an empty point

def is_point_an_eye(board, point, color):
    if board.get(point) is not None:
        return False

    #All adjacent points must contain friendly stones.
    for neighbor in point.neighbor():
        if board.is_on_grid(neighbor):

            neighbor_color = board.get(neighbor)
            if neighbor_color != color:
                return False

        """
        We must control three out of four corners if the point is in the middle of the board; 
        on the edge, you must control all corners.

        """    
        friendly_corners = 0
        off_board_corners = 0

        corners = [
            Point(point.row - 1, point.col - 1),
            Point(point.row - 1, point.col + 1),
            Point(point.row + 1, point.col - 1),
            Point(point.row + 1, point.col + 1),
        ]

        for corner in corners:
            if board.is_on_grid(corner):
                corner_color = board.get(corner)
                if corner_color == color:
                    friendly_corners +=1

            else:
                off_board_corners +=1

        if off_board_corners>0:

            # Point is on the edge or corner.
            return off_board_corners + friendly_corners == 4
        #Point is in the middle.    
        return friendly_corners >3


 