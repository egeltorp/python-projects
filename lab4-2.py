# Laboration 4, del 1
# 2025-09-16
# Theodor Holmberg

# func to create the chocolate bar matrix
def create_chocolate_bar(rows: int, cols: int):
    if rows <= 0 or cols <= 0:
        return None
    chocolate = []
    for r in range(1, rows + 1):
        row = []
        for c in range(1, cols + 1):
            row.append(f"{r}{c}")
        chocolate.append(row)
    chocolate[0][0] = "P" # --> 'poison' 1st square
    return chocolate

# print matrix in a formatted table
def print_chocolate_bar(matrix):
    for row in matrix:
        print("  ".join(f"{col:>3}" for col in row))

# func to 'chomp' away pieces of the chocolate bar
def chomp(matrix: list, row: int, col: int):
    if row < 0 or col < 0:
        return None

    result = []
    # loops for each row, checks if row is before chomp -> 
    # if true: keeps that row intact, appends to result
    for r in range(len(matrix)):
        if r < row:
            # save whole row
            result.append(matrix[r][:])
        else:
            # save only up to col index
            result.append(matrix[r][:col])
    return result

def check_winner(matrix: list):
    return matrix == ["P"]

def ask_cell_number(matrix: list):
    while True:
        try:
            choice = input("Välj en ruta: ").strip()
            if len(choice) != 2 or not choice.isdigit():
                raise ValueError 

            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    if matrix[row][col] == choice:
                        return (row, col)
            print(f"Ogiltigt val, ruta {choice} finns inte. Försök igen!")

        except ValueError:
            print("Ogiltig input, försök igen!")
            continue

print_chocolate_bar(create_chocolate_bar(3,4))