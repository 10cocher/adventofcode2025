import pytest

from src.day01 import get_score


@pytest.mark.parametrize(
    "position,position_temp,expected",
    [
        (2, 3, 0),
        (2, 0, 1),
        (0, 2, 0),
        (0, 99, 0),
        (0, 100, 1),
        (0, 101, 1),
        (0, 199, 1),
        (0, 200, 2),
        (0, 201, 2),
        (1, 99, 0),
        (1, 100, 1),
        (1, 101, 1),
        (5, -5, 1),
        (0, -1, 0),
        (0, -99, 0),
        (1, -99, 1),
        (0, -100, 1),
        (1, -100, 2),
        (0, -101, 1),
        (1, -101, 2),
        (0, -200, 2),
        (1, 0, 1),
        (1, -1, 1),
    ],
)
def test_get_score(position: int, position_temp: int, expected: int) -> None:
    assert get_score(position, position_temp) == expected
