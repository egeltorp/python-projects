import random

def display_ascii_art():
    ascii_art = '''
$$\                $$\        $$$$$$\  
$$ |               $$ |      $$ ___$$\ 
$$ |      $$$$$$\  $$$$$$$\  \_/   $$ |
$$ |      \____$$\ $$  __$$\   $$$$$ / 
$$ |      $$$$$$$ |$$ |  $$ |  \___$$\ 
$$ |     $$  __$$ |$$ |  $$ |$$\   $$ |
$$$$$$$$\\$$$$$$$ |$$$$$$$  |\$$$$$$  |
\________|\_______|\_______/  \______/ 
                                                                                        
'''
    print(ascii_art)

while True:
    display_ascii_art()

    antal_tärningar = int(input("Hur många tärningar behövs i spelet? "))
    max_kast = int(input("Hur många kast får en spelare? "))

    start = input("Klicka ENTER för att starta, skriv A för att avsluta: ")
    if start.upper() == "A":
        print("Tack och hej.")
        break

    for i in range(max_kast):
        print(f"\nKast {i+1}:")
        historik: list = []
        for j in range(antal_tärningar):
            kast_värde = random.randint(1, 6)
            historik.append(kast_värde)
            print(f">Tärning {j+1}: {kast_värde}")

        # berätta kast-värden
        print(f"Du fick {', '.join(map(str, historik))}")

        # antal kast kvar, efter första omgången
        print(f"\nNu har du {max_kast - (i+1)} kast kvar.")
        
        # fråga om en omgång till, eller avsluta
        kast_kvar = max_kast - (i+1)
        if kast_kvar == 0:  
            igen = input("Vill du börja om? (Y/N): ")
        else:
            igen = input("Vill du kasta igen? (Y/N): ")

        if igen.upper() != "Y":
            print("Avslutar.")
            exit()
        elif kast_kvar == 0:
            print()
            break
    