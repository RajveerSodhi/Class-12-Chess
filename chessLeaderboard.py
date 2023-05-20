import tkinter as tk, pymysql as pm
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox




connection = pm.connect(host = "localhost", user = "root", database = "chess1", password = "rajSim#1873")
cursor = connection.cursor()




windowdimensions, windowtitle = "900x750+205+15", "Rajveer's Chess Program"
landing_background, play_background, play_info_background, gamerules_background = "Papaya Whip", "Light Sky Blue", "Pink", "NavajoWhite2"
progrules_background, view_background, edit_background = "SeaGreen1", "IndianRed1", "Thistle2"
p1_name, p2_name, game_name = "", "", ""
content1 = "Putting the opponent's king in a checkmate - a position from which it is impossible to escape attack from your pieces."
content2 = '''White always moves first. Movement is required.
        With the exception of the knight, a piece may not move over any of the other pieces.
        When a king is threatened with capture (but can protect himself/escape), it´s called check.
        If a king is in check, then the player must eliminate the threat and cannot leave the king in check.
        If a player isn't under check but has no legal moves, the game is in stalemate and ends in a draw.
        Checkmate happens when a king is in check with no legal move to escape. This ends the game.'''
content3 = '''- King can move 1 vacant square in any direction. It may castle once per game.
        - Queen can move any number of vacant squares in any direction.
        - Rook can move any number of vacant squares vertically or horizontally. It also is moved while castling.
        - Bishop can move any number of vacant squares in any diagonal direction.
        - Knight can move one square along any rank/file and then 2 perpendicularly. Its movement can also be viewed as an “L”.
        - Pawns can move forward one vacant square. If not yet moved, it may move 2 vacant squares.
        It cannot move backward. It kills diagonally forward. It can also perform en passant and promotion.'''
content4 = '''- En Passant occurs when a pawn is moved 2 squares on its initial movement.
        The opponent can take the moved pawn “en passant” as if it had only moved one square.
        - If a pawn reaches the opponent's edge of the table, it  may be promoted to a queen, rook, bishop or knight.
        - During the castling, the king moves two squares towards the rook he intends to castle with,
        and the rook moves to the square through which the king passed.
        Castling is only permissible if neither king nor rook involved in castling may have
        moved from the original position and there are no pieces between the rook and king.
        The king may not currently be in check, nor may the king pass through or end up in a
        square that is under attack by an enemy piece.'''
content5 = '''- Enter coordinates of pieces by first mentioning the row and then the column (without any spaces) and press 'return'.
        Capitalisation does not matter.
        For example: 2g, 4E, 8f, 1D


        - If a player's king is under checkmate, or if he wishes to give up, he may type in "declare" where he is
        asked to enter the coordinates of the piece he wants to move, after which he must confirm his declaration once again.
        If it is withdrawn, the game will continue.


        - If you wish to go back to selecting the initial coordinates of the piece, type "back" where you are to type
        in the new coordinates.


        - If a game ends in a draw, any of the players can enter "draw" where he's asked to enter the coordinates of
        the piece he wants to move. This call for draw will require a confirmation from the other player.
        If the other player does not agree, the game will continue.'''




landingwindow = tk.Tk()
landingwindow.geometry(windowdimensions)
landingwindow.title(windowtitle)
landingwindow.configure(bg = landing_background)




