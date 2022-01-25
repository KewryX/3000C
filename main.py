
from distutils.version import LooseVersion
from mate1 import vane
from Levi_2 import _7tel_oszthato
from mate3 import _19cel_oszthato
from Levi_4 import atlag_negyzet
from Levi_6 import _9cel_sum
from Levi_8 import szum
from Levi_10 import kicsifele
lista = []
with open('03_000.txt',"r", encoding="utf8") as f:
    for sor in f:
        lista.append(int(sor))

vane(lista)
_7tel_oszthato(lista)
_19cel_oszthato(lista)
atlag_negyzet(lista)
_9cel_sum(lista)
szum(lista)
kicsifele(lista)