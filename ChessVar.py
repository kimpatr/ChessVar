# Author: Patrick Kim
# GitHub username: kimpatr
# Date: 11/27/23
# Description: This Portfolio project creates a ChessVar class which has Chess Piece objects. It checks if moves are valid
# and updates the board accordingly after each move. The game is won once all of a single piece
# type is catpured from the opposing color. The game state is updated accordingly.

class ChessPiece:
    """
    This method represents a ChessPiece. Specific Types will inherit this class
    """

    def __init__(self, id, color):
        self._id = id
        self._color = color

    def get_id(self):
        """ This method returns the id of the piece object"""
        return self._id

    def get_color(self):
        """ This method returns the color of the piece object"""
        return self._color

class Pawn(ChessPiece):
    """
    Represents a Pawn
    Inherits from ChessPiece class and is connected to ChessVar class.
    """
    def __init__(self, id, color):
        super().__init__(id, color)

    def __repr__(self):
        if self._color == 'White':
            return "W.Pawn"
        else:
            return "B.Pawn"

    def valid_move(self,source, dest, game_object):
        """
        This method will determine if the dest is valid based on the source specific to the Pawn.
        :param source:
        :param dest:
        :return: True or False
        """
        columns = ['a','b','c','d','e','f','g','h']
        # if pawn has reached other end, return False
        if list(source)[1] == '8' or list(source)[1] == '1':
            return False
        if list(source)[0] != list(dest)[0]:
            if game_object.get_occupied_by(dest) is None:
                return False
            else:
                return self.valid_capture(source,dest)
        else:
            if game_object.get_occupied_by(dest) is not None:
                return False
        # White
        if self._color == "White":
            # if backwards, return False
            if int(list(source)[1]) > int(list(dest)[1]):
                return False
            # if first move is more than 2 spaces, return False
            if list(source)[1] == '2':
                if int(list(dest)[1]) > 4:
                    return False
                return check_path(source,dest,game_object,"vertical")
            # after first move, if move is more than 1 space, return False
            elif int(list(source)[1]) + 1 < int(list(dest)[1]):
                return False
            else:
                return True
        # Black
        else:
            if int(list(source)[1]) < int(list(dest)[1]):
                return False
            # if first move is more than 2 spaces, return False
            if list(source)[1] == '7':
                if int(list(dest)[1]) < 5:
                    return False
            # after first move, if move is more than 1 space, return False
            elif int(list(source)[1]) - 1 < int(list(dest)[1]):
                return False
            else:
                return True

    def valid_capture(self,source,dest):
        """
        This method will determine if the capture is valid for the pawn based on parameters.
        :param source:
        :param dest:
        :return: True or False
        """
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        if columns.index(list(dest)[0]) != columns.index(list(source)[0]) + 1 and columns.index(list(dest)[0]) != columns.index(list(source)[0]) - 1:
            return False
        if self._color == "White":
            if int(list(dest)[1]) != int(list(source)[1]) + 1:
                return False
        else:
            if int(list(dest)[1]) != int(list(source)[1]) - 1:
                return False


class Rook(ChessPiece):
    """
    Represents a Rook
    Inherits from ChessPiece class and is connected to ChessVar class.
    """

    def __init__(self, id, color):
        super().__init__(id, color)

    def __repr__(self):
        if self._color == 'White':
            return "W.Rook"
        else:
            return "B.Rook"

    def valid_move(self, source, dest, game_object):
        """
        This method will determine if the dest is valid based on the source specific to the Rook.
        :param source:
        :param dest:
        :return: True or False
        """
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        # Horizontal Movement
        if list(dest)[0] != list(source)[0]:
            if list(dest)[1] != list(source)[1]:
                return False
            #path clear
            # smaller = min(columns.index(list(dest)[0]),columns.index(list(source)[0]))
            # larger = max(columns.index(list(dest)[0]),columns.index(list(source)[0]))
            # for index in range(smaller+1,larger):
            #     if game_object.get_occupied_by(columns[index]+list(dest)[1]) is not None:
            #         return False
            return check_path(source,dest,game_object,'horizontal')
        # Vertical Movement
        if list(dest)[1] != list(source)[1]:
            if list(dest)[0] != list(source)[0]:
                return False
            #path clear
            # smaller = min(int(list(dest)[1]),int(list(source)[1]))
            # larger = max(int(list(dest)[1]),int(list(source)[1]))
            # for index in range(smaller+1,larger):
            #     if game_object.get_occupied_by(list(dest)[0]+str(index)):
            #         return False

            # DOEST THIS NEED TO BE RETURNED OR JUST CALLED???
            return check_path(source, dest, game_object, 'vertical')
        # else:
        #     return True

