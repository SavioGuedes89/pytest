from piso import piso

def test_piso1():
    return piso(3,5) == [23 , 12]

def test_piso2():
    return piso(1,1) == [1 , 0]