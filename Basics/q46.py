A = [[1, 7],
     [2, 8],
     [5, 6]] # Defining a matrix A

B = [[9, 4],
     [0, 0],
     [2, 3]] # Defining another matrix B

def matrix_addition(A, B): # Writing a function to add two matrices
    '''A function that takes as inputs list of lists that depicts square matrices A and B and then returns the sum'''

    # Matrices can be added if the number of rows and columns of both the matrices are same - if not, we will reurn a message signifying the inability to compute their sum
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Can't add the given matrices!"
    
    C = [] # Resulting sum matrix
    for i in range(len(A)): # "i" represents the number of rows in the matrices
        row = [] # It defines the elements present in the row for the current iteration of the matrix
        for j in range(len(A[0])): # "j" represents the number of columns in the matrices
            row.append(A[i][j] + B[i][j]) # Adding the ij'th element of both the matrices - in the way matrix multiplication is defined
        C.append(row) # Finally adding the currrent row to the final matrix "C"

    return C

print(f"Matrix A: {A}")
print(f"Matrix B: {B}")
print(f"The sum of the above two matrices is C: {matrix_addition(A, B)}")