class Bishop(ChessPiece):
    """
    Represents a Bishop.
    Inherits from ChessPiece class and is connected to ChessVar class.
    """

    def __init__(self, id, color):
        super().__init__(id, color)

    def __repr__(self):
        if self._color == 'White':
            return "W.Bish"
        else:
            return "B.Bish"

    def valid_move(self, source, dest, game_object):
        """
        This method will determine if the dest is valid based on the source specific to the Bishop.
        :param source:
        :param dest:
        :return: True or False
        """
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        if abs(int(list(dest)[1]) - int(list(source)[1])) != abs(columns.index(list(dest)[0])-columns.index(list(source)[0])):
            return False
        else:
            return check_path(source, dest, game_object, "diagonal")

class Knight(ChessPiece):
    """
    Represents a Knight.
    Inherits from ChessPiece class and is connected to ChessVar class.
    """

    def __init__(self, id, color):
        super().__init__(id, color)

    def __repr__(self):
        if self._color == 'White':
            return "W.Knht"
        else:
            return "B.Knht"

    def valid_move(self, source, dest, game_object):
        """
        This method will determine if the dest is valid based on the source specific to the Knight.
        :param source:
        :param dest:
        :return: True or False
        """
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        if abs(int(list(dest)[1]) - int(list(source)[1])) != 2:
            if abs(columns.index(list(dest)[0])-columns.index(list(source)[0])) != 2:
                return False
        if abs(int(list(dest)[1]) - int(list(source)[1])) == 2:
            if abs(columns.index(list(dest)[0])-columns.index(list(source)[0])) != 1:
                return False
        if abs(columns.index(list(dest)[0])-columns.index(list(source)[0])) == 2:
            if abs(int(list(dest)[1]) - int(list(source)[1])) != 1:
                return False
        else:
            return True

class Queen(ChessPiece):
    """
    Represents a Queen.
    Inherits from ChessPiece class and is connected to ChessVar class.
    """

    def __init__(self, id, color):
        super().__init__(id, color)

    def __repr__(self):
        if self._color == 'White':
            return "W.Quee"
        else:
            return "B.Quee"

    def valid_move(self, source, dest, game_object):
        """
        This method will determine if the dest is valid based on the source specific to the Queen.
        :param source:
        :param dest:
        :return: True or False
        """
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        #diagonal
        if abs(int(list(dest)[1]) - int(list(source)[1])) == abs(columns.index(list(dest)[0])-columns.index(list(source)[0])):
            return check_path(source,dest,game_object,"diagonal")
        #left/right
        if list(dest)[0] != list(source)[0]:
            if list(dest)[1] != list(source)[1]:
                return False
            else:
                return check_path(source, dest, game_object, "horizontal")
        if list(dest)[1] != list(source)[1]:
            if list(dest)[0] != list(source)[0]:
                return False
            else:
                return check_path(source,dest,game_object,"vertical")


class King(ChessPiece):
    """
    Represents a King
    Inherits from ChessPiece class and is connected to ChessVar class.
    """

    def __init__(self, id, color):
        super().__init__(id, color)

    def __repr__(self):
        if self._color == 'White':
            return "W.King"
        else:
            return "B.King"

    def valid_move(self,source,dest, game_object):
        """
        This method will determine if the dest is valid based on the source specific to the King.
        :param source:
        :param dest:
        :return: True or False
        """
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        if abs(int(list(source)[1])-int(list(dest)[1])) > 1:
            return False
        if abs(columns.index(list(source)[0])-columns.index(list(dest)[0])) > 1:
            return False

