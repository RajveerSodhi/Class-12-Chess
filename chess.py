''' Rajveer's Chess Program '''


# =============================================================================
# miscellaneous functions
# =============================================================================




with open ("moves.txt", "w") as c1:
    c1.write("Moves performed in the game: \n")


board = [[   "null", "null",    "null",    "null",    "null",    "null",    "null",   "null",     "null"],                                 # the board layout
            ["null", chr(9820), chr(9822), chr(9821), chr(9819), chr(9818), chr(9821), chr(9822), chr(9820), "null", " ", " ", " ", " "],
            ["null", chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), "null", " ", " ", " ", " "],
            ["null", " ",       " ",       " ",       " ",       " ",       " ",       " ",       " ",       "null", " ", " ", " ", " "],
            ["null", " ",       " ",       " ",       " ",       " ",       " ",       " ",       " ",       "null", " ", " ", " ", " "],
            ["null", " ",       " ",       " ",       " ",       " ",       " ",       " ",       " ",       "null", " ", " ", " ", " "],
            ["null", " ",       " ",       " ",       " ",       " ",       " ",       " ",       " ",       "null", " ", " ", " ", " "],
            ["null", chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), "null", " ", " ", " ", " "],
            ["null", chr(9813), chr(9816), chr(9813), chr(9813), chr(9812), chr(9815), chr(9816), chr(9814), "null", " ", " ", " ", " "],
            ["null", "null",    "null",    "null",    "null",    "null",    "null",    "null",    "null"]]
def print_board(x):
    print("\n", "       A   B   C   D   E   F   G   H", "\n", "\n", "     +-------------------------------+", "\n", " 8  ", "|", x[1][1], "|", x[1][2], "|", x[1][3], "|", x[1][4], "|", x[1][5], "|", x[1][6], "|", x[1][7], "|", x[1][8], "|", "  8       ", x[1][10], "  ", x[1][11], "  ", x[1][12], "  ", x[1][13], "\n", "     |-------------------------------|")
    print("  7  ", "|", x[2][1], "|", x[2][2], "|", x[2][3], "|", x[2][4], "|", x[2][5], "|", x[2][6], "|", x[2][7], "|", x[2][8], "|", "  7       ", x[2][10], "  ", x[2][11], "  ", x[2][12], "  ", x[2][13], "\n", "     |-------------------------------|")
    print("  6  ", "|", x[3][1], "|", x[3][2], "|", x[3][3], "|", x[3][4], "|", x[3][5], "|", x[3][6], "|", x[3][7], "|", x[3][8], "|", "  6       ", x[3][10], "  ", x[3][11], "  ", x[3][12], "  ", x[3][13], "\n", "     |-------------------------------|")
    print("  5  ", "|", x[4][1], "|", x[4][2], "|", x[4][3], "|", x[4][4], "|", x[4][5], "|", x[4][6], "|", x[4][7], "|", x[4][8], "|", "  5       ", x[4][10], "  ", x[4][11], "  ", x[4][12], "  ", x[4][13], "\n", "     |-------------------------------|")
    print("  4  ", "|", x[5][1], "|", x[5][2], "|", x[5][3], "|", x[5][4], "|", x[5][5], "|", x[5][6], "|", x[5][7], "|", x[5][8], "|", "  4       ", x[5][10], "  ", x[5][11], "  ", x[5][12], "  ", x[5][13], "\n", "     |-------------------------------|")
    print("  3  ", "|", x[6][1], "|", x[6][2], "|", x[6][3], "|", x[6][4], "|", x[6][5], "|", x[6][6], "|", x[6][7], "|", x[6][8], "|", "  3       ", x[6][10], "  ", x[6][11], "  ", x[6][12], "  ", x[6][13], "\n", "     |-------------------------------|")
    print("  2  ", "|", x[7][1], "|", x[7][2], "|", x[7][3], "|", x[7][4], "|", x[7][5], "|", x[7][6], "|", x[7][7], "|", x[7][8], "|", "  2       ", x[7][10], "  ", x[7][11], "  ", x[7][12], "  ", x[7][13], "\n", "     |-------------------------------|")
    print("  1  ", "|", x[8][1], "|", x[8][2], "|", x[8][3], "|", x[8][4], "|", x[8][5], "|", x[8][6], "|", x[8][7], "|", x[8][8], "|", "  1       ", x[8][10], "  ", x[8][11], "  ", x[8][12], "  ", x[8][13], "\n", "     +-------------------------------+", "\n", "\n", "       A   B   C   D   E   F   G   H", "\n")


