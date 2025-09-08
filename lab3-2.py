# Uppgift 2
# Theodor Holmberg
# 2025-09-08

# fråga användaren efter antal rader och kolumner
rader = int(input("Ange antal rader: "))
kolumner = int(input("Ange antal kolumner: "))

i = 0  # Rad-index
while i < rader:
    j = 0  # Kolumn-index
    while j < kolumner:
        if (i + j) % 2 == 0:
            print("X", end="\t")
        else:
            print("O", end="\t")
        j += 1
    print()
    i += 1
