def kicsifele(lista):
    print("10. Mennyi a sorozatban található legkisebb szám fele?")
    min=lista[0]
    for e in lista:
        if e<min:
            min=e
    print(min/2)