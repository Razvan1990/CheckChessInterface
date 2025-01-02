import constans_values
from checker_positions import CheckPiecePositions


class Checker:

    def __init__(self):
        self.pos_checker = CheckPiecePositions()

    def check_chess_queen(self, position_king, position_queen):
        '''like in all the check functions we compare position of king with the piece when we try to move the black king from check'''
        '''vertical check'''
        c = self.check_higher(position_king, position_queen)
        king_queen_same_row = self.check_if_king_queen_same_row(position_king, position_queen)
        if c % 8 == 0 and position_king != position_queen:
            return True
        '''horizontal check'''
        c = self.check_higher(position_king, position_queen)
        if c <= 7 and king_queen_same_row and position_king != position_queen:
            return True
        '''diagonal check'''
        if abs(position_king - position_queen) % 7 == 0 and ((
                                                                     position_king in constans_values.POSITIONS_BLACK and position_queen in constans_values.POSITIONS_BLACK) or (
                                                                     position_king in constans_values.POSITIONS_WHITE and position_queen in constans_values.POSITIONS_WHITE)) and (
                position_king != position_queen):
            return True
        if abs(position_king - position_queen) % 9 == 0 and ((
                                                                     position_king in constans_values.POSITIONS_BLACK and position_queen in constans_values.POSITIONS_BLACK) or (
                                                                     position_king in constans_values.POSITIONS_WHITE and position_queen in constans_values.POSITIONS_WHITE)) and (
                position_king != position_queen):
            return True
        return False

    def check_chess_rook(self, position_king, position_rook):
        '''vertical check'''
        c = self.check_higher(position_king, position_rook)
        king_queen_same_row = self.check_if_king_queen_same_row(position_king, position_rook)
        if c % 8 == 0 and position_king != position_rook:
            return True
        '''horizontal check'''
        c = self.check_higher(position_king, position_rook)
        if c <= 7 and king_queen_same_row and position_king != position_rook:
            return True
        return False

    def check_chess_bishop(self, position_king, position_bishop):
        '''diagonal check'''
        if abs(position_king - position_bishop) % 7 == 0 and ((
                                                                      position_king in constans_values.POSITIONS_BLACK and position_bishop in constans_values.POSITIONS_BLACK) or (
                                                                      position_king in constans_values.POSITIONS_WHITE and position_bishop in constans_values.POSITIONS_WHITE)) and (
                position_king != position_bishop):
            return True
        if abs(position_king - position_bishop) % 9 == 0 and ((
                                                                      position_king in constans_values.POSITIONS_BLACK and position_bishop in constans_values.POSITIONS_BLACK) or (
                                                                      position_king in constans_values.POSITIONS_WHITE and position_bishop in constans_values.POSITIONS_WHITE)) and (
                position_king != position_bishop):
            return True
        return False

    def check_chess_pawn(self, position_king, position_pawn):
        '''
        The pawns will be filtered in a function to not be able to put them on positions A1-H1 OR A8-H8
        :param position_king:
        :param position_pawn:
        :return: check to see if we have chess
        we can simply use same logic as diagonal_check
        '''
        if position_king - position_pawn == 7 and ((
                                                           position_king in constans_values.POSITIONS_BLACK and position_pawn in constans_values.POSITIONS_BLACK) or (
                                                           position_king in constans_values.POSITIONS_WHITE and position_pawn in constans_values.POSITIONS_WHITE)) and (
                position_king != position_pawn):
            return True
        if position_king - position_pawn == 9 and ((
                                                           position_king in constans_values.POSITIONS_BLACK and position_pawn in constans_values.POSITIONS_BLACK) or (
                                                           position_king in constans_values.POSITIONS_WHITE and position_pawn in constans_values.POSITIONS_WHITE)) and (
                position_king != position_pawn):
            return True
        return False

    def check_chess_knight(self, position_king, position_knight):
        '''
        we need to check that the differences are 6 or 10 / 15 or 17
        :param position_king:
        :param position_knight:
        :return:check if it is chess
        '''
        if abs(position_king - position_knight) == 6 or abs(position_king - position_knight) == 10 or abs(
                position_king - position_knight) == 15 or abs(
            position_king - position_knight) == 17 and position_king != position_knight:
            return True
        return False

    @staticmethod
    def check_higher(a, b):
        if a > b:
            return a - b
        else:
            return b - a

    @staticmethod
    def check_same_colour(pos_queen, pos_king):
        if pos_king % 2 == 1 and pos_queen % 2 == 1:
            return True
        if pos_queen % 2 == 0 and pos_queen % 2 == 0:
            return True
        return False

    @staticmethod
    def check_if_king_queen_same_row(pos_king, pos_queen):
        rows = constans_values.create_list_rows()
        for row in rows:
            if pos_queen in row and pos_king in row:
                return True
        return False

    def get_position_pieces(self, pos_queen, pos_king):
        dict_map = constans_values.create_map_positions()
        return dict_map[pos_queen], dict_map[pos_king]

    def check_chess(self, dict_pieces_positions, *args):
        is_chess_queen = False
        is_chess_rook = False
        is_chess_bishop = False
        is_chess_knight = False
        is_chess_pawn = False
        are_kings_near = False
        '''check if we have check from what pieces'''
        # 1. check queen
        for piece, value in dict_pieces_positions.items():
            if piece == constans_values.PIECES[2]:
                if self.check_chess_queen(dict_pieces_positions[constans_values.PIECES[0]],
                                          value):
                    is_chess_queen = True
                    break
        # 2. check rook
        for piece, value in dict_pieces_positions.items():
            if piece == constans_values.PIECES[3]:
                if self.check_chess_rook(dict_pieces_positions[constans_values.PIECES[0]],
                                         value):
                    is_chess_rook = True
                    break
        # 3. check bishop
        for piece, value in dict_pieces_positions.items():
            if piece == constans_values.PIECES[4]:
                if self.check_chess_bishop(dict_pieces_positions[constans_values.PIECES[0]],
                                           value):
                    is_chess_bishop = True
                    break
        # 4. check knight
        for piece, value in dict_pieces_positions.items():
            if piece == constans_values.PIECES[5]:
                if self.check_chess_knight(dict_pieces_positions[constans_values.PIECES[0]],
                                           value):
                    is_chess_knight = True
                    break
        # 5. check pawn
        for piece, value in dict_pieces_positions.items():
            if piece == constans_values.PIECES[6]:
                if self.check_chess_pawn(dict_pieces_positions[constans_values.PIECES[0]],
                                         value):
                    is_chess_pawn = True
                    break
        # 6 check kings are each other
        for piece, value in dict_pieces_positions.items():
            if piece == constans_values.PIECES[1]:
                if self.pos_checker.check_position_kings(dict_pieces_positions[constans_values.PIECES[0]],
                                                         value):
                    are_kings_near = True
                    break
        # compute method to check chess and to see if positions are not between kings (cannot happen but use this method in the check_black_king_moves)
        if is_chess_queen:
            return True, 1
        if is_chess_rook:
            return True, 2
        if is_chess_bishop:
            return True, 3
        if is_chess_knight:
            return True, 4
        if is_chess_pawn:
            return True, 5
        # should never happen - used just only we check for the king movement
        if are_kings_near:
            return True, 6
        return False, 0

    def check_black_king_moves(self, position_black_king, dict_pieces_positions, *args):
        '''
        we need to get all valid positions so we do not get a number out of bounds
        in order to appeal with the check chess method for the new position, we need to create a new dict every time in which we add the new position of the king
        :param position_black_king:
        :param dict_pieces_positions:
        :param args:
        :return: check if we run into another check by moving the king to another square when checked
        '''
        # start if king in position A1
        result = True
        if position_black_king == 1:
            # we have 3 squares in this case :b1, a2, b2
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 9)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
        elif position_black_king == 8:
            # we have 3 squares in this case :g1, h2,g2
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 7)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
        elif position_black_king == 57:
            # we have 3 squares in this case :a7, b8,b7
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 7)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
        elif position_black_king == 64:
            # we have 3 squares in this case :h7, g8,g7
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 9)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
        # check now if it is on A column
        elif position_black_king in constans_values.FIRST_COLUMN:
            '''basically we have 5 ways to go'''
            # right
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # down
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # up
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal down
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 7)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal up
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 9)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
        # check now if it is on H column
        elif position_black_king in constans_values.LAST_COLUMN:
            '''basically we have 5 ways to go'''
            # left
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # down
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # up
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal down
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 9)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal up
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 7)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
        # check now if it is on first row
        elif position_black_king in constans_values.FIRST_ROW:
            '''basically we have 5 ways to go'''
            # left
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # right
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # up
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal left
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 7)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal right
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 9)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
        elif position_black_king in constans_values.LAST_ROW:
            '''basically we have 5 ways to go'''
            # left
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # right
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # down
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal left
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 9)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal right
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 7)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
        else:
            '''all 7 squares round'''
            # left
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # right
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 1)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # down
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # up
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 8)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal right down
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 7)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal right left
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 7)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal left down
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king - 9)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
            # diagonal left up
            while constans_values.PIECES[0] in dict_pieces_positions:
                dict_pieces_positions.pop(constans_values.PIECES[0])
            dict_pieces_positions.add(constans_values.PIECES[0], position_black_king + 9)
            dict_pieces_positions.mixed()
            if not self.check_chess(dict_pieces_positions, *args)[0]:
                return False
        return result

    def check_if_mate(self, dict_pieces_positions, *args):
        '''
        :param dict_pieces_positions:
        :param args:
        :return:a number that will represent if we have mate, just check with from what piece we have check, or no check at all
        '''
        is_check, check_type = self.check_chess(dict_pieces_positions, *args)
        can_king_escape = self.check_black_king_moves(dict_pieces_positions[constans_values.PIECES[0]],
                                                      dict_pieces_positions, *args)
        # MATE
        if is_check and can_king_escape:
            return "Mate"
        elif is_check and not can_king_escape:
            if check_type == 1:
                return 1
            if check_type == 2:
                return 2
            if check_type == 3:
                return 3
            if check_type == 4:
                return 4
            if check_type == 5:
                return 5
        else:
            return 0
