#1. Van-e a sorozatban 100-zal osztható szám?
def vane(lista):
    print("1. Van-e a sorozatban 100-zal osztható szám?")
    i = 0
    while (i < len(lista) and not lista[i] % 100 == 0):
        i += 1
    if i == len(lista):
        print("nincs")
    else:
        print("van")