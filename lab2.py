import time
import sys
import os

# Uppgift 1: Bränsleförbrukning 
def uppgift_1():
    körsträcka_i_km = float(input("Ange körsträcka i km: "))

    liter_bränsle_förbrukat = float(input("Ange antal liter bränsle förbrukat: "))

    bränsleförbrukning_per_100km = (liter_bränsle_förbrukat / körsträcka_i_km) * 100

    print("\n> Bränsleförbrukningen för bilen är " + str(round(bränsleförbrukning_per_100km, 3)) + " L/100 km.")

# Uppgift 2: If-satser
def uppgift_2():
    paket_vikt_kg = float(input("Ange paketets vikt (kg): "))

    # Pristabell
    if paket_vikt_kg < 2:
        pris_per_kg = 30
    elif paket_vikt_kg < 6:
        pris_per_kg = 28
    elif paket_vikt_kg < 12:
        pris_per_kg = 25
    else:
        pris_per_kg = 23

    # Beräkning och resultat
    total_kostnad = paket_vikt_kg * pris_per_kg
    print("> Paketet kommer att kosta " + str(round(total_kostnad, 2)) + " kr att skicka.")

# Uppgift 3: Slingor
def uppgift_3():
    antal_paket = int(input("Ange hur många paket du vill skicka: "))
    total_kostnad = 0
    i = 1

    while i <= antal_paket:
        vikt = float(input("Ange vikt för paket " + str(i) + " (kg): "))

        if vikt < 2:
            pris_per_kg = 30
        elif vikt < 6:
            pris_per_kg = 28
        elif vikt < 12:
            pris_per_kg = 25
        else:
            pris_per_kg = 23
        
        total_kostnad += vikt * pris_per_kg
        i += 1

    print("\n> Det kommer att kosta " + str(round(total_kostnad, 2)) + " kr att skicka alla " + str(antal_paket) + " paket.")

# --- Intro-text ---
def display_ascii_art():
    ascii_art = '''
  _       _    ___  
 | |     | |  |__ \ 
 | | __ _| |__   ) |
 | |/ _` | '_ \ / / 
 | | (_| | |_) / /_ 
 |_|\__,_|_.__/____|
                   
'''
    # Printa varje rad för sig med 0.05 sekunder delay
    # Cool animering
    for line in ascii_art.splitlines():
        print(line, flush=True)
        time.sleep(0.05)

# --- Sekvens ---
def main():
    while True:
        display_ascii_art() # Visa Ascii-konst vid startup

        print("--- Uppgift 1: Bränsleförbrukning ---")
        uppgift_1()
        print()

        print("--- Uppgift 2: If-satser ---")
        uppgift_2()
        print()

        print("--- Uppgift 3: Slingor ---")
        uppgift_3()
        print()

        igen = input("Vill du köra programmet igen? (y/n): ")
        if igen != "y":
            sys.exit()
        else:
            os.system("clear")

if __name__ == "__main__":
    main()