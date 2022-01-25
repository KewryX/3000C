def _7tel_oszthato(lista):
    print("2. Írjuk ki az utolsó 7-tel osztható szám indexét!")

    i = len(lista)-1
    while i>=0 and not lista[i]%7==0: 
        i-=1
    print(i) 
    
