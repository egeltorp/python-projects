# Laboration 4, del 1
# 2025-09-16
# Theodor Holmberg

# func to create the chocolate bar
def create_chocolate_bar(rows: int, cols: int):
    # empty matrix
    chocolate = []

    for r in range(1, rows + 1):
        row = []
        for c in range(1, cols + 1):
            row.append(f"{r}{c}")
        chocolate.append(row)
    
    return chocolate

# func to print the chocolate bar
def print_chocolate_bar():
    pass

print(create_chocolate_bar(3,4))

