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
        print("  ".join(f"{col:>3}" for col in row))

# func to 'chomp' away pieces of the chocolate bar
def chomp(matrix: list, row: int, col: int):
    # error handling
    if row < 0 or cols < 0:
        return None

    result = []

    # reformat from user input to correct index
    # row -= 1
    # col -= 1

    # loops for each row, checks if row is before chomp -> 
    # if true: keeps that row intact, appends to result
    for r in range(len(matrix)):
        if r < row:
            # rows before the chomp stay intact, save whole row
            result.append(matrix[r][:])
        else:
            # rows at or below row get cut at col, save only up to col index
            result.append(matrix[r][:col])
    return result