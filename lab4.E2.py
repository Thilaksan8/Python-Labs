a=int(input("Input number: "))
c=0
if(a>1):
    for i in range(1,a+1):
        b=0
        for m in range(1,i):
            if(i%m==0):b+=m
        if(b>i):c+=1
    print("Number of abundant numbers from 1 to" ,a, "is",c)
else:
    print("Invalid Input")

