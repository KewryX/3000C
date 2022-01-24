
from mate1 import hello_vilag
lista = []
with open('input.txt',"r", encoding="utf8") as f:
    for sor in f:
        lista.append(sor)

mate1.hello_vilag()