# Author: Patrick Kim
# GitHub username: kimpatr
# Date: 11/27/23
# Description: Halfway Progress Report for ChessVar Portfolio Project

class ChessPiece:
    """
    This method represents a ChessPiece. Specific Types will inherit this class
    """
    def __init__(self,id,color):
        """each piece will have a specific id and will be either black or white"""

class Pawn(ChessPiece):
    """
    Represents a Pawn
    Inherits from ChessPiece class and is connected to ChessVar class.
    """
    def __init__(self,id,color):
        super().__init__(id,color)

    def valid_move(self,source,dest):
        """
        This method will determine if the dest is valid based on the source specific to the Pawn.
        :param source:
        :param dest:
        :return: True or False
        """
        pass

    def valid_capture(self,source,dest):
        """
        This method will determine if the capture is valid for the pawn based on parameters.
        :param source:
        :param dest:
        :return: True or False
        """

class Rook(ChessPiece):
    """
    Represents a Rook
    Inherits from ChessPiece class and is connected to ChessVar class.
    """
    def __init__(self,id,color):
        super().__init__(id,color)

    def valid_move(self,source,dest):
        """
        This method will determine if the dest is valid based on the source specific to the Rook.
        :param source:
        :param dest:
        :return: True or False
        """
        pass

class Knight(ChessPiece):
    """
    Represents a Knight.
    Inherits from ChessPiece class and is connected to ChessVar class.
    """
    def __init__(self,id,color):
        super().__init__(id,color)

    def valid_move(self,source,dest):
        """
        This method will determine if the dest is valid based on the source specific to the Knight.
        :param source:
        :param dest:
        :return: True or False
        """
        pass

class Bishop(ChessPiece):
    """
    Represents a Bishop.
    Inherits from ChessPiece class and is connected to ChessVar class.
    """
    def __init__(self,id,color):
        super().__init__(id,color)

    def valid_move(self,source,dest):
        """
        This method will determine if the dest is valid based on the source specific to the Bishop.
        :param source:
        :param dest:
        :return: True or False
        """
        pass

class Queen(ChessPiece):
    """
    Represents a Queen.
    Inherits from ChessPiece class and is connected to ChessVar class.
    """
    def __init__(self,id,color):
        super().__init__(id,color)

    def valid_move(self,source,dest):
        """
        This method will determine if the dest is valid based on the source specific to the Queen.
        :param source:
        :param dest:
        :return: True or False
        """
        pass

class King(ChessPiece):
    """
    Represents a King
    Inherits from ChessPiece class and is connected to ChessVar class.
    """
    def __init__(self,id,color):
        super().__init__(id,color)

    def valid_move(self,source,dest):
        """
        This method will determine if the dest is valid based on the source specific to the King.
        :param source:
        :param dest:
        :return: True or False
        """
        pass

class ChessVar:
    """
    This class represents the game.
    Each piece is connected to this Class.
    """

    def __init__(self):
        """
        It will initialize the board, it will create each piece and assign the pieces to the board.
        It will initialize the game_state to 'Unfinished'. It will initialize the turn to 'White'
        It will initialize two captured dictionaries (one for each color) for piece type as the keys
        with 0 for each value.
        """
        pass

    def get_game_state(self):
        """
        This method returns the state of the game base on the current board.
        If a player has won, either "WHITE_WON" or "BLACK_WON" will be returned.
        If a player has not won yet or the game has just started,
        "UNFINISHED" will be returned.

        Input: None
        :return: One of the values: 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        pass

    def set_game_state(self,state):
        """this will update the game state"""
        self._game_state = state
        pass

    def check_captures(self):
        """
        checks the dictionaries, if a certain piece value has reached a specific limit,
        it will call the set_game_state method and set the game_state to either 'WHITE_WON' or
        'BLACK_WON'
        """

    def make_move(self, from_sq, to_sq):
        """
        If from_sq does not contain a piece belonging to the player whose
        turn it is, or if the indicated move is not legal, or if the game has
        already been won, then it should return False.
        Otherwise, it should make the indicated move, remove any captured piece(by calling
        capture_piece method),
        update the game state if necessary, update whose turn it is, and
        return True.

        :param from_sq: This is the square you want to move from
        :param to_sq: This is the square you want to move to
        :return: either TRUE or FALSE
        """
        pass

    def capture_piece(self):
        """
        When called, depending on the color of the capture piece, the other color's captured piece
        dictionary will be updated.
        :return:
        """
        pass

    def display_board(self):
        """
        This method will display the board showing pieces in each location. For debugging purposes.
        :return: prints board
        """
        pass

"""
Scenario 1: Initializing the ChessVar class
    The ChessVar class will initialize an empty board, create each piece type object, and fill the board.
    The turn will also be initialized to 'White'
    The game_state will also be initialized to 'UNFINISHED'
    It will also initialize two dictionaries for each color to keep track of captured pieces.
        The keys will be each piece type and the values will be set to 0.
        
Scenario 2: Keeping track of turn order
    The last portion of the make_move method will check the game_state, if it is still 'UNFINISHED',
    it will update the turn to 'Black' if set to 'White' and vice-versa.
    
Scenario 3: Keeping track of the current board position
    There will be a display_board method in the ChessVar class that displays the board and 
    where each piece is on the board.
    
Scenario 4: Determining if a regular move is valid
    In the make_move method, if the destination square is empty, it will call a function within
    the piece class for valid_move.
    For each piece type class, there will be a valid_move method which will take a source and destination
    location as parameters, it will return True if the move is valid and False if the move is invalid.
    
Scenario 5: Determining if a capture is valid
    In the make_move method, if the destination square is NOT empty, it will call a function valid_capture.
    If the color of the piece in the destination is the same color as the player, it will return False.
    If the color is the opposite as the player, it will check other scenarios.
    If it is a pawn, it will run another method within the pawn class to verify if the capture is valid.
    and return True or False based on that method.
    If it is not a pawn, it will run the valid_move method and return True or False based on that method.

Scenario 6: Determining the current state of the game
    After each successful capture, the dictionary will be updated, the check_captures method will be run
    to verify if winning conditions have been met, if they have, it will call the set_game_state method
    accordingly.
    
"""