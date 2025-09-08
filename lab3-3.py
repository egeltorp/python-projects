antal_tärningar = int(input("Hur många tärningar behövs i spelet? "))
antal_kast = int(input("Hur många kast får en spelare? "))

while True:
    for i in range(antal_kast):
        if i == 0:
            q = input("Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A: ")
            if q == "A":
                break
        
        
        