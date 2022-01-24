
from mate1 import vane
from mate3 import _19cel_oszthato
lista = []
with open('03_000.txt',"r", encoding="utf8") as f:
    for sor in f:
        lista.append(sor)

vane(lista)

_19cel_oszthato(lista)