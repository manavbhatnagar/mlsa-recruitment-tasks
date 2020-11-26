import math
x=int(input("enter x"))
y=int(input("enter y"))
z=int(input("enter z"))
a=(math.trunc(y/x)+1)
b=x*a
c=y+z
if(b>c):
 print("no")
else:
 print("yes")