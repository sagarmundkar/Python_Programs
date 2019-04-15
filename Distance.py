import math

Num1 = int(input("Enter the value of num1:"))
Num2 = int(input("Enter the value of num2:"))

Edistance = math.sqrt(math.pow(Num1,Num2) + math.pow(Num2,Num2))
print("Euclidean distance of Num1 and Num2",Edistance)