class ChessVar:
    """
    This class represents the game.
    Each piece is connected to this Class.
    Initializes the pieces, the board, places the pieces on the board.
    Initializes the turn to white and initializes a diciontary for captured pieces for black and white.
    """

    def __init__(self):
        self._game_state = 'UNFINISHED'
        self._game_board = [{'a8':None,'b8':None,'c8':None,'d8':None,'e8':None,'f8':None,'g8':None,'h8':None},
                            {'a7':None,'b7':None,'c7':None,'d7':None,'e7':None,'f7':None,'g7':None,'h7':None},
                            {'a6':None,'b6':None,'c6':None,'d6':None,'e6':None,'f6':None,'g6':None,'h6':None},
                            {'a5':None,'b5':None,'c5':None,'d5':None,'e5':None,'f5':None,'g5':None,'h5':None},
                            {'a4':None,'b4':None,'c4':None,'d4':None,'e4':None,'f4':None,'g4':None,'h4':None},
                            {'a3':None,'b3':None,'c3':None,'d3':None,'e3':None,'f3':None,'g3':None,'h3':None},
                            {'a2':None,'b2':None,'c2':None,'d2':None,'e2':None,'f2':None,'g2':None,'h2':None},
                            {'a1':None,'b1':None,'c1':None,'d1':None,'e1':None,'f1':None,'g1':None,'h1':None}]
        self._turn = 'White'
        self._remaining_wht = {'Pawn': 8, 'Rook': 2, 'Knight': 2, 'Bishop': 2, 'Queen': 1, 'King': 1}
        self._remaining_blk = {'Pawn': 8, 'Rook': 2, 'Knight': 2, 'Bishop': 2, 'Queen': 1, 'King': 1}

        # create black pieces
        p1 = Pawn('pb1', 'Black')
        p2 = Pawn('pb2', 'Black')
        p3 = Pawn('pb3', 'Black')
        p4 = Pawn('pb4', 'Black')
        p5 = Pawn('pb5', 'Black')
        p6 = Pawn('pb6', 'Black')
        p7 = Pawn('pb7', 'Black')
        p8 = Pawn('pb8', 'Black')
        r1 = Rook('rb1', 'Black')
        r2 = Rook('rb2', 'Black')
        b1 = Bishop('bb1', 'Black')
        b2 = Bishop('bb2', 'Black')
        k1 = Knight('kb1', 'Black')
        k2 = Knight('kb2', 'Black')
        q1 = Queen('qb1', 'Black')
        K1 = King('Kb1 ', 'Black')
        # create white pieces
        p9 = Pawn('pw1', 'White')
        p10 = Pawn('pw2', 'White')
        p11 = Pawn('pw3', 'White')
        p12 = Pawn('pw4', 'White')
        p13 = Pawn('pw5', 'White')
        p14 = Pawn('pw6', 'White')
        p15 = Pawn('pw7', 'White')
        p16 = Pawn('pw8', 'White')
        r3 = Rook('rw1', 'White')
        r4 = Rook('rw2', 'White')
        b3 = Bishop('bw1', 'White')
        b4 = Bishop('bw2', 'White')
        k3 = Knight('kw1', 'White')
        k4 = Knight('kw2', 'White')
        q2 = Queen('qw1', 'White')
        K2 = King('Kw1', 'White')

        # initializing board
        self._game_board[1]['a7'] = p1
        self._game_board[1]['b7'] = p2
        self._game_board[1]['c7'] = p3
        self._game_board[1]['d7'] = p4
        self._game_board[1]['e7'] = p5
        self._game_board[1]['f7'] = p6
        self._game_board[1]['g7'] = p7
        self._game_board[1]['h7'] = p8
        self._game_board[0]['a8'] = r1
        self._game_board[0]['b8'] = k1
        self._game_board[0]['c8'] = b1
        self._game_board[0]['d8'] = q1
        self._game_board[0]['e8'] = K1
        self._game_board[0]['f8'] = b2
        self._game_board[0]['g8'] = k2
        self._game_board[0]['h8'] = r2

        self._game_board[6]['a2'] = p9
        self._game_board[6]['b2'] = p10
        self._game_board[6]['c2'] = p11
        self._game_board[6]['d2'] = p12
        self._game_board[6]['e2'] = p13
        self._game_board[6]['f2'] = p14
        self._game_board[6]['g2'] = p15
        self._game_board[6]['h2'] = p16
        self._game_board[7]['a1'] = r3
        self._game_board[7]['b1'] = k3
        self._game_board[7]['c1'] = b3
        self._game_board[7]['d1'] = q2
        self._game_board[7]['e1'] = K2
        self._game_board[7]['f1'] = b4
        self._game_board[7]['g1'] = k4
        self._game_board[7]['h1'] = r4

    def get_occupied_by(self,loc):
        for row in self._game_board:
            if loc in row:
                return row[loc]

    def set_occupied_by(self,loc,piece_object):
        for row in self._game_board:
            if loc in row:
                self._game_board[self._game_board.index(row)][loc] = piece_object
                return

    def get_game_state(self):
        """
        This method returns the state of the game base on the current board.
        If a player has won, either "WHITE_WON" or "BLACK_WON" will be returned.
        If a player has not won yet or the game has just started,
        "UNFINISHED" will be returned.

        Input: None
        :return: One of the values: 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        return self._game_state

    def set_game_state(self,state):
        """this will update the game state"""
        self._game_state = state

    def get_board(self):
        """this returns the board list of dictionaries"""
        return self._game_board

    def check_captures(self):
        """
        checks the dictionaries, if a certain piece value has reached a specific limit,
        it will call the set_game_state method and set the game_state to either 'WHITE_WON' or
        'BLACK_WON'
        """
        if 0 in self._remaining_wht.values():
            self.set_game_state('BLACK_WON')
            print(self.get_game_state())
        if 0 in self._remaining_blk.values():
            self.set_game_state('WHITE_WON')
            print(self.get_game_state())

    def make_move(self, from_sqr, to_sqr, game_object=None):
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
        piece_object = self.get_occupied_by(from_sqr)
        # if from_sqr is empty, return False
        if piece_object is None:
            return False
        # if to_sqr doesn't exist, return False
        if len(to_sqr) > 2 or len(from_sqr) > 2:
            return False
        if list(to_sqr)[0] not in 'abcdefgh' or list(to_sqr)[1] not in '12345678':
            print("This destination does not exist!")
            return False
        # if attempting to move opposite player's piece
        if self._turn != piece_object.get_color():
            print("It is not your turn!")
            return False
        # if illegal move, return False
        if piece_object.valid_move(from_sqr,to_sqr,self) == False:
            print("Invalid move!")
            return False
        # if get_game_state != 'UNFINISHED', return False
        if self._game_state != 'UNFINISHED':
            return False
        else:
            # if dest is occupied
            if self.get_occupied_by(to_sqr) is not None:
                # if own piece is in dest
                if piece_object.get_color() == self.get_occupied_by(to_sqr).get_color():
                    print("You cannot capture your own piece!")
                    return False
                else:
                    self.capture_piece(self.get_occupied_by(to_sqr))
            # if dest is available
            self.set_occupied_by(from_sqr,None)
            self.set_occupied_by(to_sqr,piece_object)
            if self._turn == "White":
                self._turn = "Black"
            else:
                self._turn = "White"
            return True

    def capture_piece(self,captured_piece_obj):
        """
        When called, depending on the color of the capture piece,
        the other color's captured piece
        dictionary will be updated.
        :return: prints the game_state
        """
        color = captured_piece_obj.get_color()
        piece_type = captured_piece_obj.__class__.__name__
        print(f"{color} {piece_type} has been captured.")

        if color == "White":
            self._remaining_wht[piece_type] -= 1
        else:
            self._remaining_blk[piece_type] -= 1
        self.check_captures()

    def display_board(self):
        """
        This method will display the board showing pieces in each location. For debugging purposes.
        :return: prints board
        """
        for row in self._game_board:
            disp_list = []
            for kvtup in list(row.items()):
                if kvtup[1] is None:
                    disp_list.append((kvtup[0], '    '))
                else:
                    disp_list.append(kvtup)
            print(disp_list)
        print(f'White has the following pieces left: {game1._remaining_wht}')
        print(f'Black has the following pieces left: {game1._remaining_blk}')

def check_path(source,dest,game_object,direction):
    """
    This method checks the path is clear from source to destination.
    :param source: from square
    :param dest: to square
    :param game_object: game object
    :param direction: "horizontal" "verticla" or "diagonal"
    :return:
    """
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    dest_let_ind = columns.index(list(dest)[0])
    source_let_ind = columns.index(list(source)[0])
    dest_num = int(list(dest)[1])
    source_num = int(list(source)[1])

    if direction == 'horizontal':
        smaller = min(dest_let_ind, source_let_ind)
        larger = max(dest_let_ind, source_let_ind)
        for index in range(smaller + 1, larger):
            if game_object.get_occupied_by(columns[index] + list(dest)[1]) is not None:
                return False
    if direction == 'vertical':
        smaller = min(dest_num, source_num)
        larger = max(dest_num, source_num)
        for index in range(smaller + 1, larger):
            if game_object.get_occupied_by(list(dest)[0] + str(index)) is not None:
                return False
    if direction == 'diagonal':
        # if left
        if dest_let_ind - source_let_ind < 0:
            # if up
            if dest_num - source_num > 0:
                for squares in range(1, abs(dest_num - source_num)):
                    if game_object.get_occupied_by(columns[source_let_ind - squares] + str(source_num + squares)) is not None:
                        return False
            # if down
            else:
                for squares in range(1, abs(dest_num - source_num)):
                    if game_object.get_occupied_by(columns[source_let_ind - squares] + str(source_num - squares)) is not None:
                        return False
        # if right
        else:
            # if up
            if dest_num - source_num > 0:
                for squares in range(1, abs(dest_num - source_num)):
                    if game_object.get_occupied_by(columns[source_let_ind + squares] + str(source_num + squares)) is not None:
                        return False
            # if down
            else:
                for squares in range(1, abs(dest_num - source_num)):
                    if game_object.get_occupied_by(columns[source_let_ind + squares] + str(source_num - squares)) is not None:
                        return False
