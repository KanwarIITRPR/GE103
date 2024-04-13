A = [[1, 2],
     [3, 7],
     [8, 2]] # Defining a matrix A

B = [[1, 0, 9],
     [0, 5, 6]] # Defining another matrix B

def matrix_multiplication(A, B): # Writing a function to multiply two matrices
    '''A function that takes as inputs list of lists that depicts square matrices A and B and then returns their product'''

    # For two matrices to have a proper product, the first matrix requires to have the same number of columns as the number of rows of the second matrix
    if len(A[0]) != len(B):
        return "Can't multiply the given matrices!"
    
    C = [] # Resulting product matrix
    for i in range(len(A)): # "i" represents the row we are going through in A
        row = [] # It defines the elements present in the row for the current iteration of the matrix
        for j in range(len(B[0])): # "j" represents the column in which we are going through in B
            ij_th_cell = 0 # It defines the ij'th element of the resultant matrix and finally represents the dot product of the small matrices
            # Dot product of row and column matrices - derived from the initial matrices
            for k in range(len(A[0])): # "k" represents the number of iterations we are at in rows of A and in columns of B
                ij_th_cell += A[i][k] * B[k][j] # Does the dot product of ik'th element of A and kj'th element of B
            row.append(ij_th_cell) # Adds the ij'th element to the row which it is in, in the final matrix
        C.append(row) # Adds the row we were working in currently to the final matrix

    return C

print(f"Matrix A: {A}")
print(f"Matrix B: {B}")
print(f"The product of the above two matrices is C: {matrix_multiplication(A, B)}")