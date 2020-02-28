from album import album

def test_album1():
    return album(10, 2, 5,[4,7], [7,1,2,8,3]) == 1

def test_album2():
    return album(10, 2, 6,[4,7], [7,1,8,4,9,3]) == 0

def test_album4():
    return album(8, 4, 10,[2,4,6,8], [3,1,1,5,3,1,7,7,1,1]) == 4

def test_album5():
    return album(10, 2, 5,[4,7], [7,7,2,8,3]) == 1