def play():
    playwindow = tk.Tk()
    playwindow.geometry(windowdimensions)
    playwindow.title(windowtitle)
    playwindow.configure(bg = play_background)




    def play_progrules():
        progruleswindow = tk.Tk()
        progruleswindow.geometry(windowdimensions)
        progruleswindow.title(windowtitle)
        progruleswindow.configure(bg = progrules_background)


        def progrules_back():
            progruleswindow.destroy()


        progrules_frame =          tk.Frame(progruleswindow, bg = progrules_background, highlightbackground = "black", highlightthickness = 12)
        progrules_padding1_label = tk.Label(progrules_frame, bg = progrules_background, height = 1)
        progrules_title5_label =   tk.Label(progrules_frame, bg = "gray25", fg = "white", font = ("Helvetica", 16, "bold"), text = " Extra Rules: ")
        progrules_padding2_label = tk.Label(progrules_frame, bg = progrules_background, height = 1)
        progrules_content5_label = tk.Label(progrules_frame, bg = progrules_background, font = ("Helvetica", 12), text = content5)
        progrules_padding3_label = tk.Label(progrules_frame, bg = progrules_background, height = 16)
        progrules_back_button =    tk.Button(progrules_frame, bg = "black", fg = "white", font = ("Back to 1982", 14), text = "Back", command = progrules_back)




        progrules_frame.pack(fill = "both", expand = "True")
        progrules_padding1_label.pack()
        progrules_title5_label.pack(fill = "x")
        progrules_padding2_label.pack()
        progrules_content5_label.pack()
        progrules_padding3_label.pack()
        progrules_back_button.pack()




    def play_gamerules():
        gameruleswindow = tk.Tk()
        gameruleswindow.geometry(windowdimensions)
        gameruleswindow.title(windowtitle)
        gameruleswindow.configure(bg = gamerules_background)


        def gamerules_back():
            gameruleswindow.destroy()




        gamerules_frame =           tk.Frame(gameruleswindow, bg = gamerules_background, highlightbackground = "black", highlightthickness = 12)
        gamnerules_padding1_label = tk.Label(gamerules_frame, height = 1, bg = gamerules_background)
        gamerules_title1_label =    tk.Label(gamerules_frame, bg = "gray25", fg = "white", font = ("Helvetica", 16, "bold"), text = " Objective: ")
        gamerules_content1_label =  tk.Label(gamerules_frame, bg = gamerules_background, fg = "black", font = ("Helvetica", 12), text = content1)
        gamerules_padding2_label =  tk.Label(gamerules_frame, bg = gamerules_background, height = 1)
        gamerules_title2_label =    tk.Label(gamerules_frame, bg = "gray25", fg = "white", font = ("Helvetica", 16, "bold"), text = " General Gameplay: ")
        gamerules_content2_label =  tk.Label(gamerules_frame, bg = gamerules_background, fg = "black", font = ("Helvetica", 12), text = content2)
        gamerules_padding3_label =  tk.Label(gamerules_frame, bg = gamerules_background, height = 1)
        gamerules_title3_label =    tk.Label(gamerules_frame, bg = "gray25", fg = "white", font = ("Helvetica", 16, "bold"), text = " Piece Movement: ")
        gamerules_content3_label =  tk.Label(gamerules_frame, bg = gamerules_background, fg = "black", font = ("Helvetica", 12), text = content3)
        gamerules_padding4_label =  tk.Label(gamerules_frame, bg = gamerules_background, height = 1)
        gamerules_title4_label =    tk.Label(gamerules_frame, bg = "gray25", fg = "white", font = ("Helvetica", 16, "bold"), text = " Additional Rules: ")
        gamerules_content4_label =  tk.Label(gamerules_frame, bg = gamerules_background, fg = "black", font = ("Helvetica", 12), text = content4)
        gamerules_padding5_label =  tk.Label(gamerules_frame, bg = gamerules_background, height = 1)
        gamerules_back_button =     tk.Button(gamerules_frame, bg = "black", fg = "white", font = ("Back to 1982", 14), text = "Back", command = gamerules_back)




        gamerules_frame.pack(fill = "both", expand = True)
        gamnerules_padding1_label.pack()
        gamerules_title1_label.pack(fill = "x")
        gamerules_content1_label.pack()
        gamerules_padding2_label.pack()
        gamerules_title2_label.pack(fill = "x")
        gamerules_content2_label.pack()
        gamerules_padding3_label.pack()
        gamerules_title3_label.pack(fill = "x")
        gamerules_content3_label.pack()
        gamerules_padding4_label.pack()
        gamerules_title4_label.pack(fill = "x")
        gamerules_content4_label.pack()
        gamerules_padding5_label.pack()
        gamerules_back_button.pack()


    def play_back():
        playwindow.destroy()


    transcript_file = game_name  + ".txt"
    with open(transcript_file, "r") as m1:
        transcript = m1.read()
        m1.seek(0, 0)
        transcript_lines = m1.readlines()
    w1, b1, w2, b2 = 0, 0, 0, 0
    for i in transcript_lines:
        words = i.split()
        if words[0] == "White" and words[2] == "moved":
            w1 += 1
        elif words[0] == "Black" and words[2] == "moved":
            b1 += 1
        elif words[0] == "White" and words[3] == "killed":
            b2 += 1
        elif words[0] == "Black" and words[3] == "killed":
            w2 += 1
    cursor.execute("Select Winner from Leaderboard where Game_Name = '{}';".format(game_name))
    winner_name = cursor.fetchall()[0][0]


    play_frame =                tk.Frame(playwindow, bg = play_background, highlightbackground = "black", highlightthickness = 12)
    play_padding3_label =       tk.Label(play_frame, bg = play_background, height = 1)
    play_name_label =           tk.Label(play_frame, text = p1_name+" v. "+p2_name, bg = play_background, fg = "black", font = ("Back to 1982", 16))
    play_padding1_label =       tk.Label(play_frame, bg = play_background, text = "     ")
    text_transcript =           ScrolledText(play_frame, height = 40, width = 55)
    play_padding2_label =       tk.Label(play_frame, bg = play_background, text = "     ")
    play_info_frame =           tk.Frame(play_frame, bg = play_info_background, height = 645, width = 350)
    play_rules_frame =          tk.Frame(play_info_frame, bg = play_info_background)
    play_padding5_label =       tk.Label(play_info_frame, bg = play_info_background, height = 1)
    play_padding6_label =       tk.Label(play_rules_frame, bg = play_info_background, text = "  ")
    play_progrules_button =     tk.Button(play_rules_frame, bg = "black", fg = "white", text = " Program Rules ", font = ("Helvetica", 14, "bold"), command = play_progrules)
    play_padding4_label =       tk.Label(play_rules_frame, bg = play_info_background, text = "  ")
    play_gamerules_button =     tk.Button(play_rules_frame, bg = "black", fg = "white", text = "   Chess Rules   ", font = ("Helvetica", 14, "bold"), command = play_gamerules)
    play_padding7_label =       tk.Label(play_rules_frame, bg = play_info_background, text = "  ")
    play_padding8_label =       tk.Label(play_info_frame, bg =  play_info_background, height = 1)
    play_winner_frame =         tk.Frame(play_info_frame, bg = "dodger blue")
    play_win_label =            tk.Label(play_winner_frame, text = "Winner:", font = ("Back to 1982", 14, "bold"), bg = "dodger blue", fg = "white")
    play_winner_label =         tk.Label(play_winner_frame, text = winner_name, font = ("Helvetica", 12, "bold"), bg = "dodger blue", fg = "white")
    play_padding9_label =       tk.Label(play_info_frame, bg =  play_info_background, height = 7)
    play_moves_frame =          tk.Frame(play_info_frame, bg = play_info_background)
    play_p1_moves_label =       tk.Label(play_moves_frame, text = p1_name+"'s Moves: ", font = ("Helvetica", 14, "bold"), bg = play_info_background, fg = "black")
    play_p1_movescount_label =  tk.Label(play_moves_frame, text = w1, font = ("Helveteica", 14), bg = play_info_background, fg = "black")
    play_p2_moves_label =       tk.Label(play_moves_frame, text = p2_name+"'s Moves: ", font = ("Helvetica", 14, "bold"), bg = play_info_background, fg = "black")
    play_p2_movescount_label =  tk.Label(play_moves_frame, text = b1, font = ("Helveteica", 14), bg = play_info_background, fg = "black")
    play_padding10_label =      tk.Label(play_info_frame, bg = play_info_background, height = 4)
    play_pieces_frame =         tk.Frame(play_info_frame, bg = play_info_background)
    play_p1_pieces_label =      tk.Label(play_pieces_frame, bg = play_info_background, fg = "black", text = p1_name+"'s Pieces Killed: ", font = ("Helvetica", 14, "bold"))
    play_p1_piecescount_label = tk.Label(play_pieces_frame, bg = play_info_background, fg = "black", text = w2, font = ("Helvetica", 14))
    play_p2_pieces_label =      tk.Label(play_pieces_frame, bg = play_info_background, fg = "black", text = p2_name+"'s Pieces Killed: ", font = ("Helvetica", 14, "bold"))
    play_p2_piecescount_label = tk.Label(play_pieces_frame, bg = play_info_background, fg = "black", text = b2, font = ("Helvetica", 14))
    play_padding11_label =      tk.Label(play_info_frame, bg = play_info_background, height = 7)
    play_padding14_label =      tk.Label(play_info_frame, bg = play_info_background, height = 1)
    play_quit_button =          tk.Button(play_info_frame, bg = "black", fg = "white", font = ("Back to 1982", 13), text = " Back ", command = play_back)
    play_padding15_label =      tk.Label(play_info_frame, bg = play_info_background, height = 1)




    play_frame.pack(fill = "both", expand = True)
    play_padding3_label.pack()
    play_name_label.pack()
    play_padding1_label.pack(side = "left")
    text_transcript.pack(side = "left")
    play_padding2_label.pack(side = "right")
    play_info_frame.pack(side = "right")
    play_padding5_label.pack(side = "top")
    play_rules_frame.pack(side = "top")
    play_padding6_label.grid(row = 0, column = 0)
    play_progrules_button.grid(row = 0, column = 1)
    play_padding4_label.grid(row = 0, column = 2)
    play_gamerules_button.grid(row = 0, column = 3)
    play_padding7_label.grid(row = 0, column = 4)
    play_padding8_label.pack()
    play_winner_frame.pack(fill = "x", expand = True)
    play_win_label.pack(pady = 5)
    play_winner_label.pack()
    play_padding9_label.pack()
    play_moves_frame.pack()
    play_p1_moves_label.grid(row = 0, column = 0)
    play_p1_movescount_label.grid(row = 0, column = 1)
    play_p2_moves_label.grid(row = 1, column = 0)
    play_p2_movescount_label.grid(row = 1, column = 1)
    play_padding10_label.pack()
    play_pieces_frame.pack()
    play_p1_pieces_label.grid(row = 0, column = 0)
    play_p1_piecescount_label.grid(row = 0, column = 1)
    play_p2_pieces_label.grid(row = 1, column = 0)
    play_p2_piecescount_label.grid(row = 1, column = 1)
    play_padding11_label.pack()
    play_padding14_label.pack()
    play_quit_button.pack()
    play_padding15_label.pack()






    text_transcript.insert(tk.END, transcript)
    text_transcript.configure(state = "disabled")








