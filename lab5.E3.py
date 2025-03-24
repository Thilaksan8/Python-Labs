marks=[]                           # an empty list to store. 
for i in range(4):                  # Loop to input marks of 4 students.
    marks_in=input()                 # get input for the marks of a student.
    marks_in=marks_in.split()       # Split the input string into a list of individual marks.
    marks.append(marks_in)          # Append the list of marks to the 'marks' list.
for i in marks:                      # Loop each list of marks in the 'marks' list.
    total=0                          # define a variable to store the total marks of each student
    for m in i:                      # Loop each mark in the student's list of marks.
        total=total+int(m)             # Convert the mark to an integer and add it to the total.
    print("Total:",total,"Average:",'%.1f'%(total/3))    # Print the total marks and the average marks for the each student.
    