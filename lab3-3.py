import random

while True:
    antal_tärningar = int(input("Hur många tärningar behövs i spelet? "))
    max_kast = int(input("Hur många kast får en spelare? "))

    start = input("Klicka ENTER för att starta, skriv A för att avsluta: ")
    if start.upper() == "A":
        break

    for i in range(max_kast):
        print(f"\nKast {i+1}:")
        for j in range(antal_tärningar):
            kast_värde = random.randint(1, 6)
            print(f">Tärning {j+1}: {kast_värde}")

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
    