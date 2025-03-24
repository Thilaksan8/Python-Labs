a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))

delta=b**2-4*a*c

if delta >=0:
    r1=(-b-delta**(1/2))/(2*a)
    r2=(-b+delta**(1/2))/(2*a)
    print("Roots are: ", r1,r2)
else:
    print("No real roots")
