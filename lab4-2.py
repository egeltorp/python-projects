# Chomp Game
# 2025-09-16
# Theodor Holmberg

def intro():
    print("\n--- Välkommen till Chomp ---")
    print("* I spelet kommer du utmanas om att välja ett blocknummer från spelplanen.")
    print("* Det valda blocket och alla block under och till högre kommer att raderas.")
    print("* Spelet går ut på att undvika att välja P, den spelare som väljer P förlorar och den andra spelaren vinner.")
    print()

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
    print()
    for row in matrix:
        print("  ".join(f"{col:>3}" for col in row))

# func to 'chomp' away pieces of the chocolate bar
def chomp(matrix: list, row: int, col: int):
    if row < 0 or col < 0:
        return None

    result = []
    for r in range(row, len(matrix)):
        del matrix[r][col:]

    for r in range(len(matrix) - 1, -1, -1):
        if not matrix[r]:
            del matrix[r]
    return matrix

def check_winner(matrix: list):
    return len(matrix) == 1

def ask_cell_number(matrix: list):
    while True:
        try:
            choice = input("> Välj en ruta: ").strip()
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

def play():
    # print instructions
    intro()

    # ask for board (matrix) size
    rows = max(2, min(9, int(input("[?] Hur många rader ska chokladbaren bestå av (2-9): "))))
    cols = max(2, min(9, int(input("[?] Hur många kolumner ska chokladbaren bestå av (2-9): "))))

    # generate first matrix using user-input values
    matrix = create_chocolate_bar(rows, cols)
    print_chocolate_bar(matrix)

    current_player = 1

    while True:
        # print whose turn it is
        if current_player == 1:
            print("\nFörsta spelarens tur")
        elif current_player == 2:
            print("\nAndra spelarens tur")

        # ask which cell to chomp
        row,col = ask_cell_number(matrix)

        # alter matrix using row,col indices
        matrix = chomp(matrix, row, col)

        # check after each chomp, before printing matrix
        if check_winner(matrix) == True:
            break

        # print new matrix
        print_chocolate_bar(matrix)

        # change current player, 3-1=2, 3-2=1, alternating each loop
        current_player = 3 - current_player

    print(f"\n---> Endast P kvar. Spelare {current_player} vinner!")

if __name__ == "__main__":
    play()