def select(board, piece_list, y_dict, trapped, pawn, rook, knight, bishop, queen, king, select):        # initial coordinates selection
    global selection, breaker, init_u_coords, init_u_x, init_u_y  , init_c_x, init_c_y, winner
    while selection not in piece_list:
        if breaker:
            break
        while trapped == True:
            try:
                init_u_coords = input("Enter the coordinates of the piece you want to move: ")
                if init_u_coords.lower() == "declare":              # declaration of loss
                    declare_sure = input("Are you sure? (y/n): ")
                    if declare_sure.lower() == "y":
                        print(you, "declared defeat.", opponent, "wins!")
                        breaker, winner = True, opponent
                        break
                    else:
                        print(you, "withdrew their declaration.")
                        select(board, piece_list, y_dict, trapped, pawn, rook, knight, bishop, queen, king, select)
                        break
                elif init_u_coords.lower() == "draw":               # calls to end the match in a draw
                    print(you, "is calling for a draw! Does", opponent, "agree? (Type draw if yes):")
                    draw_input = input()
                    if draw_input.lower() == "draw":
                        print("The game ended in a draw!")
                        breaker, winner = True, "draw"
                        break
                    else:
                        print(opponent, "Doesn't agree with you. The match coninues.", "\n")
                        select(board, piece_list, y_dict, trapped, pawn, rook, knight, bishop, queen, king, select)
                        break
                init_u_x, init_u_y = int(init_u_coords[0]), init_u_coords[1].title()
                if init_u_x not in range(1,9):
                    continue
                init_c_x, init_c_y = 9-init_u_x, y_dict[init_u_y]
                selection = board[init_c_x][init_c_y]
                if selection not in piece_list:                 # checks if the coordinates entered have a piece from your team or from the other team/ is a blank space
                    print("Error! Please choose a piece from your team.")
                    continue
                trapped, trap_breaker = False, False            # checks if the piece is surrounded, i.e., if it has any legal moves at all. if it doesn't the user won't be allowed to choose it at all
                if selection == chr(9817):                                   # white pawn
                    for i in range(-1, 2, 2):
                        if init_c_x == 4 and board[init_c_x][init_c_y+i] == chr(9823) and board[init_c_x-1][init_c_y+i] == " ":
                            trapped, trap_breaker = False, True
                            break
                    if trap_breaker:
                        break
                    if board[init_c_x-1][init_c_y] != " " and board[init_c_x-1][init_c_y+1] not in black_list and board[init_c_x-1][init_c_y-1] not in black_list:
                        trapped = True
                elif selection == chr(9823):                                 # black pawn
                    for i in range(-1,2,2):
                        if init_c_x == 5 and board[init_c_x][init_c_y+i] == chr(9817) and board[init_c_x+1][init_c_y+i] == " ":
                            trapped, trap_breaker = False, True
                            break
                    if trap_breaker:
                        break
                    if board [init_c_x+1][init_c_y] != " " and board[init_c_x+1][init_c_y+1] not in white_list and board[init_c_x+1][init_c_y-1] not in white_list:
                        trapped = True
                elif selection == chr(9814) or selection == chr(9820):       # rook
                    if ((board[init_c_x+1][init_c_y] in piece_list or board[init_c_x+1][init_c_y] == "null") and (board[init_c_x-1][init_c_y] in piece_list or board[init_c_x-1][init_c_y] == "null")) and ((board[init_c_x][init_c_y+1] in piece_list or board[init_c_x][init_c_y+1] == "null") and (board[init_c_x][init_c_y-1] in piece_list or board[init_c_x][init_c_y-1] == "null")):
                        trapped = True
                elif selection == chr(9815) or selection == chr(9821):       # bishop
                    if (board[init_c_x+1][init_c_y+1] in piece_list or board[init_c_x+1][init_c_y+1] == "null") and (board[init_c_x+1][init_c_y-1] in piece_list or board[init_c_x+1][init_c_y-1] == "null") and (board[init_c_x-1][init_c_y-1] in piece_list or board[init_c_x-1][init_c_y-1] == "null") and (board[init_c_x-1][init_c_y+1] in piece_list or board[init_c_x-1][init_c_y+1] == "null"):
                        trapped = True
                elif selection == chr(9812) or selection == chr(9818) or selection == chr(9819) or selection == chr(9813):      # king, queen
                    if ((board[init_c_x+1][init_c_y] in piece_list or board[init_c_x+1][init_c_y] == "null") and (board[init_c_x-1][init_c_y] in piece_list or board[init_c_x-1][init_c_y] == "null")) and ((board[init_c_x][init_c_y+1] in piece_list or board[init_c_x][init_c_y+1] == "null") and (board[init_c_x][init_c_y-1] in piece_list or board[init_c_x][init_c_y-1] == "null")) and (board[init_c_x+1][init_c_y+1] in piece_list or board[init_c_x+1][init_c_y+1] == "null") and (board[init_c_x+1][init_c_y-1] in piece_list or board[init_c_x+1][init_c_y-1] == "null") and (board[init_c_x-1][init_c_y-1] in piece_list or board[init_c_x-1][init_c_y-1] == "null") and (board[init_c_x-1][init_c_y+1] in piece_list or board[init_c_x-1][init_c_y+1] == "null"):
                        trapped = True


                if trapped == True:
                    print("Error! Please choose a piece that can move.")
            except Exception:
                continue


