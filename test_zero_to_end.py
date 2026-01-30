from ZeroToEnd import MoveZerosToEnd

def test_move_zeros_basic():
    arr = [1, 2, 0, 4, 0, 5]
    result = MoveZerosToEnd(arr, len(arr))
    assert result == [1, 2, 4, 5, 0, 0]

def test_no_zeros():
    arr = [1, 2, 3]
    result = MoveZerosToEnd(arr, len(arr))
    assert result == [1, 2, 3]
