import constans_values
from paste.util.multidict import MultiDict
from interface import InterfaceSetup
from chcker import Checker


def run_program():
    # interface = InterfaceSetup()
    # interface.create_main_gui()
    checker = Checker()
    print(constans_values.create_position_to_number_map())
    dict_test = MultiDict()
    dict_test.add( constans_values.PIECES[0], 33)
    dict_test.add(constans_values.PIECES[2], 57)
    dict_test.add(constans_values.PIECES[2], 42)
    dict_test.mixed()
    for piece, value in dict_test.items():
        print(piece, value)


    # dict_test = \
    #     {
    #         constans_values.PIECES[0]: 46,
    #         constans_values.PIECES[1]: 62,
    #         constans_values.PIECES[2]: 29,
    #         constans_values.PIECES[6]: 20
    #     }
    result = checker.check_if_mate(dict_test)
    print(result)


if __name__ == "__main__":
    run_program()
