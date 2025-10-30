def play(board):
    # Set all possible winning combinations
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # determine whose turn it is
    x_count = board.count('x')
    o_count = board.count('o')
    turn = 'x' if x_count == o_count else 'o'

    # find winning or blocking move
    def find_best_move(player):
        for a, b, c in wins:
            line = [board[a], board[b], board[c]]
            if line.count(player) == 2 and line.count('') == 1:
                return [a, b, c][line.index('')]
        return None

    # Try to win
    move = find_best_move(turn)
    if move is not None:
        return move

    # Try to block opponent’s win
    opponent = 'o' if turn == 'x' else 'x'
    move = find_best_move(opponent)
    if move is not None:
        return move

    # Take center if free
    if board[4] == '':
        return 4

    # Take a corner if free
    for i in [0, 2, 6, 8]:
        if board[i] == '':
            return i

    # Take a side
    for i in [1, 3, 5, 7]:
        if board[i] == '':
            return i

    # If no moves left
    return -1