def en_passant(board, new_c_x, new_c_y, print_board, kill_dict, selection, init_u_coords ,new_u_coords, counter, u_y_dict, white_list, black_list):     # en passant movement for pawns
    global white_kill, black_kill, inloop, printer, passant
    while inloop:
        if counter % 2 == 0:
            kill_list, kill_add, initial_x, a, killed_u_coord, killed_chr, opp_list, king, add = white_kill, 5, 4, -1, "5", chr(9823), black_list, chr(9812), black_add      # variables to make the same function applicable to both pawns
        elif counter % 2 == 1:
            kill_list, kill_add, initial_x, a, killed_u_coord, killed_chr, opp_list, king, add = black_kill, 1, 5, 1, "4", chr(9817), white_list, chr(9818), white_add
        for i in range (-1, 2, 2):
            if init_c_x == initial_x and board[init_c_x][init_c_y+i] == killed_chr:
                if new_c_x == init_c_x+a and new_c_y == init_c_y+i:
                    killed_piece, killer_piece, killer, killed = kill_dict[board[init_c_x][new_c_y]], kill_dict[selection], board[init_c_x][init_c_y], board[new_c_x][new_c_y]
                    killed_piece_u_coords = killed_u_coord + u_y_dict[new_c_y]
                    board[new_c_x][new_c_y], board[init_c_x][init_c_y+i], board[init_c_x][init_c_y] = killer, " ", " "
                    checker(board, opp_list, king, add)
                    if selection in white_list:
                        check = white_check
                    elif selection in black_list:
                        check = black_check
                    if check:
                        print("King is under check! Invalid move!")
                        board[new_c_x][new_c_y], board[init_c_x][init_c_y], board[new_c_x][new_c_y+i], inloop, counter, printer = " ", killer, killed, False, counter - 1, False
                        break
                    else:
                        board[new_c_x][new_c_y], board[init_c_x][init_c_y+i], board[init_c_x][init_c_y] = killer, " ", " "
                        board[(kill_list // 4) + kill_add][(kill_list % 4)+10] = board[init_c_x][new_c_y]
                        kill_list, inloop = kill_list + 1, inloop
                        print("\n", killer_piece," (", init_u_coords[0:2], ") ", "killed ", killed_piece, " (", killed_piece_u_coords, ")", "\n", sep = "")
                        if counter % 2 == 0:                                        # shows the killed piece to the right of the board in a 4x4 grid for each team
                            board[(white_kill // 4)+5][(white_kill % 4)+10], white_kill = board[new_c_x][new_c_y], white_kill + 1
                        elif counter % 2 == 1:
                            board[((black_kill) // 4)+1][(black_kill % 4)+10], black_kill = board[new_c_x][new_c_y], black_kill + 1
                        print_board(board)
                        break
    passant = False


def new_coords_choice(y_dict):      # asks for entry of new coordinates
    global new_c_x, new_c_y, new_u_coords, back, counter, printer, breaker
    while True:
        try:
            new_u_coords = input("Enter the coordinates of where you want to move the piece: ")
            if new_u_coords.lower() == "back":
                back, counter, printer = True, counter - 1, False
                break
            else:
                new_u_x, new_u_y = int(new_u_coords[0]), new_u_coords[1].title()
            if new_u_x not in range(1,9):           # makes sure the row entered is between 1 and 8
                continue
            new_c_x, new_c_y = 9-new_u_x, y_dict[new_u_y]
            break
        except Exception:
            pass


def counter_checker(counter, white_list, black_list):           # defines whose turn it is and assigns the list of the opponent's pieces accordingly
    global piece_list
    if counter % 2 == 0:
        piece_list = black_list
    if counter % 2 == 1:
        piece_list = white_list


def checker(board, white_list, black_king, white_add):              # checks whether a team's king is under check
    global black_check, white_check
    king, check = black_king, False
    for king_x in range (len(board)):
        if type(board[king_x]) == type(board):
            try:
                king_y = board[king_x].index(black_king)
                break
            except ValueError:
                pass


    for i in range(-1,2,2):             # pawn
        try:
            if board[king_x+white_add][king_y+i] == white_list[5]:
                check = True
                break
        except IndexError:
            pass
    for i in range (king_x+1, 9):       #white rook, queen: straight
        if board[i][king_y] == white_list[0] or board[i][king_y] == white_list[3]:
            check = True
        elif board[i][king_y] not in [" " , white_list[3], white_list[0]]:
            break
    for i in range(king_x-1, 0, -1):
        if board[i][king_y] == white_list[0] or board[i][king_y] == white_list[3]:
            check = True
        elif board[i][king_y] not in [" " , white_list[3], white_list[0]]:
            break
    for i in range (king_y+1, 9):
        if board[king_x][i] == white_list[0] or board[king_x][i] == white_list[3]:
            check = True
        elif board[king_x][i] not in [" " , white_list[3], white_list[0]]:
            break
    for i in range(king_y-1, 0, -1):
        if board[king_x][i] == white_list[0] or board[king_x][i] == white_list[3]:
            check = True


        elif board[king_x][i] not in [" " , white_list[3], white_list[0]]:
            break
    y=king_y+1                  # white bishop, queen: diagonal
    for x in range(king_x+1, 9):
        try:
            if board[x][y] == white_list[3] or board[x][y] == white_list[2]:
                check = True
            elif board[x][y] not in [" ", white_list[3], white_list[2]]:
                break
            if y < 8:
                y += 1
        except IndexError:
            break
    y=king_y+1
    for x in range(king_x-1, 0, -1):
        try:
            if board[x][y] == white_list[3] or board[x][y] == white_list[2]:
                check = True
            elif board[x][y] not in [" ", white_list[3], white_list[2]]:
                break
            if y < 8:
                y += 1
        except IndexError:
            break
    y=king_y-1
    for x in range(king_x-1, 0, -1):
        try:
            if board[x][y] == white_list[3] or board[x][y] == white_list[2]:
                check = True
            elif board[x][y] not in [" ", white_list[3], white_list[2]]:
                break
            if y > 0:
                y -= 1
        except IndexError:
            break
    y=king_y-1
    for x in range(king_x+1, 9):
        try:
            if board[x][y] == white_list[3] or board[x][y] == white_list[2]:
                check = True
            elif board[x][y] not in [" ", white_list[3], white_list[2]]:
                break
            if y > 0:
                y -= 1
        except IndexError:
            break
    for i in range (-1,2,2):            # knight
        for m in range (-2,3,4):
            try:
                if board[king_x+m][king_y+i] == white_list[1] or board[king_x+i][king_y+m] == white_list[1]:
                    check = True
            except IndexError:
                pass
    for i in range(-1,2,2):             # king
        try:
            if board[king_x][king_y+i] == white_list[4] or board[king_x+i][king_y] == white_list[4] or board[king_x+i][king_y+i] == white_list[4] or board[king_x+i][king_y-i] == white_list[4]:
                check = True
        except IndexError:
            pass


    if king == chr(9818):
        black_check = check
    elif king == chr(9812):
        white_check = check


def movement(kill, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check):       # master function for movement of all pieces, includes functionality for checking check as well as the killing of pieces. will be used for movement in 90% places.      
    global inloop, counter, white_check, black_check, printer
    new_piece = board[new_c_x][new_c_y]
    board[new_c_x][new_c_y] = board[init_c_x][init_c_y]
    board[init_c_x][init_c_y] = " "
    checker(board, opp_list, king, add)
    if selection in white_list:
        check = white_check
    elif selection in black_list:
        check = black_check
    if check:
        print("King is under check! Invalid move!")
        board[init_c_x][init_c_y] = board[new_c_x][new_c_y]
        board[new_c_x][new_c_y] = new_piece
        inloop, counter, printer = False, counter - 1, False
    else:
        board[init_c_x][init_c_y] = board[new_c_x][new_c_y]
        board[new_c_x][new_c_y] = new_piece
        kill(board, new_c_x, new_c_y, print_board, kill_dict, selection, init_u_coords ,new_u_coords, counter, init_c_x, init_c_y)
        inloop = False
def kill(board, new_c_x, new_c_y, print_board, kill_dict, selection, init_u_coords ,new_u_coords, counter, init_c_x, init_c_y):             # updates board with new positions, but if a player is killed, shows kill message and displays the killed piece to the side of the board
    global white_kill, black_kill, king_breaker, moves_kill, winner
    king_checker = ""
    if board[new_c_x][new_c_y] != " ":
        killed_piece, killer_piece = kill_dict[board[new_c_x][new_c_y]], kill_dict[selection]
        if counter % 2 == 0:                                       # shows the killed piece to the right of the board in a 4x4 grid for each team
            board[(white_kill // 4)+5][(white_kill % 4)+10], white_kill = board[new_c_x][new_c_y], white_kill + 1
        elif counter % 2 == 1:
            board[((black_kill) // 4)+1][(black_kill % 4)+10], black_kill = board[new_c_x][new_c_y], black_kill + 1
        kill_statement = killer_piece + " (" + init_u_coords[0:2] + ") killed " + killed_piece + " (" + new_u_coords[0:2] + ") \n"
        print("\n", kill_statement)
        with open("moves.txt", "a") as c1:
            c1.write(kill_statement)
        moves_kill = True
        king_checker = killed_piece
    board[new_c_x][new_c_y] = board[init_c_x][init_c_y]
    board[init_c_x][init_c_y] = " "
    print_board(board)
    if king_checker == "Black King":                    # if the killed piece is a king, the game ends
        print("The Black King has been killed! Player 1 wins!")
        with open("moves.txt", "a") as c1:
            c1.write("The Black King has been killed! Player 1 wins!")
        king_breaker, moves_kill, winner = True, True, "Player 1"
    elif king_checker == "White King":
        print("The White King has been killed! Player 2 wins!")
        with open("moves.txt", "a") as c1:
            c1.write("The White King has been killed! Player 2 wins!")
        king_breaker, moves_kill, winner = True, True, "Player 2"


def update_board(board, new_c_x, new_c_y, print_board, kill_dict, selection, init_u_coords ,new_u_coords, counter, init_c_x, init_c_y) :            # updating board with new positions, primarily used in pawn movement
    board[new_c_x][new_c_y], board[init_c_x][init_c_y] = board[init_c_x][init_c_y], " "
    print_board(board)


def diagonal_block(board, new_c_x, init_c_x, new_c_y, init_c_y, change):            # blockage checker for bishop and diagonal movement of queen
    global add, blockage
    blockage, add = False, 1
    if new_c_x == init_c_x+change:                  # checks if its path is obstructed
        if new_c_y > init_c_y:          # down, right
            for c in range(init_c_x+1, new_c_x):
                if board[init_c_x+add][init_c_y+add] != " ":
                    blockage = True
                add += 1
        elif new_c_y < init_c_y:        # down, left
            for c in range(init_c_x+1, new_c_x):
                if board[init_c_x+add][init_c_y-add] != " ":
                    blockage = True
                add += 1
    elif new_c_x == init_c_x-change:
        if new_c_y > init_c_y:          # up, right
            for c in range(new_c_x+1, init_c_x):
                if board[init_c_x-add][init_c_y+add] != " ":
                    blockage = True
                add += 1
        elif new_c_y < init_c_y:        # up, left
            for c in range(new_c_x+1, init_c_x):
                if board[init_c_x-add][init_c_y-add] != " ":
                    blockage = True
                add += 1
def straight_block(board, new_c_x, init_c_x, new_c_y, init_c_y):        # blockage checker for rook and straight movement of queen
    global blockage
    blockage = False            # checks if its path is obstructed
    if new_c_y == init_c_y:
        if init_c_x > new_c_x:
            for block in range (new_c_x+1, init_c_x):
                if board[block][new_c_y] != " ":
                    blockage = True
        elif init_c_x < new_c_x:
            for block in range (init_c_x+1, new_c_x):
                if board[block][new_c_y] != " ":
                    blockage = True
    elif new_c_x == init_c_x:
        if init_c_y > new_c_y:
            for block in range (new_c_y+1, init_c_y):
                if board[new_c_x][block] != " ":
                    blockage = True
        elif init_c_y < new_c_y:
            for block in range (init_c_y+1, new_c_y):
                if board[new_c_x][block] != " ":
                    blockage = True




# various lists, tuples, dictionaries and variables defined for reference throughout the code
kill_dict = {chr(9820) : "Black Rook", chr(9822) : "Black Knight", chr(9821) : "Black Bishop", chr(9819) : "Black Queen" , chr(9818) : "Black King", chr(9823) : "Black Pawn", chr(9814) : "White Rook", chr(9816) : "White Knight", chr(9815) : "White Bishop", chr(9813) : "White Queen", chr(9812) : "White King", chr(9817) : "White Pawn"}
y_dict, u_y_dict = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8}, {1 : "a", 2 : "b", 3 : "c",  4 : "d", 5 : "e", 6 : "f", 7 : "g", 8 : "h"}
white_promotion_dict, black_promotion_dict = {"Rook" : chr(9814), "Knight" : chr(9816), "Bishop" : chr(9815), "Queen" : chr(9813)},  {"Rook" : chr(9820), "Knight" : chr(9822), "Bishop" : chr(9821), "Queen" : chr(9819)}
white_list, black_list = (chr(9814), chr(9816), chr(9815), chr(9813), chr(9812), chr(9817), "♙", "♖", "♘", "♗", "♕", "♔"), (chr(9820), chr(9822), chr(9821), chr(9819), chr(9818), chr(9823), "♟", "♜", "♞", "♝", "♛", "♚")
new_c_x, new_c_y, new_u_coords, counter, piece_list, white_kill, black_kill, white_castling_checker, black_castling_checker, king_breaker, black_check, white_check, white_king, black_king, white_add, black_add, back, inloop, printer, passant, blockage, add, winner = 0, 0, "0z", 0, [], 0, 0, True, True, False, False, False, chr(9812), chr(9818), 1, -1, False, True, True, True, False, 1, ""


# =============================================================================
# piece movement
# =============================================================================


def pawn(board, print_board, init_c_x, init_c_y, black_list, new_coords_choice, update_board, y_dict, white_list, kill, en_passant, white_promotion_dict, black_promotion_dict, selection, king_breaker, movement):
    global back, white_check, black_check, counter, inloop, passant
    if counter % 2 == 0:                        # variables that make the function usable for pawns from either team
        initial_x, a, piece_list, final_x, promotion_dict, passant_x, opponent, opponent_king, opp_list, add, check, king = 7, -1, black_list, 1, white_promotion_dict, 4, chr(9823), chr(9818), black_list, black_add, white_check, chr(9812)
    elif counter % 2 == 1:
        initial_x, a, piece_list, final_x, promotion_dict, passant_x, opponent, opponent_king, opp_list, add, check, king = 2, 1, white_list, 8, black_promotion_dict, 5, chr(9817), chr(9812), white_list, white_add, black_check, chr(9818)
    inloop, passant = True, True
    while inloop:
        new_coords_choice(y_dict)
        if back:
            inloop, back = False, False
            break


        new_piece = board[new_c_x][new_c_y]
        for i in range(-1, 2, 2):               # calls for en passant function
            if init_c_x == passant_x and board[init_c_x][init_c_y+i] == opponent and new_c_y == init_c_y+i and board[new_c_x][new_c_y] == " ":
                en_passant(board, new_c_x, new_c_y, print_board, kill_dict, selection, init_u_coords ,new_u_coords, counter, u_y_dict, white_list, black_list)




        if init_c_x == initial_x:           # checks for movement if pawn has not been moved yet
            for i in range(-1, 2, 2):
                if board[init_c_x+a][init_c_y+i] in piece_list:     # if the pawn is killing a piece
                    if new_c_x == init_c_x+a and new_c_y == init_c_y+i:
                        movement(kill, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
                        break
                    elif new_c_x == init_c_x+a and new_c_y == new_c_y and board[new_c_x][new_c_y] == " ":   # if it is moving just one space
                        movement(update_board, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
                        break
            if (new_c_x == init_c_x+(2*a) or new_c_x == init_c_x+a) and new_c_y == init_c_y and board[new_c_x][new_c_y] == " ":     # if it is moving 2 spaces
                if new_c_x == init_c_x+(2*a):
                    if board[new_c_x-1][new_c_y] != " ":
                        continue
                movement(update_board, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
                break
        else:               # general movement of pawn on any other position on the board
            if passant:
                for i in range(-1, 2, 2):
                    if board[init_c_x+a][init_c_y+i] in piece_list:         # if it can kill a piece
                        if new_c_x == init_c_x+a and new_c_y == init_c_y+i:
                            movement(kill, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
                        elif new_c_x == init_c_x+a and new_c_y == new_c_y and board[new_c_x][new_c_y] == " ":


                            movement(update_board, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
                            break
                    else:
                        if new_c_x == init_c_x+a and new_c_y == new_c_y and board[new_c_x][new_c_y] == " ":
                            movement(update_board, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
                            break


        if new_piece != opponent_king:
            if new_c_x == final_x:          # promotion of a pawn if it reaches the end of the board
                init_sel, promote = selection, ""
                print("\n", "What would you like to promote ", kill_dict[selection], " (", new_u_coords, ") to?", sep = "")
                while promote not in promotion_dict:
                    promote = input().title()
                board[new_c_x][new_c_y] = promotion_dict[promote]
                selection = board[new_c_x][new_c_y]
                print_board(board)
                promotion_statement =  kill_dict[init_sel] + " (" + new_u_coords[0:2] + ") has been promoted to " + kill_dict[selection]
                print("\n", promotion_statement)
                with open ("moves.txt", "a") as c1:
                    c1.write(promotion_statement + "\n")


        if inloop == False:
            break
        print("Invalid move!")


def rook(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, movement, straight_block):         # elephant
    global back, counter, white_check, black_check, inloop, blockage
    counter_checker(counter, white_list, black_list)
    if counter % 2 == 0:
        king, add, check, opp_list = chr(9812), black_add, white_check, black_list
    elif counter % 2 == 1:
        king, add, check, opp_list = chr(9818), white_add, black_check, white_list
        inloop = True
    while inloop:
        new_coords_choice(y_dict)
        if back:
            back = False
            break


        if (board[new_c_x][new_c_y] == " " or board[new_c_x][new_c_y] in piece_list) and (new_c_y == init_c_y or new_c_x == init_c_x):
            straight_block(board, new_c_x, init_c_x, new_c_y, init_c_y)
            if blockage:
                print("Path blocked! Invalid move!")
                continue
            elif blockage == False:
                movement(kill, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
        if inloop == False:
            break
        print("Invalid move!")


def knight(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, movement):       # ek do dhai
    global back, counter, white_check, black_check, inloop
    counter_checker(counter, white_list, black_list)
    if counter % 2 == 0:
        king, add, check, opp_list = chr(9812), black_add, white_check, black_list
    elif counter % 2 == 1:
        king, add, check, opp_list = chr(9818), white_add, black_check, white_list
    inloop = True
    while inloop:
        new_coords_choice(y_dict)
        if back:
            back, inloop = False, False


        for i in range(-2, 3, 4):
            if (board[new_c_x][new_c_y] == " " or board[new_c_x][new_c_y] in piece_list) and ((new_c_x == init_c_x+i and (new_c_y == init_c_y+(i//2) or new_c_y == init_c_y-(i//2))) or ((new_c_x == init_c_x+(i//2) or new_c_x == init_c_x-(i//2)) and new_c_y == init_c_y+i)):
                movement(kill, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
        if inloop == False:
            break
        print("Invalid move!")


def bishop(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, movement, diagonal_block, breaker):
    global back, counter, white_check, black_check, inloop, blockage, add
    counter_checker(counter, white_list, black_list)
    if counter % 2 == 0:
        king, add, check, opp_list = chr(9812), black_add, white_check, black_list
    elif counter % 2 == 1:
        king, add, check, opp_list = chr(9818), white_add, black_check, white_list
    inloop = True
    while inloop:
        new_coords_choice(y_dict)
        change = abs(new_c_y - init_c_y)        # horizontal distance covered. if horizontal distance == vertical distance, move is valid
        if back:
            back = False
            break


        if (board[new_c_x][new_c_y] == " " or board[new_c_x][new_c_y] in piece_list) and ((new_c_x == init_c_x+change or new_c_x == init_c_x-change) and (new_c_y == init_c_y+change or new_c_y == init_c_y-change)):
            diagonal_block(board, new_c_x, init_c_x, new_c_y, init_c_y, change)
            if blockage:
                print("Path blocked! Invalid move!")
                continue
            elif blockage == False:
                movement(kill, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
        if inloop == False:
            break
        print("Invalid move!")


def queen(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, movement, diagonal_block, straight_block, breaker):
    global back, counter, white_check, black_check, inloop, blockage, add
    counter_checker(counter, white_list, black_list)
    inloop = True
    if counter % 2 == 0:
        king, add, check, opp_list = chr(9812), black_add, white_check, black_list
    elif counter % 2 == 1:
        king, add, check, opp_list = chr(9818), white_add, black_check, white_list
    while inloop:             # queen's movement is basically a combination of rook's and bishop's, so code for her is copy-paste of both their codes
        new_coords_choice(y_dict)
        change = abs(new_c_y - init_c_y)
        if back:
            back = False
            break


        if (board[new_c_x][new_c_y] == " " or board[new_c_x][new_c_y] in piece_list) and (((new_c_x == init_c_x+change or new_c_x == init_c_x-change) and (new_c_y == init_c_y+change or new_c_y == init_c_y+change)) or (new_c_y == init_c_y or new_c_x == init_c_x)):
            if (new_c_x == init_c_x+change or new_c_x == init_c_x-change) and (new_c_y == init_c_y+change or new_c_y == init_c_y+change):       # if queen is moving diagonally
                diagonal_block(board, new_c_x, init_c_x, new_c_y, init_c_y, change)
            elif new_c_y == init_c_y or new_c_x == init_c_x:            # if queen is moving in a straight line
                straight_block(board, new_c_x, init_c_x, new_c_y, init_c_y)
            if blockage:
                print("Path blocked! Invalid move!")
                continue
            elif blockage == False:
                movement(kill, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
        if inloop == False:
            break
        print("Invalid move!")


def king(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, selection, checker, movement):
    global white_castling_checker, black_castling_checker, counter, back, white_check, black_check, inloop
    if counter % 2 == 0:
        opp_list, initial_x, castling_checker, add, king, check = black_list, 8, white_castling_checker, black_add, chr(9812), white_check
    elif counter % 2 == 1:
        opp_list, initial_x, castling_checker, add, king, check = white_list, 1, black_castling_checker, white_add, chr(9818), black_check
    inloop = True
    while inloop:
        new_coords_choice(y_dict)
        if back:
            back, inloop = False, False
            break


        if castling_checker:            # for castling
            for i in range (-2, 3, 4):
                if new_c_x == initial_x and init_c_y == 5 and new_c_y == 5+i:
                    if i == 2:
                        if board[new_c_x][6] == " " and board[new_c_x][7] == " ":
                            board[new_c_x][7], board[new_c_x][6] = selection, board[new_c_x][8]
                            original_1, original_2 = board[new_c_x][init_c_y], board[new_c_x][8]
                            board[new_c_x][init_c_y], board[new_c_x][8] = " ", " "
                            checker(board, opp_list, king, add)
                            if selection in white_list:
                                check = white_check
                            elif selection in black_list:
                                check = black_check
                            if check:
                                print("Invalid move!")
                                selection, board[new_c_x][8] = board[new_c_x][7], board[new_c_x][6]
                                board[new_c_x][init_c_y], board[new_c_x][8] = original_1, original_2
                                inloop, counter = False, counter - 1
                                break
                            else:
                                print("\n", "Castled!", "\n", sep = "")
                                print_board(board)
                                inloop, castling_checker = False, False
                    elif i == -2:
                        if board[new_c_x][2] == " " and board[new_c_x][3] == " " and board[new_c_x][4] == " ":
                            board[new_c_x][2], board[new_c_x][3], board[new_c_x][4] = board[init_c_x][init_c_y], selection, board[new_c_x][1]
                            original_3, original_4 = board[init_c_x][init_c_y], board[new_c_x][1]
                            board[init_c_x][init_c_y], board[new_c_x][1] = " ", " "
                            checker(board, opp_list, king, add)
                            if selection in white_list:
                                check = white_check
                            elif selection in black_list:
                                check = black_check
                            if check:
                                print("Invalid move!")
                                board[init_c_x][init_c_y], selection, board[new_c_x][1] =  board[new_c_x][2], board[new_c_x][3], board[new_c_x][4]
                                board[init_c_x][init_c_y], board[new_c_x][1] = original_3, original_4
                                inloop, counter = False, counter - 1
                                break
                            else:
                                print("\n", "Castled!", "\n", sep = "")
                                print_board(board)
                                inloop, castling_checker = False, False
        for i in range (-1, 2, 2):
            if (board[new_c_x][new_c_y] == " " or board[new_c_x][new_c_y] in opp_list) and ((new_c_x == init_c_x and new_c_y == init_c_y+i) or (new_c_y == init_c_y and new_c_x == init_c_x+i) or (new_c_x == init_c_x+i and new_c_y == init_c_y+i) or (new_c_x == init_c_x-i and new_c_y == init_c_y+i)):
                movement(kill, board, checker, new_c_x, init_c_x, new_c_y, init_c_y, opp_list, king, add, white_list, black_list, check)
        if inloop == False:
            break
        print("Invalid move!")


# =============================================================================
# interface
# =============================================================================


print("\n", "Welcome to CHESS!", "\n")
print_board(board)


while True:
    if king_breaker:
        break
    breaker, selection, trapped, init_u_coords, init_u_x, init_u_y, init_c_x, init_c_y, moves_kill = False, "", True, "0z", 0, "0", 0, 0, False
    checker(board, black_list, white_king, black_add)       # checks if white king is checked
    checker(board, white_list, black_king, white_add)       # checks if black king is checked
    if counter % 2 == 0:
        if printer:
            print("\n", "Player 1's turn:", sep = "")
            if white_check:
                print("The White King is under check!")
            if black_check:
                print("The Black King is under check!")
        piece_list, you, opponent, printer = white_list, "Player 1", "Player 2", True
    elif counter % 2 == 1:
        if printer:
            print("\n", "Player 2's turn:", sep = "")
            if white_check:
                print("The White King is under check!")
            if black_check:
                print("The Black King is under check!")
        piece_list, you, opponent, printer = black_list, "Player 2", "Player 1", True


    select(board, piece_list, y_dict, trapped, pawn, rook, knight, bishop, queen, king, select)
    if breaker:
        break
    print("You have selected", kill_dict[selection])
    if selection == chr(9817) or selection == chr(9823):
        pawn(board, print_board, init_c_x, init_c_y, black_list, new_coords_choice, update_board, y_dict, white_list, kill, en_passant, white_promotion_dict, black_promotion_dict, selection, king_breaker, movement)
    elif selection == chr(9814) or selection == chr(9820):
        rook(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, movement, straight_block)
    elif selection == chr(9816) or selection == chr(9822):
        knight(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, movement)
    elif selection == chr(9815) or selection == chr(9821):
        bishop(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, movement, diagonal_block)
    elif selection == chr(9813) or selection == chr(9819):
        queen(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, movement, diagonal_block, straight_block, breaker)
    elif selection == chr(9812) or selection == chr(9818):
        king(board, print_board, init_c_x, init_c_y, black_list, white_list, new_coords_choice, kill, selection, checker, movement)


    if moves_kill == False:
        if new_u_coords.lower() != "back":
            statement = kill_dict[selection] + " moved from " + init_u_coords[0:2] + " to " + new_u_coords[0:2] + "\n"
            with open ("moves.txt", "a") as c1:
                c1.write(statement)


    counter += 1


# =============================================================================
# Data Management
# =============================================================================


import pymysql as pm


transcript_choice = ""
while transcript_choice not in ["y", "n"]:
    transcript_choice = (input("Would you like to save a transcript of this game (y/n): ")).lower()
if transcript_choice == "y":
    filename = " "
    print("Note: If the filename already exists, its contents will be overwritten.")
    while " " in filename:
        filename = input("Please type what you would like to call this game (no spaces, 15 chars max): ")  + ".txt"
    with open(filename, "w") as c2:
        with open("moves.txt", "r") as c1:
            transcript = c1.read()
            c1.seek(0)
            linecount = len(c1.readlines()) - 1
        c2.write(transcript)
        print(filename, "has been saved on your system successfully.")


    if winner != "draw":
        connection = pm.connect(host = "localhost", user = "root", database = "chess1", password = "rajSim#1873")
        cursor = connection.cursor()
        cursor.execute("select count(*) from leaderboard;")
        leaderboard_len = cursor.fetchall()[0][0]
        cursor.execute("select moves from leaderboard;")
        try:
            top_moves = cursor.fetchall()[0]
            top_move = max(top_moves)
        except IndexError:
            top_move = linecount + 1
        if linecount < top_move:
            if leaderboard_len < 10:
                p1, p2 = input("Enter Player 1's name (12 chars max): "), input("Enter Player 2's name (12 chars max): ")
                if winner == "Player 1":
                    winner = p1
                else:
                    winner = p2
                cursor.execute("insert into leaderboard values('{}', '{}', '{}', '{}', {});".format(filename.rstrip(".txt"), p1, p2, winner, linecount))
                connection.commit()
            else:
                cursor.execute("delete from leaderboard where Moves = '{}';".format(top_move))
                connection.commit()
                cursor.execute("insert into leaderboard values('{}', '{}', '{}', '{}', {});".format(filename.rstrip(".txt"), p1, p2, winner, linecount))
            print("This game has been added to the top 10 leaderboard!")