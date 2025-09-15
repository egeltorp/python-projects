# Laboration 4, del 1
# 2025-09-16
# Theodor Holmberg

# func to create the chocolate bar matrix
def create_chocolate_bar(rows: int, cols: int):
    # error handling
    if rows <= 0 or cols <= 0:
        return None

    # matrix
    chocolate = []
    for r in range(1, rows + 1):
        row = []
        for c in range(1, cols + 1):
            row.append(f"{r}{c}")
        chocolate.append(row)
    return chocolate

# print chocolate bar in a formatted table
def print_chocolate_bar(matrix):
    for row in matrix:
        print("  ".join(row))

# func to 'chomp' away pieces of the chocolate bar
def chomp(chocolate: bar, row: int, col: int):
    pass

choco = create_chocolate_bar(5, 5)
print_chocolate_bar(choco)

