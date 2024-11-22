%%writefile main.py
from Chessnut import Game
import random

# Piece value for evaluating captures (optional: can be expanded)
piece_value = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 100}

def chess_bot(obs):

    # 0. Parse the current board state and generate legal moves using Chessnut library
    game = Game(obs.board)
    moves = list(game.get_moves())

    # 1. Filter out moves that would leave the king in check
    valid_moves = []
    for move in moves:
        g = Game(obs.board)
        g.apply_move(move)
        if g.status != Game.CHECK:
            valid_moves.append(move)
    
    if not valid_moves:
        # If all moves leave the king in check, return a random move as fallback
        return random.choice(moves)
    
    # 2. Check for checkmate moves
    for move in valid_moves[:10]:  # Limit to first 10 moves for efficiency
        g = Game(obs.board)
        g.apply_move(move)
        if g.status == Game.CHECKMATE:
            return move

    # 3. Check for captures (prioritizing high-value pieces)
    best_capture = None
    highest_value = 0
    for move in valid_moves:
        target_piece = game.board.get_piece(Game.xy2i(move[2:4]))
        if target_piece != ' ' and piece_value.get(target_piece.upper(), 0) > highest_value:
            best_capture = move
            highest_value = piece_value[target_piece.upper()]

    if best_capture:
        return best_capture

    # 4. Check for queen promotions
    for move in valid_moves:
        if "=" in move:  # Identify promotion moves (e.g., "a7a8q")
            return move

    # 5. Handle checks defensively
    if game.status == Game.CHECK:
        for move in valid_moves:
            g = Game(obs.board)
            g.apply_move(move)
            if g.status != Game.CHECK:
                return move

    # 6. Default to a random move from valid moves
    return random.choice(valid_moves)
