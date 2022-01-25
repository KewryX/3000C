lista = []
with open('03_000.txt',"r", encoding="utf8") as f:
    for sor in f:
        lista.append(int(sor))