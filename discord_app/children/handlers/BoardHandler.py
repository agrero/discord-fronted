


class BoardHandler:
    """
    takes in a linear string that represents a board
    
    returns a 2d board 
    """
    def __init__(self, in_board:str) -> None:
        self.in_board = in_board

        # expensive but whatever
        self.list_1d = self._1d_from_string()
        self.list_2d = self._2d_from_string()

    def _1d_from_string(self):
        """
        in: linear string 
        out: 2d list of string
        """
        return [
            i for i in self.in_board
        ]

    def _2d_from_string(self):
        """
        in: linear string 
        out: 2d list of string
        """
        return [
            [i for i in self.in_board][j:j+9]
            for j in range(0,81,9)
        ]

