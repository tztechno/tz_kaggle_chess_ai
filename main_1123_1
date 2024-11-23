%%writefile main.py
from Chessnut import Game


# 駒の価値を定義
piece_value = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 100}

def evaluate_board(game):
    """
    シンプルな評価関数: 現在の盤面の価値を計算
    正: 有利, 負: 不利
    """
    score = 0
    for square in range(64):  # 8x8の盤面
        piece = game.board.get_piece(square)
        if piece != ' ':
            value = piece_value.get(piece.upper(), 0)
            score += value if piece.isupper() else -value
    return score

def minimax_alpha_beta(game, depth, alpha, beta, maximizing_player):
    """
    アルファベータ剪定付きミニマックス法
    - game: 現在の盤面状態
    - depth: 探索の深さ
    - alpha: 最大化プレイヤーの下限
    - beta: 最小化プレイヤーの上限
    - maximizing_player: 自分の手番か否か (Trueなら自分)
    """
    if depth == 0 or game.status in [Game.CHECKMATE, Game.STALEMATE]:
        return evaluate_board(game)

    moves = list(game.get_moves())
    if maximizing_player:
        max_eval = float('-inf')
        for move in moves:
            g = Game(game.board)
            g.apply_move(move)
            eval = minimax_alpha_beta(g, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # 枝刈り
        return max_eval
    else:
        min_eval = float('inf')
        for move in moves:
            g = Game(game.board)
            g.apply_move(move)
            eval = minimax_alpha_beta(g, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # 枝刈り
        return min_eval

def chess_bot(obs):
    """
    3手先を読むチェスボット
    """
    game = Game(obs.board)
    moves = list(game.get_moves())
    best_move = None
    best_value = float('-inf')

    for move in moves:
        g = Game(obs.board)
        g.apply_move(move)
        board_value = minimax_alpha_beta(g, depth=3, alpha=float('-inf'), beta=float('inf'), maximizing_player=False)
        if board_value > best_value:
            best_value = board_value
            best_move = move

    return best_move
