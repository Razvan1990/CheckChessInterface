import os
import tkinter
from tkinter import *

import constans_values
from chcker import Checker

'''
#This is derived from the CheckChessInterface project and updated to check mate
#Featues have been added in other files - all are referenced in the respective files
'''


class InterfaceSetup(object):

    def __init__(self):
        self.checker = Checker()
        self.folder = r"G:\pycharm\pythonProject\CheckChessInterfac\images"
        self.dict_squares = {}
        self.list_stored_pieces = []
        self.total_entries = []

    def insert_piece(self, entry, *args):
        if len(self.list_stored_pieces) % 2 == 0:
            print(entry)
            entry.delete(0, "end")
            entry.insert(0, "K")
            self.list_stored_pieces.append(entry)
            print(self.list_stored_pieces[0]["text"])
        elif len(self.list_stored_pieces) % 2 == 1 and self.list_stored_pieces[0]["text"] == "":
            entry.delete(0, "end")
            entry.insert(0, "Q")
            self.list_stored_pieces.append(entry)
        # start checking if we have 2 values in list
        if len(self.list_stored_pieces) == 2:
            '''now we start the process'''
            # 1.Enable the button for checking
            button_check_chess["state"] = tkinter.NORMAL
            # 2. Disable all the other buttons
            for i in range(0, len(self.total_entries)):
                if self.total_entries[i] not in self.list_stored_pieces:
                    # make logic per row
                    if 0 <= i <= 7:
                        if i % 2 == 0:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#eef7d8")
                        else:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#7d7861")
                    if 8 <= i <= 15:
                        if i % 2 == 0:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#7d7861")
                        else:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#eef7d8")
                    if 16 <= i <= 23:
                        if i % 2 == 0:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#eef7d8")
                        else:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#7d7861")
                    if 24 <= i <= 31:
                        if i % 2 == 0:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#7d7861")
                        else:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#eef7d8")
                    if 32 <= i <= 39:
                        if i % 2 == 0:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#eef7d8")
                        else:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#7d7861")
                    if 40 <= i <= 47:
                        if i % 2 == 0:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#7d7861")
                        else:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#eef7d8")
                    if 48 <= i <= 55:
                        if i % 2 == 0:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#eef7d8")
                        else:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#7d7861")
                    if 56 <= i <= 63:
                        if i % 2 == 0:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#7d7861")
                        else:
                            self.total_entries[i].configure(state=tkinter.DISABLED, disabledbackground="#eef7d8")

    def check_chess(self, position_king, position_queen):
        result = self.checker.check_chess_queen(position_king, position_queen)
        map_positions_queen, map_position_king = self.checker.get_position_pieces(
            position_queen, position_king)
        '''Make label for chess and type of chess'''
        if result:
            label_check["text"] = "{} from QUEEN on {} to KING on {}".format(constans_values.TYPE_CHECKS[type_chess],
                                                                             map_positions_queen, map_position_king)
            label_check["fg"] = "#176e2c"
            button_check_chess["state"] = tkinter.DISABLED
        else:
            label_check["text"] = "False alarm! {}".format(constans_values.TYPE_CHECKS[3])
            label_check["fg"] = "#e13e0e"
            button_check_chess["state"] = tkinter.DISABLED

    def create_game(self, window):
        '''
        :param window:
        :return:the board game
        '''

        '''FIrst we will create 63 global entries for every square'''
        # A
        global squareA1
        global squareA2
        global squareA3
        global squareA4
        global squareA5
        global squareA6
        global squareA7
        global squareA8

        # B
        global squareB1
        global squareB2
        global squareB3
        global squareB4
        global squareB5
        global squareB6
        global squareB7
        global squareB8

        # C
        global squareC1
        global squareC2
        global squareC3
        global squareC4
        global squareC5
        global squareC6
        global squareC7
        global squareC8

        # D
        global squareD1
        global squareD2
        global squareD3
        global squareD4
        global squareD5
        global squareD6
        global squareD7
        global squareD8

        # E
        global squareE1
        global squareE2
        global squareE3
        global squareE4
        global squareE5
        global squareE6
        global squareE7
        global squareE8

        # F
        global squareF1
        global squareF2
        global squareF3
        global squareF4
        global squareF5
        global squareF6
        global squareF7
        global squareF8

        # G
        global squareG1
        global squareG2
        global squareG3
        global squareG4
        global squareG5
        global squareG6
        global squareG7
        global squareG8

        # H
        global squareH1
        global squareH2
        global squareH3
        global squareH4
        global squareH5
        global squareH6
        global squareH7
        global squareH8

        global label_check
        global button_check_chess

        # we use this to keep and to store where x is marked
        result_square = StringVar()
        '''Create entries'''
        list_squares_row1 = list()
        squareA1 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row1.append(squareA1)
        squareB1 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row1.append(squareB1)
        squareC1 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row1.append(squareC1)
        squareD1 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row1.append(squareD1)
        squareE1 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row1.append(squareE1)
        squareF1 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row1.append(squareF1)
        squareG1 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row1.append(squareG1)
        squareH1 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row1.append(squareH1)
        x_start = 150
        y_start = 700
        offset = 0
        for square in list_squares_row1:
            square.place(x=x_start + offset, y=y_start)
            offset += 75

        list_squares_row2 = list()
        squareA2 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row2.append(squareA2)
        squareB2 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row2.append(squareB2)
        squareC2 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row2.append(squareC2)
        squareD2 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row2.append(squareD2)
        squareE2 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row2.append(squareE2)
        squareF2 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row2.append(squareF2)
        squareG2 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row2.append(squareG2)
        squareH2 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row2.append(squareH2)
        x_start = 150
        y_start = 650
        offset = 0
        for square in list_squares_row2:
            square.place(x=x_start + offset, y=y_start)
            offset += 75

        list_squares_row3 = list()
        squareA3 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row3.append(squareA3)
        squareB3 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row3.append(squareB3)
        squareC3 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row3.append(squareC3)
        squareD3 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row3.append(squareD3)
        squareE3 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row3.append(squareE3)
        squareF3 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row3.append(squareF3)
        squareG3 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row3.append(squareG3)
        squareH3 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row3.append(squareH3)
        x_start = 150
        y_start = 600
        offset = 0
        for square in list_squares_row3:
            square.place(x=x_start + offset, y=y_start)
            offset += 75

        list_squares_row4 = list()
        squareA4 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row4.append(squareA4)
        squareB4 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row4.append(squareB4)
        squareC4 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row4.append(squareC4)
        squareD4 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row4.append(squareD4)
        squareE4 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row4.append(squareE4)
        squareF4 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row4.append(squareF4)
        squareG4 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row4.append(squareG4)
        squareH4 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row4.append(squareH4)
        x_start = 150
        y_start = 550
        offset = 0
        for square in list_squares_row4:
            square.place(x=x_start + offset, y=y_start)
            offset += 75

        list_squares_row5 = list()
        squareA5 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row5.append(squareA5)
        squareB5 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row5.append(squareB5)
        squareC5 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row5.append(squareC5)
        squareD5 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row5.append(squareD5)
        squareE5 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row5.append(squareE5)
        squareF5 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row5.append(squareF5)
        squareG5 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row5.append(squareG5)
        squareH5 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row5.append(squareH5)
        x_start = 150
        y_start = 500
        offset = 0
        for square in list_squares_row5:
            square.place(x=x_start + offset, y=y_start)
            offset += 75

        list_squares_row6 = list()
        squareA6 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row6.append(squareA6)
        squareB6 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row6.append(squareB6)
        squareC6 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row6.append(squareC6)
        squareD6 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row6.append(squareD6)
        squareE6 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row6.append(squareE6)
        squareF6 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row6.append(squareF6)
        squareG6 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row6.append(squareG6)
        squareH6 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row6.append(squareH6)
        x_start = 150
        y_start = 450
        offset = 0
        for square in list_squares_row6:
            square.place(x=x_start + offset, y=y_start)
            offset += 75

        list_squares_row7 = list()
        squareA7 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row7.append(squareA7)
        squareB7 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row7.append(squareB7)
        squareC7 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row7.append(squareC7)
        squareD7 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row7.append(squareD7)
        squareE7 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row7.append(squareE7)
        squareF7 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row7.append(squareF7)
        squareG7 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row7.append(squareG7)
        squareH7 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row7.append(squareH7)
        x_start = 150
        y_start = 400
        offset = 0
        for square in list_squares_row7:
            square.place(x=x_start + offset, y=y_start)
            offset += 75

        list_squares_row8 = list()
        squareA8 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row8.append(squareA8)
        squareB8 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row8.append(squareB8)
        squareC8 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row8.append(squareC8)
        squareD8 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row8.append(squareD8)
        squareE8 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row8.append(squareE8)
        squareF8 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row8.append(squareF8)
        squareG8 = Entry(window, fg="#313528", bg="#7d7861", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row8.append(squareG8)
        squareH8 = Entry(window, fg="#313528", bg="#eef7d8", font=("Comic Sans", 28, "bold"), bd=5,
                         cursor="dotbox", width=3, justify="center", )
        list_squares_row8.append(squareH8)
        x_start = 150
        y_start = 350
        offset = 0
        for square in list_squares_row8:
            square.place(x=x_start + offset, y=y_start)
            offset += 75
        # create dictionary of entries
        for index, entry in enumerate(list_squares_row1, start=1):
            self.dict_squares.update({entry: index})
            self.total_entries.append(entry)
        for index, entry in enumerate(list_squares_row2, start=9):
            self.dict_squares.update({entry: index})
            self.total_entries.append(entry)
        for index, entry in enumerate(list_squares_row3, start=17):
            self.dict_squares.update({entry: index})
            self.total_entries.append(entry)
        for index, entry in enumerate(list_squares_row4, start=25):
            self.dict_squares.update({entry: index})
            self.total_entries.append(entry)
        for index, entry in enumerate(list_squares_row5, start=33):
            self.dict_squares.update({entry: index})
            self.total_entries.append(entry)
        for index, entry in enumerate(list_squares_row6, start=41):
            self.dict_squares.update({entry: index})
            self.total_entries.append(entry)
        for index, entry in enumerate(list_squares_row7, start=49):
            self.dict_squares.update({entry: index})
            self.total_entries.append(entry)
        for index, entry in enumerate(list_squares_row8, start=57):
            self.dict_squares.update({entry: index})
            self.total_entries.append(entry)
        '''Create a chess title label'''

        label_title = Label(window, fg="#2130c8", bg="#55f9bb", font=("Comic Sans", 30, "bold"), bd=10,
                            cursor="spraycan", width=25, justify="center", text="CHECK CHESS PROGRAM")
        label_title.place(x=300, y=100)

        '''Create button to check chess'''
        button_check_chess = Button(window, text="CHECK CHESS", width=13, height=2, fg="#e5ff3d", bg="#126bad",
                                    font=("Helvetica", 14, "bold"),
                                    command=lambda: self.check_chess(self.dict_squares[self.list_stored_pieces[0]],
                                                                     self.dict_squares[self.list_stored_pieces[1]]))
        # command=self.get_actual_weather))
        button_check_chess["state"] = tkinter.DISABLED
        button_check_chess.place(x=920, y=350)

        '''Create label where we will put the result'''
        label_check = Label(window, fg="#d61515", bg="#55f9bb", font=("Comic Sans", 14, "bold"), bd=4, width=40,
                            justify="center", text="")
        label_check.place(x=800, y=500)

        '''Make the bindings now'''
        # result square is not necessary
        squareA1.bind("<1>", lambda event, entry=squareA1: self.insert_piece(entry,
                                                                             result_square))
        squareA2.bind("<1>", lambda event, entry=squareA2: self.insert_piece(entry,
                                                                             result_square))
        squareA3.bind("<1>", lambda event, entry=squareA3: self.insert_piece(entry,
                                                                             result_square))
        squareA4.bind("<1>", lambda event, entry=squareA4: self.insert_piece(entry,
                                                                             result_square))
        squareA5.bind("<1>", lambda event, entry=squareA5: self.insert_piece(entry,
                                                                             result_square))
        squareA6.bind("<1>", lambda event, entry=squareA6: self.insert_piece(entry,
                                                                             result_square))
        squareA7.bind("<1>", lambda event, entry=squareA7: self.insert_piece(entry,
                                                                             result_square))
        squareA8.bind("<1>", lambda event, entry=squareA8: self.insert_piece(entry,
                                                                             result_square))

        squareB1.bind("<1>", lambda event, entry=squareB1: self.insert_piece(entry,
                                                                             result_square))
        squareB2.bind("<1>", lambda event, entry=squareB2: self.insert_piece(entry,
                                                                             result_square))
        squareB3.bind("<1>", lambda event, entry=squareB3: self.insert_piece(entry,
                                                                             result_square))
        squareB4.bind("<1>", lambda event, entry=squareB4: self.insert_piece(entry,
                                                                             result_square))
        squareB5.bind("<1>", lambda event, entry=squareB5: self.insert_piece(entry,
                                                                             result_square))
        squareB6.bind("<1>", lambda event, entry=squareB6: self.insert_piece(entry,
                                                                             result_square))
        squareB7.bind("<1>", lambda event, entry=squareB7: self.insert_piece(entry,
                                                                             result_square))
        squareB8.bind("<1>", lambda event, entry=squareB8: self.insert_piece(entry,
                                                                             result_square))

        squareC1.bind("<1>", lambda event, entry=squareC1: self.insert_piece(entry,
                                                                             result_square))
        squareC2.bind("<1>", lambda event, entry=squareC2: self.insert_piece(entry,
                                                                             result_square))
        squareC3.bind("<1>", lambda event, entry=squareC3: self.insert_piece(entry,
                                                                             result_square))
        squareC4.bind("<1>", lambda event, entry=squareC4: self.insert_piece(entry,
                                                                             result_square))
        squareC5.bind("<1>", lambda event, entry=squareC5: self.insert_piece(entry,
                                                                             result_square))
        squareC6.bind("<1>", lambda event, entry=squareC6: self.insert_piece(entry,
                                                                             result_square))
        squareC7.bind("<1>", lambda event, entry=squareC7: self.insert_piece(entry,
                                                                             result_square))
        squareC8.bind("<1>", lambda event, entry=squareC8: self.insert_piece(entry,
                                                                             result_square))

        squareD1.bind("<1>", lambda event, entry=squareD1: self.insert_piece(entry,
                                                                             result_square))
        squareD2.bind("<1>", lambda event, entry=squareD2: self.insert_piece(entry,
                                                                             result_square))
        squareD3.bind("<1>", lambda event, entry=squareD3: self.insert_piece(entry,
                                                                             result_square))
        squareD4.bind("<1>", lambda event, entry=squareD4: self.insert_piece(entry,
                                                                             result_square))
        squareD5.bind("<1>", lambda event, entry=squareD5: self.insert_piece(entry,
                                                                             result_square))
        squareD6.bind("<1>", lambda event, entry=squareD6: self.insert_piece(entry,
                                                                             result_square))
        squareD7.bind("<1>", lambda event, entry=squareD7: self.insert_piece(entry,
                                                                             result_square))
        squareD8.bind("<1>", lambda event, entry=squareD8: self.insert_piece(entry,
                                                                             result_square))

        squareE1.bind("<1>", lambda event, entry=squareE1: self.insert_piece(entry,
                                                                             result_square))
        squareE2.bind("<1>", lambda event, entry=squareE2: self.insert_piece(entry,
                                                                             result_square))
        squareE3.bind("<1>", lambda event, entry=squareE3: self.insert_piece(entry,
                                                                             result_square))
        squareE4.bind("<1>", lambda event, entry=squareE4: self.insert_piece(entry,
                                                                             result_square))
        squareE5.bind("<1>", lambda event, entry=squareE5: self.insert_piece(entry,
                                                                             result_square))
        squareE6.bind("<1>", lambda event, entry=squareE6: self.insert_piece(entry,
                                                                             result_square))
        squareE7.bind("<1>", lambda event, entry=squareE7: self.insert_piece(entry,
                                                                             result_square))
        squareE8.bind("<1>", lambda event, entry=squareE8: self.insert_piece(entry,
                                                                             result_square))

        squareF1.bind("<1>", lambda event, entry=squareF1: self.insert_piece(entry,
                                                                             result_square))
        squareF2.bind("<1>", lambda event, entry=squareF2: self.insert_piece(entry,
                                                                             result_square))
        squareF3.bind("<1>", lambda event, entry=squareF3: self.insert_piece(entry,
                                                                             result_square))
        squareF4.bind("<1>", lambda event, entry=squareF4: self.insert_piece(entry,
                                                                             result_square))
        squareF5.bind("<1>", lambda event, entry=squareF5: self.insert_piece(entry,
                                                                             result_square))
        squareF6.bind("<1>", lambda event, entry=squareF6: self.insert_piece(entry,
                                                                             result_square))
        squareF7.bind("<1>", lambda event, entry=squareF7: self.insert_piece(entry,
                                                                             result_square))
        squareF8.bind("<1>", lambda event, entry=squareF8: self.insert_piece(entry,
                                                                             result_square))

        squareG1.bind("<1>", lambda event, entry=squareG1: self.insert_piece(entry,
                                                                             result_square))
        squareG2.bind("<1>", lambda event, entry=squareG2: self.insert_piece(entry,
                                                                             result_square))
        squareG3.bind("<1>", lambda event, entry=squareG3: self.insert_piece(entry,
                                                                             result_square))
        squareG4.bind("<1>", lambda event, entry=squareG4: self.insert_piece(entry,
                                                                             result_square))
        squareG5.bind("<1>", lambda event, entry=squareG5: self.insert_piece(entry,
                                                                             result_square))
        squareG6.bind("<1>", lambda event, entry=squareG6: self.insert_piece(entry,
                                                                             result_square))
        squareG7.bind("<1>", lambda event, entry=squareG7: self.insert_piece(entry,
                                                                             result_square))
        squareG8.bind("<1>", lambda event, entry=squareG8: self.insert_piece(entry,
                                                                             result_square))

        squareH1.bind("<1>", lambda event, entry=squareH1: self.insert_piece(entry,
                                                                             result_square))
        squareH2.bind("<1>", lambda event, entry=squareH2: self.insert_piece(entry,
                                                                             result_square))
        squareH3.bind("<1>", lambda event, entry=squareH3: self.insert_piece(entry,
                                                                             result_square))
        squareH4.bind("<1>", lambda event, entry=squareH4: self.insert_piece(entry,
                                                                             result_square))
        squareH5.bind("<1>", lambda event, entry=squareH5: self.insert_piece(entry,
                                                                             result_square))
        squareH6.bind("<1>", lambda event, entry=squareH6: self.insert_piece(entry,
                                                                             result_square))
        squareH7.bind("<1>", lambda event, entry=squareH7: self.insert_piece(entry,
                                                                             result_square))
        squareH8.bind("<1>", lambda event, entry=squareH8: self.insert_piece(entry,
                                                                             result_square))

    def create_main_gui(self):
        root = Tk()
        root.geometry("1280x960")
        root.title("ChessCheck")
        root.iconbitmap(os.path.join(self.folder, "chess.ico"))
        root["bg"] = "#55f9bb"
        self.create_game(root)
        root.mainloop()
