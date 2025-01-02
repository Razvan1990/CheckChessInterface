# difference from check chess interface is that here we have all the pieces
POSITIONS_WHITE = [1, 3, 5, 7, 10, 12, 14, 16, 17, 19, 21, 23, 26, 28, 30, 32, 33, 35, 37, 39, 42, 44, 46, 48, 49, 51,
                   53, 55, 58, 60, 62, 64]
POSITIONS_BLACK = [2, 4, 6, 8, 9, 11, 13, 15, 18, 20, 22, 24, 25, 27, 29, 31, 34, 36, 38, 40, 41, 43, 45, 47, 50, 52,
                   54, 56, 57, 59, 61, 63]
COLUMNS = ["A", "B", "C", "D", "E", "F", "G", "H"]
FIRST_COLUMN = [1, 9, 17, 25, 33, 41, 49, 57]
LAST_COLUMN = [x + 7 for x in FIRST_COLUMN]
FIRST_ROW = [1, 2, 3, 4, 5, 6, 7, 8]
LAST_ROW = [x + 56 for x in FIRST_ROW]
PIECES = ["BLACK KING", "WHITE KING", "QUEEN", "ROOK", "BISHOP", "KNIGHT", "PAWN"]


def create_map_positions():
    map_positions = dict()
    counter_columns = 0
    for letter in COLUMNS:
        starting_pos = 1
        for i in range(1, 9):
            map_positions.update({starting_pos + counter_columns: letter + str(i)})
            starting_pos += 8
        counter_columns += 1
    return map_positions


def create_position_to_number_map():
    '''
    This function is the inverted function for create_map_positions(),
    but we need it when we introduce the position from the interface to map to the pos and make the chess logic
    :return:map that has keys the chess positions and as values the respective numbers
    '''
    map_positions = dict()
    position = 1
    for i in range(1, 9):
        for column in COLUMNS:
            map_positions.update({column + str(i): position})
            position += 1
    return map_positions


def create_list_rows():
    list_rows = list()
    start = 1
    for row_number in range(0, 8):
        row = list()
        for i in range(start, start + 8):
            row.append(i)
        list_rows.append(row)
        start += 8
    return list_rows
