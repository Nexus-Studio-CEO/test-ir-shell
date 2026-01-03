import pytest

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def is_even(x):
    return x % 2 == 0

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(-2, -3) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True

def test_add_type_error():
    with pytest.raises(TypeError):
        add(2, 'a')

def test_multiply_type_error():
    with pytest.raises(TypeError):
        multiply(2, 'a')

def test_is_even_type_error():
    with pytest.raises(TypeError):
        is_even('a')