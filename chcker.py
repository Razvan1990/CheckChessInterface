import constans_values


class Checker:

    def __init__(self):
        self.right_list = [1, 9, 17, 25, 33, 41, 49, 57]
        self.left_list = [x + 8 for x in self.right_list]
        self.first_row = [1, 2, 3, 4, 5, 6, 7, 8]
        self.last_row = [x + 56 for x in self.first_row]

    def check_chess(self, position_king, position_queen):
        '''vertical check'''
        c = self.check_higher(position_king, position_queen)
        if c % 8 == 0:
            return True, 0
        '''horizontal check'''
        c = self.check_higher(position_king, position_queen)
        if c <= 7:
            return True, 1
        '''diagonal check'''
        if abs(position_king - position_queen) % 7 == 0 and ((
                                                                     position_king in constans_values.POSITIONS_BLACK and position_queen in constans_values.POSITIONS_BLACK) or (
                                                                     position_king in constans_values.POSITIONS_WHITE and position_queen in constans_values.POSITIONS_WHITE)):
            return True, 2
        if abs(position_king - position_queen) % 9 == 0 and ((
                                                                     position_king in constans_values.POSITIONS_BLACK and position_queen in constans_values.POSITIONS_BLACK) or (
                                                                     position_king in constans_values.POSITIONS_WHITE and position_queen in constans_values.POSITIONS_WHITE)):
            return True, 2
        return False, 3

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


    def get_position_pieces(self, pos_queen, pos_king):
        dict_map = constans_values.create_map_positions()
        return dict_map[pos_queen], dict_map[pos_king]
