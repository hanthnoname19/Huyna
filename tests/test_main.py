import pathlib
import sys

import pytest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from main import even_only


def test_even_only_returns_even_numbers():
    assert even_only([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_even_only_handles_negative_and_zero():
    assert even_only([-3, -2, -1, 0, 1, 2]) == [-2, 0, 2]


def test_even_only_empty_input():
    assert even_only([]) == []


def test_even_only_raises_on_non_integers():
    with pytest.raises(TypeError):
        even_only([1, 2.0, 3])


def test_even_only_none_input():
    with pytest.raises(TypeError):
        even_only(None)
