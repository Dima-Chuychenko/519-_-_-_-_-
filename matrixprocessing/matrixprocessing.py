import copy
import sys


def matrix_enter():
    print("Enter the number of lines and columns")
    size = input().split()
    matrix = []
    print("Enter numeric")
    for i in range(int(size[0])):
        line = input().split()[:int(size[1])]
        matrix.append([])
        for j in range(int(size[1])):
            matrix[i].append(float(line[j]))
    return matrix


def matrix_round(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(matrix[i][j]) if matrix[i][j] == round(matrix[i][j]) else matrix[i][j]
    return matrix


def add_matrices():
    matrix_1 = matrix_enter()
    matrix_2 = matrix_enter()
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        for o in range(len(matrix_1)):
            for k in range(len(matrix_1[0])):
                matrix_1[o][k] += matrix_2[o][k]
                matrix_1[o][k] = round(matrix_1[o][k], 1)
    print("The result is:")
    for v in matrix_round(matrix_1):
        print(" ".join(str(x) for x in v))
    print()


def multiply_matrix_by_a_constant():
    matrix_1 = matrix_enter()
    num = int(input("enter number\n"))
    for o in range(len(matrix_1)):
        for k in range(len(matrix_1[0])):
            matrix_1[o][k] *= num
            matrix_1[o][k] = round(matrix_1[o][k], 1)
    print("The result is:")
    for v in matrix_round(matrix_1):
        print(" ".join(str(x) for x in v))
    print()


def multiply_matrices():
    matrix_1 = matrix_enter()
    matrix_2 = matrix_enter()
    if len(matrix_1[0]) != len(matrix_2):
        print('Numbers of columns of first matrix and number of rows of second matrix are not equal')
        return None
    matrix = [[0 for j in range(len(matrix_2[0]))] for i in range(len(matrix_1))]
    for i in range(0, len(matrix_1)):
        for j in range(0, len(matrix_2[i])):
            result = 0
            for k in range(0, len(matrix_2)):
                result += matrix_1[i][k] * matrix_2[k][j]
            matrix[i][j] = int(result) if round(result) == 0 else result
            matrix[i][j] = round(matrix[i][j], 1)
    print("The result is:")
    for v in matrix_round(matrix):
        print(" ".join(str(x) for x in v))
    print()


def transpose_matrix():
    action = input('''1. Main diagonal 
2. Side diagonal 
3. Vertical line 
4. Horizontal line
5. Back \n''')
    match action:
        case "1":
            matrix_1 = matrix_enter()
            matrix = [[0 for j in range(len(matrix_1))] for i in range(len(matrix_1[0]))]
            for o in range(len(matrix_1)):
                for k in range(len(matrix_1[0])):
                    matrix[o][k] = matrix_1[k][o]
            print("The result is:")
            for v in matrix:
                print(" ".join(str(x) for x in v))
            print()
        case "2":
            matrix_1 = matrix_enter()
            length = len(matrix_1)
            matrix = [[0 for i in range(length)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    matrix[i][j] = matrix_1[-j - 1][-i - 1]
            print("The result is:")
            for v in matrix:
                print(" ".join(str(x) for x in v))
            print()
        case "3":
            matrix_1 = matrix_enter()
            length = len(matrix_1)
            matrix = [[0 for i in range(length)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    matrix[i][j] = matrix_1[i][-j - 1]
            print("The result is:")
            for v in matrix:
                print(" ".join(str(x) for x in v))
            print()
        case "4":
            matrix_1 = matrix_enter()
            length = len(matrix_1)
            matrix = [[0 for i in range(length)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    matrix[i][j] = matrix_1[-i - 1][j]
            print("The result is:")
            for v in matrix:
                print(" ".join(str(x) for x in v))
            print()
        case "5":
            return None


def minor_function(matrix, i, j):
    minor = copy.deepcopy(matrix)
    del minor[i]
    for i in range(len(matrix[0]) - 1):
        del minor[i][j]
    return minor


def det(matrix):
    m = len(matrix)
    n = len(matrix[0])
    if m != n:
        return None
    if n == 1:
        return matrix[0][0]
    signum = 1
    determinant = 0
    for j in range(n):
        if det(minor_function(matrix, 0, j)) is None:
            determinant += 0
            signum *= -1
        else:
            determinant += matrix[0][j] * signum * det(minor_function(matrix, 0, j))
            determinant = int(determinant) if determinant == round(determinant) else determinant
            signum *= -1
    return round(determinant, 1)


def calculate_a_determinant():
    matrix_1 = matrix_enter()
    print("The result is:")
    print(det(matrix_1))
    print()


def inverse_matrix():
    matrix = matrix_enter()
    if len(matrix) != len(matrix[0]):
        print('Non-square matrix!!!')
        return None
    determinant = det(matrix)
    if determinant == 0:
        print('Reverse matrix for matrix with zero determinant doesn`t exist')
        return None
    matrix_1 = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for o in range(len(matrix_1)):
        for k in range(len(matrix_1[0])):
            matrix_1[o][k] = matrix[k][o]
    inverse = [[0 for j in range(len(matrix_1))] for i in range(len(matrix_1[0]))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            minor = [[0 for j in range(len(matrix_1) - 1)] for i in range(len(matrix_1[0]) - 1)]
            row_shift = 0
            for k in range(len(matrix_1)):
                if k == i:
                    row_shift = 1
                    continue
                column_shift = 0
                for p in range(len(matrix_1[0])):
                    if p == j:
                        column_shift = 1
                        continue
                    minor[(k - row_shift)][(p - column_shift)] = matrix_1[k][p]
            inverse[i][j] = ((-1) ** (i + j)) * det(minor)
    for o in range(len(matrix_1)):
        for k in range(len(matrix_1[0])):
            inverse[o][k] *= 1 / determinant
            inverse[o][k] = round(inverse[o][k], 1)
    print("The result is:")
    for v in matrix_round(inverse):
        print(" ".join(str(x) for x in v))
    print()


def exit():
    print("Enjoy! Come back!")
    sys.exit()


while True:
    action_choose = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
""")
    while action_choose != '1' \
            and action_choose != '2' \
            and action_choose != '3' \
            and action_choose != '4' \
            and action_choose != '5' \
            and action_choose != '6' \
            and action_choose != '0':
        print("You wrote the wrong line!")
        action_choose = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Determinant 
6. Inverse matrix
0. Exit
""")
    if action_choose == '1':
        add_matrices()
    elif action_choose == '2':
        multiply_matrix_by_a_constant()
    elif action_choose == '3':
        multiply_matrices()
    elif action_choose == '4':
        transpose_matrix()
    elif action_choose == '5':
        calculate_a_determinant()
    elif action_choose == '6':
        inverse_matrix()
    elif action_choose == '0':
        exit()