def landing_quit():
    landingwindow.destroy()


def landing_leaderboard():
    def view_leaderboard():
        viewwindow = tk.Tk()
        viewwindow.geometry(windowdimensions)
        viewwindow.title(windowtitle)
        viewwindow.configure(bg = view_background)


        def view_back():
            viewwindow.destroy()


        cursor.execute("Select * from leaderboard order by moves limit 0, 10")
        leaderdata = cursor.fetchall()


        view_frame =          tk.Frame(viewwindow, bg = view_background, highlightbackground = "black", highlightthickness = 12)
        view_padding1_label = tk.Label(view_frame, bg = view_background, height = 1)
        view_title_label =    tk.Label(view_frame, bg = view_background, text = " Top 10 Leaderboard ", fg = "black", font = ("Helvetica", 20, "bold"))
        view_padding2_label = tk.Label(view_frame, bg = view_background, height = 5)
        view_padding3_label = tk.Label(view_frame, bg = view_background, height = 6)
        view_header_label =   tk.Label(view_frame, bg = view_background, text = "     Rank     Game Name         Player1             Player2               Winner        Moves to Win     ", fg = "black", font = ("Helvetica", 14, "bold"))
        view_board_frame =    tk.Label(view_frame, bg = "gray27", highlightbackground = "black", highlightthickness = 3)
        view_back_button =    tk.Button(view_frame, bg = "black", fg = "white", text = "Back", font = ("Back to 1982", 14), command = view_back)


        view_frame.pack(fill = "both", expand = True)
        view_padding1_label.pack()
        view_title_label.pack()
        view_padding3_label.pack()
        view_header_label.pack()
        view_board_frame.pack()
        view_padding2_label.pack()
        view_back_button.pack()


        i = 0
        for rec in leaderdata:
            for j in range (len(leaderdata[0])):
                block_entry = tk.Entry(view_board_frame, width = 12, fg = "black", bg = "white", font = ("Helvetica", 14))
                block_entry.grid(row = i, column = j+1, pady = 3, padx = 1)
                block_entry.insert(tk.END, " " + str(rec[j]))
                block_entry.configure(state = "disabled")
            rank_entry =  tk.Entry(view_board_frame, width = 5, fg = "black", bg = "white", font = ("Helvetica", 14))
            rank_entry.grid(row = i, column = 0, pady = 3, padx = 1)
            rank_entry.insert(tk.END, " " +str(i+1) +" ")
            rank_entry.configure(state = "disabled")
            i += 1


    def edit_leaderboard():
        editwindow = tk.Tk()
        editwindow.geometry(windowdimensions)
        editwindow.title(windowtitle)
        editwindow.configure(bg = edit_background)


        def edit_back():
            editwindow.destroy()


        def show_rank():
            cursor.execute("select Player1, Player2 from leaderboard where Game_Name = '{}'".format(edit_rank.get()))
            show_rank_info = cursor.fetchall()
            edit_show_rank_label.configure(text = show_rank_info)


        def delete_record():
            if edit_rank.get() == "":
                messagebox.showinfo("Error", "Please select a Game to operate on.")
            else:
                cursor.execute("delete from leaderboard where Game_Name = '{}'".format(edit_rank.get()))
                connection.commit()
                messagebox.showinfo("Success", "The Record has been deleted from the Leaderboard.")


        def edit_record():
            if edit_rank.get() == "":
                messagebox.showinfo("Error", "Please select a Game to operate on.")
            else:
                def edit_record_back():
                    edit_attribute_label.forget()
                    edit_padding10_label.forget()
                    edit_attribute_frame.forget()
                    edit_padding7_label.forget()
                    edit_change_label.forget()
                    edit_padding8_label.forget()
                    edit_change_entry.forget()
                    edit_padding9_label.forget()
                    edit_submit_button.forget()
                    edit_padding2_label.forget()
                    edit_record_back_button.forget()
                    edit_padding5_label.pack()
                    edit_action_label.pack()
                    edit_padding6_label.pack()
                    edit_action1_button.pack()
                    edit_padding7_label.pack()
                    edit_action2_button.pack()
                    edit_padding2_label.pack()
                    edit_back_button.pack()


                edit_attribute, attribute_list = tk.StringVar(editwindow), ["Player1", "Player2"]


                def edit_submit():
                    if edit_attribute.get() == "":
                        messagebox.showinfo("Error", "Please select a Player Name to edit.")
                    elif edit_change_entry.get() == "":
                        messagebox.showinfo("Error", "Please enter a value.")
                    else:
                            if len(edit_change_entry.get()) > 12:
                                messagebox.showinfo("Error", "Length of Player Name cannot exceed 12 characters.")
                            else:
                                cursor.execute("Select Winner from Leaderboard where Game_Name = '{}'".format(edit_rank.get()))
                                winner_name = cursor.fetchall()[0][0]
                                cursor.execute("Select {} from leaderboard where Game_Name = '{}'".format(edit_attribute.get(), edit_rank.get()))
                                player_name = cursor.fetchall()[0][0]
                                if winner_name == player_name:
                                    cursor.execute("update leaderboard set winner = '{}' where Game_Name = '{}'".format(edit_change_entry.get(), edit_rank.get()))
                                    connection.commit()
                                cursor.execute("update leaderboard set {} = '{}' where Game_Name = '{}'".format(edit_attribute.get(), edit_change_entry.get(), edit_rank.get()))
                                connection.commit()
                                messagebox.showinfo("Success", "Leaderboard edited successfully. See the updated records in the 'View Leaderboard' tab.")


                edit_action_label.forget()
                edit_padding6_label.forget()
                edit_action1_button.forget()
                edit_padding7_label.forget()
                edit_action2_button.forget()
                edit_padding2_label.forget()
                edit_back_button.forget()


                edit_attribute_label =    tk.Label(edit_frame, bg = edit_background, fg = "black", text = "Select an Attribute to Edit:", font = ("Helvetica", 16, "bold"))
                edit_attribute_frame =    tk.Frame(edit_frame, bg = edit_background)
                edit_change_label =       tk.Label(edit_frame, bg = edit_background, fg = "black", text = "Enter the Updated Value:", font = ("Helvetica", 16, "bold"))
                edit_padding8_label =     tk.Label(edit_frame, bg = edit_background, height = 1)
                edit_change_entry =       tk.Entry(edit_frame, highlightbackground = edit_background, width = 34)
                edit_padding9_label =     tk.Label(edit_frame, bg = edit_background, height = 2)
                edit_submit_button =      tk.Button(edit_frame, bg = "white", fg = "black", text = "Submit Changes", font = ("Back to 1982", 18), command = edit_submit)
                edit_padding10_label =    tk.Label(edit_frame, bg = edit_background, height = 1)
                edit_record_back_button = tk.Button(edit_frame, bg = "black", fg = "white", text = "Back", font = ("Back to 1982", 14), command = edit_record_back)


                for i in attribute_list:
                        edit_attribute_radio = tk.Radiobutton(edit_attribute_frame, text = " "+i+" ", var = edit_attribute, value = i, indicatoron = 0, font = ("Helvetica", 10, "bold"), width = 17)
                        edit_attribute_radio.grid(row = 0, column = attribute_list.index(i))


                edit_attribute_label.pack()
                edit_padding10_label.pack()
                edit_attribute_frame.pack()
                edit_padding7_label.pack()
                edit_change_label.pack()
                edit_padding8_label.pack()
                edit_change_entry.pack()
                edit_padding9_label.pack()
                edit_submit_button.pack()
                edit_padding2_label.pack()
                edit_record_back_button.pack()


        edit_frame =           tk.Frame(editwindow, bg = edit_background, highlightbackground = "black", highlightthickness = 12)
        edit_padding1_label =  tk.Label(edit_frame, bg = edit_background, height = 2)
        edit_rank_label =      tk.Label(edit_frame, bg = edit_background, fg = "black", text = "Select a Game Name to Edit its Record:", font = ("Helvetica", 16, "bold"))
        edit_padding3_label =  tk.Label(edit_frame, bg = edit_background, height = 1)
        edit_rank_frame =      tk.Frame(edit_frame, bg = edit_background)
        edit_padding4_label =  tk.Label(edit_frame, bg = edit_background, height = 1)
        edit_show_rank_label = tk.Label(edit_frame, bg = edit_background, fg = "black", text = "Nothing Selected", font = ("Helvetica", 12, "bold"))
        edit_padding5_label =  tk.Label(edit_frame, bg = edit_background, height = 2)
        edit_action_label =    tk.Label(edit_frame, bg = edit_background, fg = "black", text = "Select what you want to do:", font = ("Helvetica", 16, "bold"))
        edit_padding6_label =  tk.Label(edit_frame, bg = edit_background, height = 5)
        edit_action1_button =  tk.Button(edit_frame, text = " Edit Record", font = ("Back to 1982", 16, "bold"), width = 17, bg = "white", fg = "black", command = edit_record)
        edit_padding7_label =  tk.Label(edit_frame, bg = edit_background, height = 1)
        edit_action2_button =  tk.Button(edit_frame, text = " Delete Record", font = ("Back to 1982", 16, "bold"), width = 17, bg = "white", fg = "black", command = delete_record)
        edit_padding2_label =  tk.Label(edit_frame, bg = edit_background, height = 9)
        edit_back_button =     tk.Button(edit_frame, bg = "black", fg = "white", text = "Back", font = ("Back to 1982", 14), command = edit_back)


        cursor.execute("select Game_Name from leaderboard order by moves;")
        gamename_list = cursor.fetchall()


        edit_rank = tk.StringVar(editwindow)


        for i in range(10):
            try:
                name = gamename_list[i][0]
                edit_rank_radio = tk.Radiobutton(edit_rank_frame, text = " "+name+" ", variable = edit_rank, value = name, indicatoron = 0, font = ("Helvetica", 10, "bold"), width = 17, command = show_rank)
                if i <= 4:
                    edit_rank_radio.grid(row = 0, column = i)
                else:
                    edit_rank_radio.grid(row = 1, column = i-5)
            except Exception:
                pass


        edit_frame.pack(fill = "both", expand = True)
        edit_padding1_label.pack()
        edit_rank_label.pack()
        edit_padding3_label.pack()
        edit_rank_frame.pack()
        edit_padding4_label.pack()
        edit_show_rank_label.pack()
        edit_padding5_label.pack()
        edit_action_label.pack()
        edit_padding6_label.pack()
        edit_action1_button.pack()
        edit_padding7_label.pack()
        edit_action2_button.pack()
        edit_padding2_label.pack()
        edit_back_button.pack()


    def landing_leaderboard_back():
        landing_padding1_label.configure(height = 13)
        landing_padding3_label.forget()
        landing_padding4_label.forget()
        landing_padding5_label.forget()
        landing_leaderboard_back_button.forget()
        landing_leaderboard_edit_button.forget()
        landing_leaderboard_view_button.forget()
        landing_buttons_frame.pack()
        landing_leaderboard_button.grid(row = 0, column = 0)
        landing_padding2_label.grid(row = 0, column = 1)
        landing_play_button.grid(row = 0, column = 2)
        landing_padding3_label.pack()
        landing_quit_button.pack()


    landing_padding1_label.configure(height = 1)
    landing_buttons_frame.forget()
    landing_padding3_label.forget()
    landing_quit_button.forget()
    landing_padding4_label =          tk.Label(landing_frame, bg = landing_background, height = 3)
    landing_leaderboard_view_button = tk.Button(landing_frame, bg = "white", fg = "black", text = "View Leaderboard", font = ("Back to 1982", 18), command = view_leaderboard)
    landing_padding5_label =          tk.Label(landing_frame, bg = landing_background, height = 2)
    landing_leaderboard_edit_button = tk.Button(landing_frame, bg = "white", fg = "black", text = "Edit Leaderboard", font = ("Back to 1982", 18), command = edit_leaderboard)
    landing_leaderboard_back_button = tk.Button(landing_frame, bg = "black", fg = "white", text = "Back", font = ("Back to 1982", 14), command = landing_leaderboard_back)


    landing_padding4_label.pack()
    landing_leaderboard_view_button.pack()
    landing_padding5_label.pack()
    landing_leaderboard_edit_button.pack()
    landing_padding3_label.pack()
    landing_leaderboard_back_button.pack()


