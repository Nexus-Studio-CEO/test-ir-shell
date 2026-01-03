import pytest

def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def test_additionner_deux_entiers_positifs():
    assert additionner(5, 7) == 12

def test_soustraire_deux_entiers_positifs():
    assert soustraire(10, 4) == 6

def test_multiplier_deux_entiers_positifs():
    assert multiplier(3, 9) == 27

def test_additionner_un_entier_et_un_float():
    assert additionner(5, 7.5) == 12.5

def test_soustraire_un_entier_et_un_float():
    assert soustraire(10, 4.5) == 5.5

def test_multiplier_un_entier_et_un_float():
    assert multiplier(3, 9.5) == 28.5

def test_additionner_deux_entiers_negatifs():
    assert additionner(-5, -7) == -12

def test_soustraire_deux_entiers_negatifs():
    assert soustraire(-10, -4) == -6

def test_multiplier_deux_entiers_negatifs():
    assert multiplier(-3, -9) == 27