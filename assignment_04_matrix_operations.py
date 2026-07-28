# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

def transpose_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = input_matrix(rows, cols)

    print("Transposed Matrix:")
    for j in range(cols):
        for i in range(rows):
            print(matrix[i][j], end=" ")
        print()

def add_matrices():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter first matrix:")
    matrix1 = input_matrix(rows, cols)

    print("Enter second matrix:")
    matrix2 = input_matrix(rows, cols)

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    print("Sum of matrices:")
    display_matrix(result)

def multiply_matrices():
    rows1 = int(input("Rows of Matrix A: "))
    cols1 = int(input("Columns of Matrix A: "))

    print("Enter Matrix A:")
    A = input_matrix(rows1, cols1)

    rows2 = int(input("Rows of Matrix B: "))
    cols2 = int(input("Columns of Matrix B: "))

    if cols1 != rows2:
        print("Matrices cannot be multiplied.")
        return

    print("Enter Matrix B:")
    B = input_matrix(rows2, cols2)

    result = []

    for i in range(rows1):
        row = []
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    print("Product of matrices:")
    display_matrix(result)

transpose_matrix()
add_matrices()
multiply_matrices()
# =============================================================================

