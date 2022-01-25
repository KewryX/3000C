#5. Igaz-e, hogy minden szám nagyobb, mint 10?


def nagyobb_mint_10(lista):
    print("5. Igaz-e, hogy minden szám nagyobb, mint 10?")
    igaze = True
    i = 0
    while i < len(lista) and not igaze:
        if lista[i] <= 10:
            igaze = False
        i += 1

    return igaze
