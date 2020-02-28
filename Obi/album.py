def album(N,C,M,FCar, FCcmp):
    if(len(FCar) != C):
        return 0
    if(len(FCcmp) != M):
        return 0    
    cont = 0
    Posu = []
    for figCon in FCcmp :
        if(figCon in Posu):
            cont = cont
        else:
            Posu.append(figCon)
            if(figCon in FCar):
                cont = cont +1
        
    return C - cont
        

        
    