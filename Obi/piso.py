def piso(L,C):
    piso2 = ((L -1)*2) + ((C-1)*2)
    piso1 = (L*C) +((L-1)*(C-1))
    return [piso1 , piso2]