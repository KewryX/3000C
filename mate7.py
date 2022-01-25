#7. Írjuk ki a sorozatban található 15-tel osztható számok felét!
def _15tel_osztahato_fele(lista):
    print("7. Írjuk ki a sorozatban található 15-tel osztható számok felét!")
    for e in lista:
        if e % 15 == 0:
            print(e/2)