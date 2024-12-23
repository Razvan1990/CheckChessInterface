POSITIONS_WHITE = [1, 3, 5, 7, 10, 12, 14, 16, 17, 19, 21, 23, 26, 28, 30, 32, 33, 35, 37, 39, 42, 44, 46, 48, 49, 51,
                   53, 55, 58, 60, 62, 64]
POSITIONS_BLACK = [2, 4, 6, 8, 9, 11, 13, 15, 18, 20, 22, 24, 25, 27, 29, 31, 34, 36, 38, 40, 41, 43, 45, 47, 50, 52,
                   54, 56, 57, 59, 61, 63]
COLUMNS = ["A", "B", "C", "D", "E", "F", "G", "H"]
TYPE_CHECKS = {0: "Vertical Check", 1: "Horizontal Check", 2: "Diagonal Check", 3: "NO CHECK"}


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
