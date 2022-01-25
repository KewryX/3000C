
from distutils.version import LooseVersion
from mate1 import vane
from Levi_2 import _7tel_oszthato
from mate3 import _19cel_oszthato

from mate5 import nagyobb_mint_10

from mate7 import _15tel_osztahato_fele

from mate9 import negativ_utan_pozitiv
lista = []
with open('03_000.txt',"r", encoding="utf8") as f:
    for sor in f:
        lista.append(int(sor))

vane(lista)
_7tel_oszthato(lista)
_19cel_oszthato(lista)

nagyobb_mint_10(lista)

_15tel_osztahato_fele(lista)

negativ_utan_pozitiv(lista)