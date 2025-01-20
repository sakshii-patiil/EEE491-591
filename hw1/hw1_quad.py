from numpy import sqrt
import cmath
a= float (input("Input coefficient a:"))
b= float (input("Input coefficient b:"))
c= float (input("Input coefficient c:"))

root = (b*b - 4*a*c)
print(root,"\n")

if root==0:
    x=float (-b / (2*a))
    print("\nDouble root :",x)
else :
    if (cmath.sqrt((root))).imag ==0:
        x1= (-b+ sqrt(root))/(2*a)
        x2= (-b- sqrt(root))/(2*a)
    else:
        x1= (-b/(2*a)) + (cmath.sqrt((root))) / (2*a)
        x2= (-b/(2*a)) - (cmath.sqrt((root))) / (2*a)
    print("\nRoot 1 :",x1)
    print("Root 1 :",x2)