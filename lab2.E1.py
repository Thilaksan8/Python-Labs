a=float(input("Enter angle 1: "))
b=float(input("Enter angle 2: "))
c=float(input("Enter angle 3: "))
if(a+b+c== 180 and a>0 and b>0 and c>0):
    if(a==90 or b==90 or c == 90):
        print("Right angled")
    elif(a>90 or b>90 or c>90):
       print("Obtuse angled")
    else:
        print("Acute angled")
else:
    print("Angles do not form a triangle")