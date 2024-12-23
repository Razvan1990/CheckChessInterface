from interface import InterfaceSetup


def run_program():
    interface = InterfaceSetup()
    # position_king = int(input("Position king "))
    # position_queen = int(input("Position queen "))
    # print(checker.check_chess(position_queen, position_king))
    # pos_queen = checker.get_position_pieces(position_queen, position_king)[0]
    # print(pos_queen)
    # pos_king = checker.get_position_pieces(position_queen, position_king)[1]
    # print(pos_king)
    interface.create_main_gui()


if __name__ == "__main__":
    run_program()
