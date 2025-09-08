# Uppgift 1: Celsius till Fahrenheit-
# Theodor Holmberg
# 2025-09-08

print("Celsius\tFahrenheit")
print("--------------------")

for c in range(0, 21):              # Celsius från 0 till 20
    f = (c * 9 + 160) / 5           # exakt formel enligt uppgiften
    print(f"{c}\t{f:.1f}")
