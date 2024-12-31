import constans_values


class CheckPiecePositions(object):

    def check_position_kings(self, position_black_king, position_white_king):
        '''
        Basically, we need to check every neighbour square
        :param position_black_king:
        :param position_white_king:
        :return: if the kings are on adjacent squares or not
        '''
        # 1= horizontal
        # 8 =vertical
        # 7 and 9 = diagonal
        if abs(position_black_king - position_white_king) == 1 or \
                abs(position_black_king - position_white_king) == 8 or \
                abs(position_black_king - position_white_king) == 7 or \
                abs(position_black_king - position_white_king) == 9:
            return True
        return False

    def check_positions_bishops(self, pos_bishop_white, pos_bishop_black):
        # check to see if there is a WHITE bishop and not put the black bishop on a white square
        if pos_bishop_white in constans_values.POSITIONS_WHITE and pos_bishop_black in constans_values.POSITIONS_WHITE:
            return True
        # check to see if there is a BLACK bishop and not put the WHITE bishop on a black square
        if pos_bishop_black in constans_values.POSITIONS_BLACK and pos_bishop_white in constans_values.POSITIONS_BLACK:
            return True
        return False

    def check_position_free(self, position_piece, list_pieces):
        if position_piece in list_pieces:
            return True
        return False




