a=input("Enter message: ")
base=int(input("Enter base: "))
final=""
for i in a:
    b=ord(i)
    sum=""
    while(b>0):
        c=b%base
        b=b//base
        sum=str(c)+sum
    final=final+sum
print(final)
        

