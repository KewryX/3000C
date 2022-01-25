def _9cel_sum(lista):
    print("6. Hány 9-cel osztható szám található a sorozatban?")
    
    oszthato=0
    for e in lista:
        if e%9==0:
            oszthato+=1
        
    print(oszthato)
