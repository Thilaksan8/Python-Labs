obj=input()            # get input as a single string.
obj=obj.split()        # Split the input string into a list of words. 
sub=["I","We"]          # Define a list of sub
verb=['play','watch']       # Define a list of verb
for i in range(2):          # Outer loop iterates over the indexes of the 'sub' list (0 and 1)
    for m in range(2):      # Middle loop iterates over the indexes of the 'verb' list (0 and 1)
        for n in range(2):      # Inner loop iterates over the indexes of the 'obj' list (0 and 1)
            print(sub[i],verb[m],obj[n]+".")     # Print the combination of subject, verb, and object with a period at the end.
            