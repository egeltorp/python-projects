# Uppgift 2: Nästlade slingor
# Theodor Holmberg
# 2025-09-08

# användaren anger antal rader och kolumner
rader = int(input("Ange antal rader: "))
kolumner = int(input("Ange antal kolumner: "))

i = 0  # rad-index
while i < rader:
    j = 0  # kolumn-index
    while j < kolumner:
        # beräkna
        if (i + j) % 2 == 0:
            print("X", end="\t")
        else:
            print("O", end="\t")
        j += 1
    print()
    i += 1
