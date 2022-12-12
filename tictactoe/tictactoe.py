matrix = [list("---"), list("---"), list("---")]  # matrix for playing field
step = "X"  # "X" takes the first step. The players move will change step by step
players = ["X", "O"]
win_combination = (matrix[0].count(step * 3) + matrix[1].count(step * 3) + matrix[2].count(step * 3) +
                   (matrix[0][0] + matrix[1][1] + matrix[2][2]).count(step * 3) +
                   (matrix[0][2] + matrix[1][1] + matrix[2][0]).count(step * 3) +
                   (matrix[0][0] + matrix[1][0] + matrix[2][0]).count(step * 3) +
                   (matrix[0][1] + matrix[1][1] + matrix[2][1]).count(step * 3) +
                   (matrix[0][2] + matrix[1][2] + matrix[2][2]).count(step * 3))
print('PLAYING FIELD')


def board():
    """function for create matrix"""

    print("_____")
    print(f"|{''.join(matrix[0])}|\n|{''.join(matrix[1])}|\n|{''.join(matrix[2])}|")
    print("_____")  # print the board


board()

while True:
    print("\nHINTS: enter coordinates separated by a \"spase\"\n")
    print(step, "Enter the coordinates:", end="")
    coordinate_input = input().split(" ", 2)  # user input coordinate

    while len(coordinate_input) != 2:  # check for correct input
        print("", step, "Enter the coordinates:", end="")
        coordinate_input = input().split(" ", 2)

    if not (coordinate_input[0].isnumeric() and coordinate_input[1].isnumeric()):  # check for correct input
        print("You should enter numbers!")
        print(step, "Enter the coordinates:", end="")
        continue

    x = int(coordinate_input[0]) - 1  # coordinate x
    y = int(coordinate_input[1]) - 1  # coordinate y

    if not (0 <= x < 3 and 0 <= y < 3):  # matrix boundary condition
        print("Coordinates should be from 1 to 3!")
        continue

    if matrix[x][y] != '-':  # check for filled cell
        print("This cell is occupied! Choose another one!")
        continue

    matrix[x][y] = step  # update board
    board()

    if win_combination == 1:  # check for winner
        print(f"{step} wins")
        break

    if '-' not in matrix[0] and '-' not in matrix[1] and '-' not in matrix[2]:  # check for filled cell
        print("Draw")
        break

    step = players[(players.index(step) - 1)]  # change player
