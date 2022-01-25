#9. Van-e a sorozatban olyan negatív szám, amelyet pozitív követ?
def negativ_utan_pozitiv(lista):
    print("9. Van-e a sorozatban olyan negatív szám, amelyet pozitív követ?")
  
    i = 0
    
    while i < len(lista)-1 and not (lista[i] < 0 and lista[i+1] > 0):                
        i+=1

    if i == len(lista):
        print("nincs")
    else:
        print("van")