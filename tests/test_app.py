from app import add


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_and_positive_number():
    assert add(-1, 4) == 3
