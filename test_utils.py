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

def test_additionner_un_entier_et_un_flocon():
    with pytest.raises(TypeError):
        additionner(5, 'a')

def test_soustraire_un_entier_et_un_flocon():
    with pytest.raises(TypeError):
        soustraire(5, 'a')

def test_multiplier_un_entier_et_un_flocon():
    with pytest.raises(TypeError):
        multiplier(5, 'a')