num=input()                   #Input a space-separated list of numbers as a single string.
num=num.split()                #Split the input into a list of individual elements
max1=min1=num[0]               #assign num[0] value to max1 &max2
for i in num:                  #Iterate the each number in the num list
    if(float(i)>float(max1)):    #finding the maximum in the num list
        max1=i
    if(float(i)<float(min1)):     #finding the minimum value in the num list
        min1=i
print("Minimum =",min1)       # Print the minimum value  in the list.
print("Maximum =",max1)       # Print the maximum value  in the list.