from huyna.core import even_only

def test_even_only_basic():
    assert even_only([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

def test_empty():
    assert even_only([]) == []

def test_negatives():
    assert even_only([-3, -2, -1, 0, 1, 2]) == [-2, 0, 2]
