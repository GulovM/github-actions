import pytest
from app import add, subtract, multiply, divide, is_prime


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-2, -3) == -5


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        divide(5, 0)


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False
    assert is_prime(4) is False
    assert is_prime(15) is False

