
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        # printBoard(board
    return


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove(i):
    insertLetter(player, i)
    return


def playerMove_adjacent(before, after):
    board[before] = ' '
    insertLetter(player, after)
    return


def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)

    return bestMove


def compMove_adjacent():
    place_x = []
    place_empty = []

    possible = []

    for key in board.keys():
        if (board[key] == 'X'):
            place_x.append(key)

    for key in board.keys():
        if (board[key] == ' '):
            place_empty.append(key)

    count = 0

    for before in place_x:
        for after in place_empty:
            if move_restriction(before, after):
                # print("[before: " + str(before) + ", after: " + str(after) + "]")
                possible.append([before, after])
                count += 1

    bestScore = -800
    bestMove = (0, 0)

    for i, (before, after) in enumerate(possible):
        board[before] = ' '
        board[after] = bot
        score = minimax(board, 0, False)
        board[after] = ' '
        board[before] = bot
        # print("score: " + str(score))

        if (score > bestScore):
            bestScore = score
            bestMove = (before, after)

    # print(bestMove)
    board[bestMove[0]] = ' '
    insertLetter(bot, bestMove[1])

    return bestMove


def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


def move_restriction(before, after):
    available_or_not = True

    if before == 1:
        if after == 2 or after == 4 or after == 5:
            available_or_not = True
        else:
            available_or_not = False

    if before == 2:
        if after == 1 or after == 3 or after == 5:
            available_or_not = True
        else:
            available_or_not = False

    if before == 3:
        if after == 2 or after == 5 or after == 6:
            available_or_not = True
        else:
            available_or_not = False

    if before == 4:
        if after == 1 or after == 5 or after == 7:
            available_or_not = True
        else:
            available_or_not = False

    if before == 5:
        if after == 1 or after == 2 or after == 3 or after == 4 or after == 6 or after == 7 or after == 8:
            available_or_not = True
        else:
            available_or_not = False

    if before == 6:
        if after == 3 or after == 5 or after == 9:
            available_or_not = True
        else:
            available_or_not = False

    if before == 7:
        if after == 4 or after == 5 or after == 8:
            available_or_not = True
        else:
            available_or_not = False

    if before == 8:
        if after == 5 or after == 7 or after == 9:
            available_or_not = True
        else:
            available_or_not = False

    if before == 9:
        if after == 5 or after == 6 or after == 8:
            available_or_not = True
        else:
            available_or_not = False

    return available_or_not


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

player = 'O'
bot = 'X'
score_array = []

global firstComputerMove
firstComputerMove = True

