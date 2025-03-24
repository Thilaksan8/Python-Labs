matrix=[]                       # define an empty
is_error=0                      # Flag variable to track if an error has occurred.
while True:                     # define loop to input rows of the matrix
    rows_in=input()             # get input for a row of the matrix
    if (rows_in=="-1"):          
        break                      # Exit the loop if "-1" is entered.
    rows_in=rows_in.split()        # Split the input string into a list of elements.
    if not matrix:                 # If the matrix is empty (i.e., first row being entered).
        count=len(rows_in)         # Set the expected number of columns based on the first row.
    if (count!=len(rows_in)):        # Check if the current row has a different number of elements than the first row.
            print("Invalid Matrix")   
            is_error=1                # Set the error flag to indicate an issue.
            break                      # Exit the loop since the matrix is invalid
    for i in rows_in:                 # Loop through each element in the current row.
        try:
            float(i)                 # Attempt to convert the element to a float.
        except ValueError:
            print("Error")           # Print an error message if conversion fails.

            is_error=1               # Set the error flag to indicate an issue.
            break                       # Exit the loop since an invalid element was found
    matrix.append(rows_in)              # Append the current row to the matrix.
if(is_error==0):                         # Loop to transpose the matrix by switching rows with columns.
    for i in range(len(matrix[0])):  # Iterate over the number of columns.
        tranpose=[]                  #define an empty list to store the transposed row.
        for j in matrix:              # Loop through each row of the matrix.
            tranpose.append(j[i])      # Append the i-th element of each row to the transposed row.
        print(' '.join(tranpose))       # Print the transposed row as a space-separated string.
            
    
    