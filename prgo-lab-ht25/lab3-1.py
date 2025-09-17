# Uppgift 1: Celsius till Fahrenheit
# Theodor Holmberg
# 2025-09-08

print("C \t F")
print("--\t --")

for c in range(0, 21):            
    f = (c * 9 + 160) / 5
    print(f"{c} \t {f:.1f}")
