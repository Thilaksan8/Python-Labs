INPUT_FILE_NAME = input()  # Takes the name of the input file from the user.
########################################################################################
# Do not change anything above this line
########################################################################################

# Use INPUT_FILE_NAME variable to read the file instead of 'matrix_data.txt'
# Enter your code here
def input_matrix(matrix):
    matrix_file = open(matrix, 'r')  # Open the  file in read mode.
    data = matrix_file.read()  # Read the file.
    matrix_file.close()  # Close the file.
    data = data.split('\n')  # Split the content by line.
    data_index = 1  # to keep track of the current line.
    matrices = []  # List to store all the matrices.
    for repeat in range(int(data[0])):  # to know line tells how many matrices to process.
        n = int(data[data_index])  # Reads the size of the current matrix.
        data_index += 1  # to move to next line.
        matrix = []  # to store the current matrix.
        for i in range(n):  # Read the each row of the matrix.
            row = list(map(int, data[data_index].split(',')))  # Split the row by comma and convert  each value to an integer.
            matrix.append(row)  # Adds the row to the matrix.
            data_index += 1  # to move the next line.
        matrices.append(matrix)  # Add the current matrix to the list of matrices.
    return matrices  # Return the list of matrices.

def determinant(matrix):
    if len(matrix) == 2:  # Special case for a 2x2 matrix to determine the determinant.
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        det = 0  # take initial determinant as 0.
        for col in range(len(matrix)):  # Iterate over the first row to calculate the determinant.
            minor = minor_matrix(matrix, 0, col)  # Get the minor matrix after removing the first row and current column.
            det += ((-1) ** col) * matrix[0][col] * determinant(minor)  # Apply cofactor expansion.
        return det  # Returns the determinant.

def minor_matrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])] # Returns the matrix obtained by removing the i-th row and j-th column.
    

def cofactor_matrix(matrix):
    cofactors = []  # List to store the cofactor matrix.
    for row in range(len(matrix)):  # Iterate over each row.
        cofactor_row = []  # List to store the cofactor row.
        for col in range(len(matrix)):  # Iterate over each column.
            minor = minor_matrix(matrix, row, col)  # Get the minor matrix for the current element.
            cofact_val = ((-1) ** (row + col)) * determinant(minor)  # Calculate the cofactor of the element.
            cofactor_row.append(cofact_val)  # Append the cofactor value to the row.
        cofactors.append(cofactor_row)  # Append the cofactor row to the cofactor matrix.
    return cofactors  # Returns the cofactor matrix.

def transpose(matrix):
    Transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] # Returns the transpose of a given matrix.
    return Transpose

def inverse_matrix(matrix):
    det = determinant(matrix)  # Calculate the determinant of the matrix.
    if len(matrix) == 2:  # Special case for a 2x2 matrix to calculate the inverse directly.
        a, b = matrix[0][0], matrix[0][1]
        c, d = matrix[1][0], matrix[1][1]
        return [[d / det, -b / det], [-c / det, a / det]]  # Return the inverse using the 2x2 formula.
    else:
        cofactors = cofactor_matrix(matrix)  # Get the cofactor matrix.
        adjoint = transpose(cofactors)  # Get the adjoint .
        inverse = [[(1/det) * elem for elem in row] for row in adjoint]  # Multiply each element of adjoint by 1/determinant.
        return inverse  # Return the inverse matrix.

def display_resultant_inverse(matrix, matrix_idx):
    print(f"Inverse of Matrix {matrix_idx}:")  # Print the index of the matrix.
    for row in matrix:  # Iterate over each row of the matrix.
        print("".join(f"{0.00 if elem == -0.00 else elem:7.2f}" for elem in row))  # Print each element formatted to 2 decimal places.

# Read the matrices from the file.
matrices = input_matrix(INPUT_FILE_NAME)

matrix_idx = 1  # Variable to keep track of the matrix index.
for matrix in matrices:  # Iterate over each matrix.
    inv_matrix = inverse_matrix(matrix)  # Calculate the inverse of the matrix.
    display_resultant_inverse(inv_matrix, matrix_idx)  # Display the inverse of the matrix.
    matrix_idx += 1  # Increment the matrix index.