def landing_play():
    global p1_name, p2_name


    def landing_play_back():
        landing_padding1_label.configure(height = 13)
        landing_padding3_label.forget()
        landing_padding4_label.forget()
        landing_padding5_label.forget()
        landing_play_frame.forget()
        landing_start_game_button.forget()
        landing_play_back_button.forget()
        landing_buttons_frame.pack()
        landing_leaderboard_button.grid(row = 0, column = 0)
        landing_padding2_label.grid(row = 0, column = 1)
        landing_play_button.grid(row = 0, column = 2)
        landing_padding3_label.pack()
        landing_quit_button.pack()


    def submission():
        global p1_name, p2_name, game_name
        if view_rank.get() == "":
            messagebox.showinfo("Error", "Please select a game to view.")
        else:
            cursor.execute("Select Player1, Player2 from Leaderboard where Game_Name = '{}'".format(view_rank.get()))
            player_names = cursor.fetchall()[0]
            p1_name, p2_name, game_name = player_names[0], player_names[1], view_rank.get()
            play()




    landing_padding1_label.configure(height = 1)
    landing_buttons_frame.forget()
    landing_padding3_label.forget()
    landing_quit_button.forget()
    landing_padding4_label =    tk.Label(landing_frame, bg = landing_background, height = 3)
    landing_play_frame =        tk.Frame(landing_frame, bg = landing_background)
    landing_padding5_label =    tk.Label(landing_frame, bg = landing_background, height = 4)
    landing_start_game_button = tk.Button(landing_frame, bg = "white", fg = "black", text = "    View Game    ", font = ("Back to 1982", 18), command = submission)
    landing_play_back_button =  tk.Button(landing_frame, bg = "black", fg = "white", text = "Back", font = ("Back to 1982", 14), command = landing_play_back)


    cursor.execute("select Game_Name from leaderboard order by moves;")
    gamename_list = cursor.fetchall()
    view_rank = tk.StringVar(landingwindow)
    for i in range(10):
        try:
            name = gamename_list[i][0]
            edit_rank_radio = tk.Radiobutton(landing_play_frame, text = " "+name+" ", variable = view_rank, value = name, indicatoron = 0, font = ("Helvetica", 10, "bold"), width = 17)
            if i <= 4:
                edit_rank_radio.grid(row = 0, column = i)
            else:
                edit_rank_radio.grid(row = 1, column = i-5)
        except Exception:
            pass


    landing_padding4_label.pack()
    landing_play_frame.pack()
    landing_padding5_label.pack()
    landing_start_game_button.pack()
    landing_padding3_label.pack()
    landing_play_back_button.pack()




