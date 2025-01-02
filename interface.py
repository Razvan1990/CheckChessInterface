import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import constans_values
from paste.util.multidict import MultiDict
from chcker import Checker
from checker_positions import CheckPiecePositions

'''
#This is derived from the CheckChessInterface project and updated to check mate
#Featues have been added in other files - all are referenced in the respective files
'''


class InterfaceSetup(object):

    def __init__(self):
        self.checker = Checker()
        self.pos_checker = CheckPiecePositions()
        self.folder = r"G:\pycharm\pythonProject\CheckChessInterfac\images"
        self.dict_squares = {}
        self.list_stored_pieces = []
        self.list_stored_entries = []
        self.list_stored_chess_positions = []
        self.total_entries = []
        self.dict_pieces_positions = MultiDict()

    def insert_piece(self, piece_type, ):
        '''
        :param piece_type:
        :return: insert the piece on the correct square based on what we choose
        '''
        table_to_position_dict = constans_values.create_position_to_number_map()
        # first we will enable the button for mate if we have 2 pieces at least
        if len(self.list_stored_chess_positions) >= 2:
            button_check_mate["state"] = tkinter.NORMAL
        table_position = askstring("POSITION PIECE", "Insert the position for {}".format(piece_type)).upper()
        # 1. First check is to see if we inserted a correct position
        if table_position.upper() not in table_to_position_dict:
            messagebox.showerror("INVALID POSITION", "Please select a chess position :A1->H1", )
            return
        position_piece = table_to_position_dict[table_position]
        # 2 check if the square is not occupied
        if self.pos_checker.check_position_free(table_position, self.list_stored_chess_positions):
            messagebox.showerror("POSITION ALREADY TAKEN", "Please select a free position", )
            return
        # 3. Third check is to see if the black king is already there - it must be there as it is the only button active
        if piece_type != constans_values.PIECES[0]:
            if len(self.list_stored_pieces) == 0:
                messagebox.showinfo("BLACK KING MISSING", "The black king has not been selected", )
                return
        else:
            # put the black king and enable everything
            self.list_stored_pieces.append(constans_values.PIECES[0])
            self.list_stored_chess_positions.append(table_position.upper())
            # now we can enable all buttons
            button_insert_white_king["state"] = tkinter.NORMAL
            button_insert_queen["state"] = tkinter.NORMAL
            button_insert_rook["state"] = tkinter.NORMAL
            button_insert_bishop["state"] = tkinter.NORMAL
            button_insert_knight["state"] = tkinter.NORMAL
            button_insert_pawn["state"] = tkinter.NORMAL
            button_insert_black_king["state"] = tkinter.DISABLED
            # add in the multidict the black king position to start
            self.dict_pieces_positions.add(constans_values.PIECES[0], position_piece)
            # add in the respective entry the black king
            for entry in self.dict_squares:
                if self.dict_squares[entry] == position_piece:
                    entry.delete(0, "end")
                    entry.insert(0, "BK")
                    self.list_stored_entries.append(entry)
                    break
        '''custom checks for every piece'''
        # A. white king
        if piece_type == constans_values.PIECES[1]:
            # a. check to not have 2 white kings
            if constans_values.PIECES[1] in self.list_stored_pieces:
                messagebox.showerror("KING PRESENT", "The white king is already on the table!", )
                return
            are_kings_near = self.pos_checker.check_position_kings(
                self.dict_pieces_positions.getone(constans_values.PIECES[0]), position_piece)
            if are_kings_near:
                messagebox.showinfo("KINGS ARE ON NEIGHBOUR SQUARES", "Kings cannot be on neighbour squares", )
                return
            self.list_stored_pieces.append(constans_values.PIECES[1])
            self.list_stored_chess_positions.append(table_position.upper())
            self.dict_pieces_positions.add(constans_values.PIECES[1], position_piece)
            for entry in self.dict_squares:
                if self.dict_squares[entry] == position_piece:
                    entry.delete(0, "end")
                    entry.insert(0, "WK")
                    entry["fg"] = "#d9e1e1"
                    self.list_stored_entries.append(entry)
                    break
        # B bishops
        elif piece_type == constans_values.PIECES[4]:
            # check to see if we don't have more than 2 bishops
            counter_bishops = 0
            for piece in self.list_stored_pieces:
                if piece == constans_values.PIECES[4]:
                    counter_bishops += 1
            if counter_bishops >= 2:
                messagebox.showerror("BISHOPS ALREADY PRESENT", "There are already 2 bishops on the board!", )
                return
            if constans_values.PIECES[4] in self.list_stored_pieces:
                are_bishops_on_same_colour = self.pos_checker.check_positions_bishops(
                    self.dict_pieces_positions.getone(constans_values.PIECES[4]), position_piece)
                if are_bishops_on_same_colour:
                    messagebox.showinfo("BISHOPS ON SAME COLOUR", "Bishops cannot be on the same colour", )
                    return
            self.list_stored_pieces.append(constans_values.PIECES[4])
            self.list_stored_chess_positions.append(table_position.upper())
            self.dict_pieces_positions.add(constans_values.PIECES[4], position_piece)
            for entry in self.dict_squares:
                if self.dict_squares[entry] == position_piece:
                    entry.delete(0, "end")
                    entry.insert(0, "b")
                    entry["fg"] = "#d9e1e1"
                    self.list_stored_entries.append(entry)
                    break
        # PAWNS
        elif piece_type == constans_values.PIECES[6]:
            # check if pawns are not on first and last row
            if self.pos_checker.check_position_pawn(position_piece):
                messagebox.showinfo("PAWNS NOT CORRECT VALUES", "Pawns cannot be positioned on the first or last row", )
                return
            # check if we don't have more than 8 pawns - kind of silly check :)
            counter_pawns = 0
            for piece in self.list_stored_pieces:
                if piece == constans_values.PIECES[6]:
                    counter_pawns += 1
            if counter_pawns == 8:
                messagebox.showerror("TOO MANY PAWNS", "There are already 8 pawns on the board!", )
                return
            self.list_stored_pieces.append(constans_values.PIECES[6])
            self.list_stored_chess_positions.append(table_position.upper())
            self.dict_pieces_positions.add(constans_values.PIECES[6], position_piece)
            for entry in self.dict_squares:
                if self.dict_squares[entry] == position_piece:
                    entry.delete(0, "end")
                    entry.insert(0, "p")
                    entry["fg"] = "#d9e1e1"
                    self.list_stored_entries.append(entry)
                    break
        # knights, rooks, queens
        # we do not need any conditions for them
        elif piece_type == constans_values.PIECES[2]:
            self.list_stored_pieces.append(constans_values.PIECES[2])
            self.list_stored_chess_positions.append(table_position.upper())
            self.dict_pieces_positions.add(constans_values.PIECES[2], position_piece)
            for entry in self.dict_squares:
                if self.dict_squares[entry] == position_piece:
                    entry.delete(0, "end")
                    entry.insert(0, "Q")
                    entry["fg"] = "#d9e1e1"
                    self.list_stored_entries.append(entry)
                    break
        elif piece_type == constans_values.PIECES[3]:
            self.list_stored_pieces.append(constans_values.PIECES[3])
            self.list_stored_chess_positions.append(table_position.upper())
            self.dict_pieces_positions.add(constans_values.PIECES[3], position_piece)
            for entry in self.dict_squares:
                if self.dict_squares[entry] == position_piece:
                    entry.delete(0, "end")
                    entry.insert(0, "r")
                    entry["fg"] = "#d9e1e1"
                    self.list_stored_entries.append(entry)
                    break
        elif piece_type == constans_values.PIECES[5]:
            self.list_stored_pieces.append(constans_values.PIECES[5])
            self.list_stored_chess_positions.append(table_position.upper())
            self.dict_pieces_positions.add(constans_values.PIECES[5], position_piece)
            for entry in self.dict_squares:
                if self.dict_squares[entry] == position_piece:
                    entry.delete(0, "end")
                    entry.insert(0, "k")
                    entry["fg"] = "#d9e1e1"
                    self.list_stored_entries.append(entry)
                    break
        #check and debug purposes
        print(self.list_stored_entries)
        print(self.list_stored_pieces)
        print(self.list_stored_chess_positions)
        print(self.dict_pieces_positions)

    def check_mate(self):
        '''
        we do not need any parameters as all relevant stuff needed is in the multidict
        :return:if it is check mate or just check or no check at all
        '''
        is_mate = self.checker.check_if_mate(self.dict_pieces_positions)
        # disable now all the buttons
        button_insert_white_king["state"] = tkinter.DISABLED
        button_insert_queen["state"] = tkinter.DISABLED
        button_insert_rook["state"] = tkinter.DISABLED
        button_insert_bishop["state"] = tkinter.DISABLED
        button_insert_knight["state"] = tkinter.DISABLED
        button_insert_pawn["state"] = tkinter.DISABLED
        button_insert_black_king["state"] = tkinter.DISABLED
        # disable empty squares
        for i in range(0, len(self.total_entries)):
            if self.total_entries[i] not in self.list_stored_entries:
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
        if is_mate == "Mate":
            label_check["text"] = "IT IS CHECK MATE"
            label_check["fg"] = "#176e2c"
            button_check_mate["state"] = tkinter.DISABLED
            return
        '''just check now'''
        if is_mate == 1:
            label_check["text"] = "IT IS JUST CHECK FROM THE {}".format(constans_values.PIECES[2])
            label_check["fg"] = "#e2b441"
            button_check_mate["state"] = tkinter.DISABLED
            return
        elif is_mate == 2:
            label_check["text"] = "IT IS JUST CHECK FROM THE {}".format(constans_values.PIECES[3])
            label_check["fg"] = "#e2b441"
            button_check_mate["state"] = tkinter.DISABLED
            return
        elif is_mate == 3:
            label_check["text"] = "IT IS JUST CHECK FROM THE {}".format(constans_values.PIECES[4])
            label_check["fg"] = "#e2b441"
            button_check_mate["state"] = tkinter.DISABLED
            return
        elif is_mate == 4:
            label_check["text"] = "IT IS JUST CHECK FROM THE {}".format(constans_values.PIECES[5])
            label_check["fg"] = "#e2b441"
            button_check_mate["state"] = tkinter.DISABLED
            return
        elif is_mate == 5:
            label_check["text"] = "IT IS JUST CHECK FROM THE {}".format(constans_values.PIECES[6])
            label_check["fg"] = "#e2b441"
            button_check_mate["state"] = tkinter.DISABLED
            return
        elif is_mate == 0:
            label_check["text"] = "False alarm! NO CHECK"
            label_check["fg"] = "#e13e0e"
            button_check_mate["state"] = tkinter.DISABLED
            return

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
        global button_insert_black_king
        global button_insert_white_king
        global button_insert_queen
        global button_insert_rook
        global button_insert_bishop
        global button_insert_knight
        global button_insert_pawn
        global button_check_mate

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

        '''Create buttons for the pieces'''
        # black king
        button_insert_black_king = Button(window, text="INSERT BLACK KING", width=18, height=2, fg="#1c0803",
                                          bg="#df2250",
                                          font=("Helvetica", 12, "bold"),
                                          command=lambda: self.insert_piece(constans_values.PIECES[0]))
        # white king
        button_insert_white_king = Button(window, text="INSERT WHITE KING", width=18, height=2, fg="#fffefb",
                                          bg="#8ff436",
                                          font=("Helvetica", 12, "bold"),
                                          command=lambda: self.insert_piece(constans_values.PIECES[1]))
        button_insert_white_king["state"] = tkinter.DISABLED
        # queen
        button_insert_queen = Button(window, text="INSERT QUEEN", width=18, height=2, fg="#fffefb", bg="#7eb2a9",
                                     font=("Helvetica", 12, "bold"),
                                     command=lambda: self.insert_piece(constans_values.PIECES[2]))
        button_insert_queen["state"] = tkinter.DISABLED
        # rook
        button_insert_rook = Button(window, text="INSERT ROOK ", width=18, height=2, fg="#fffefb", bg="#2d496b",
                                    font=("Helvetica", 12, "bold"),
                                    command=lambda: self.insert_piece(constans_values.PIECES[3]))
        button_insert_rook["state"] = tkinter.DISABLED
        # bishop
        button_insert_bishop = Button(window, text="INSERT BISHOP", width=18, height=2, fg="#fffefb", bg="#76258e",
                                      font=("Helvetica", 12, "bold"),
                                      command=lambda: self.insert_piece(constans_values.PIECES[4]))
        button_insert_bishop["state"] = tkinter.DISABLED
        # knight
        button_insert_knight = Button(window, text="INSERT KNIGHT", width=18, height=2, fg="#fffefb", bg="#caab0d",
                                      font=("Helvetica", 12, "bold"),
                                      command=lambda: self.insert_piece(constans_values.PIECES[5]))
        button_insert_knight["state"] = tkinter.DISABLED
        # pawn
        button_insert_pawn = Button(window, text="INSERT PAWN", width=18, height=2, fg="#fffefb", bg="#5a5850",
                                    font=("Helvetica", 12, "bold"),
                                    command=lambda: self.insert_piece(constans_values.PIECES[6]))
        button_insert_pawn["state"] = tkinter.DISABLED
        # put them on the screen
        button_insert_black_king.place(x=50, y=200)
        button_insert_white_king.place(x=50, y=275)
        button_insert_queen.place(x=250, y=275)
        button_insert_rook.place(x=450, y=275)
        button_insert_bishop.place(x=650, y=275)
        button_insert_knight.place(x=850, y=275)
        button_insert_pawn.place(x=1050, y=275)

        button_check_mate = Button(window, text="CHECK MATE", width=13, height=2, fg="#0f1010", bg="#55f9bb",
                                   font=("Helvetica", 14, "bold"), bd=5, highlightbackground="#1d607b",
                                   highlightthickness=2,
                                   command=lambda: self.check_mate())
        button_check_mate["state"] = tkinter.DISABLED
        button_check_mate.place(x=920, y=400)

        '''Create label where we will put the result'''
        label_check = Label(window, fg="#d61515", bg="#55f9bb", font=("Comic Sans", 14, "bold"), bd=4, width=40,
                            justify="center", text="")
        label_check.place(x=800, y=550)

    def create_main_gui(self):
        root = Tk()
        root.geometry("1280x960")
        root.title("ChessCheck")
        root.iconbitmap(os.path.join(self.folder, "chess.ico"))
        root["bg"] = "#55f9bb"
        self.create_game(root)
        root.mainloop()
