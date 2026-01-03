import pytest

def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def test_additionner():
    assert additionner(5, 3) == 8
    assert additionner(-5, 3) == -2
    assert additionner(-5, -3) == -8

def test_soustraire():
    assert soustraire(5, 3) == 2
    assert soustraire(-5, 3) == -8
    assert soustraire(-5, -3) == -2

def test_multiplier():
    assert multiplier(5, 3) == 15
    assert multiplier(-5, 3) == -15
    assert multiplier(-5, -3) == 15

def test_additionner_type():
    with pytest.raises(TypeError):
        additionner(5, 'a')

def test_soustraire_type():
    with pytest.raises(TypeError):
        soustraire(5, 'a')

def test_multiplier_type():
    with pytest.raises(TypeError):
        multiplier(5, 'a')