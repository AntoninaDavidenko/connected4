from datetime import datetime, timezone

from ..constants import M, N, PlayerEnum
from ..core import detect_winner, mark_winner, calculate_row_by_col
from .models import Game, Move


def make_move(game: Game, col: int) -> None: 
    # make move 
    row = calculate_row_by_col(game.board, col)
    move_value = game.next_player_to_move_sign
    game.board[row][col] = move_value
    move = Move(row=row, col=col, val=move_value)
    game.moves.append(move)
    game.move_number += 1

    # handle winner 
    winner = detect_winner(game.board)
    if winner:
        mark_winner(game.board, winner)
        game.winner = PlayerEnum(winner)
        game.finished_at = datetime.now(timezone.utc)
    elif game.move_number == N * M + 1: # draw
        game.winner = None
        game.finished_at = datetime.now(timezone.utc)
     