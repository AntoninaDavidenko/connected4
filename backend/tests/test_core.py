import pytest 

from src.core import is_valid_move

@pytest.mark.parametrize(
    "row, col, expected",
    (
        (5, 0, True),
        (4, 0, False),
        (1, 1, False),
        (1, 4, True),
        (0, 3, False),
        (3, 2, True),
    ),
)
def test_is_valide_move(row, col, expected):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 2, 0, 0],
        [0, 0, 2, 2, 1, 0, 0],
        [0, 0, 1, 1, 2, 0, 0],
    ]
    assert is_valid_move(board, row, col) == expected