from copy import deepcopy


RED = (255, 0, 0)
GREEN = (124, 252, 0)


def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        max_eval = float("-inf")
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            if max_eval < evaluation:
                max_eval = evaluation
                best_move = move

        return max_eval, best_move
    else:
        min_eval = float("inf")
        best_move = None
        for move in get_all_moves(position, GREEN, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            if min_eval > evaluation:
                min_eval = evaluation
                best_move = move

        return min_eval, best_move


def simulate_move(piece, move, board, game, skip):
    print("move", move)
    board.move(piece, move[0], move[1])  # also move[0] mean row and move[1] mean col
    if skip:  # if we jump over the piece
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        print(valid_moves)
        for (move_row, move_col) in valid_moves:
            skip = valid_moves[(move_row, move_col)]
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, (move_row, move_col), temp_board, game, skip)
            moves.append(new_board)

    return moves
