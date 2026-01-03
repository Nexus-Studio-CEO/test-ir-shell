import pytest

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

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
    assert is_even(-2) == True
    assert is_even(-3) == False

def test_is_even_zero():
    assert is_even(0) == True

def test_add_negative_numbers():
    assert add(-5, -7) == -12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0

def test_is_even_negative():
    assert is_even(-10) == True
    assert is_even(-11) == False