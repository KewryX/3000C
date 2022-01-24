#3. Írjuk ki az első 19-cel osztható szám indexét!
def _19cel_oszthato(lista):
    print("3. Írjuk ki az első 19-cel osztható szám indexét!")
    i = 0
    while (i < len(lista) and not i %19==0):        
        i += 1
    if i == len(lista):
        print("nincs")
    else:
        return i