landing_frame =              tk.Frame(landingwindow, bg = landing_background, highlightbackground = "black", highlightthickness = 12)
landing_padding1_label =     tk.Label(landing_frame, bg = landing_background, height = 13)
chess_logo_label =           tk.Label(landing_frame, text = "  -  CHESS  -  ", font = ("back to 1982", 68), bg = landing_background, fg = "black")
chess_line_label =           tk.Label(landing_frame, text = "---", font = ("back to 1982", 54), bg = landing_background, fg = "black")
landing_buttons_frame =      tk.Frame(landing_frame, bg = landing_background)
landing_leaderboard_button = tk.Button(landing_buttons_frame, bg = "white", fg = "black", text = "Leaderboard", font = ("Back to 1982", 18), command = landing_leaderboard)
landing_play_button =        tk.Button(landing_buttons_frame, bg = "white", fg = "black", text = " View Games ", font = ("Back to 1982", 18), command = landing_play)
landing_padding2_label =     tk.Label(landing_buttons_frame, bg = landing_background, text = "   ")
landing_padding3_label =     tk.Label(landing_frame, bg = landing_background, height = 5)
landing_quit_button =        tk.Button(landing_frame, fg = "white", bg = "black", text = "Quit", font = ("Back to 1982", 14), command = landing_quit)


landing_frame.pack(fill = "both", expand = True)
landing_padding1_label.pack()
chess_logo_label.pack()
chess_line_label.pack()
landing_buttons_frame.pack()
landing_leaderboard_button.grid(row = 0, column = 0)
landing_padding2_label.grid(row = 0, column = 1)
landing_play_button.grid(row = 0, column = 2)
landing_padding3_label.pack()
landing_quit_button.pack()


landingwindow.mainloop()