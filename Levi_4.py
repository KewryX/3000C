
def atlag_negyzet(lista):
    print("4. Mennyi a sorozatban található számok átlagának a négyzete?")
    
    sum=0
    atlag=0
    for e in lista:
        sum+=e
    atlag=sum/len(lista)
    print(atlag**2)

