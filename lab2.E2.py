date_input = input()
y, m, d = map(int, date_input.split())
if(m<3):
    m+=12
    y-=1
a= 2*m + 6*(m + 1)// 10
b = y + y//4-y//100 + y//400
f1 = d + a + b +1
f = f1%7
print(f)