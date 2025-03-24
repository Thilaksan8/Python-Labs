def diemen():
    matrix_dimension=input("Enter the dimension: ").split(',')    #get dimension from user
    matrix_dimension=[int(i) for i in matrix_dimension]    
    row_dimension=matrix_dimension[0]
    coloumn_dimension=matrix_dimension[1]
    return row_dimension,coloumn_dimension  # Return the number of rows and columns
def matrix(matrix_name,row_dimension,coloumn_dimension):
    b=0   # Flag to indicate if there's an error in the matrix input
    matrix=[]
    print('Enter Matrix '+matrix_name+':')
    for i in range(row_dimension):
        if(b!=1):
            row=input().split()  #get input for rows of matrix
            if(len(row)==coloumn_dimension):
                matrix.append(row)
            else:
                print('Invalid Matrix')  
                b=1  # Set the error flag
                break
            for k in row:
                try:
                    int(k)
                except ValueError:
                    b=1   # Set the error flag
                    print('Error')
                    break
    if(b==0):
        return matrix
    else:
        return b
def transpose(B):
    if(B!=1):
        transpose1=[]
        for i in range(len(B[0])):
            tanpose_row=[]
            for j in B:
                 tanpose_row.append(j[i])
            transpose1.append(tanpose_row)
    return transpose1
def matrix_product(A,BT,row_dimension,coloumn_dimension):
    value_of_element=0
    product_row=[]
    for i in range(row_dimension):
        for k in range(row_dimension):
            for j in range(coloumn_dimension):
                value=int(A[i][j])*int(BT[j][k])
                value_of_element=value_of_element+value
            row=str(value_of_element)
            product_row.append(row)
            value_of_element=0
        print(' '.join(product_row))
        product_row=[]
row_dimension,coloumn_dimension=diemen()   # Get matrix dimensions from the user
matrix_name='A'
A=matrix(matrix_name,row_dimension,coloumn_dimension)
if(A!=1):
    matrix_name='B'
    B=matrix(matrix_name,row_dimension,coloumn_dimension)
    BT=transpose(B)   # Transpose matrix B
    if(B!=1):
        matrix_product(A,BT,row_dimension,coloumn_dimension)
