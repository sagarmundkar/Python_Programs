import math

num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
num3 = int(input("Enter the number3:"))

rootx1 = 0.0
rootx2 = 0.0

delta = num2 * num2 - 4 * num1 * num3

if delta > 0:
    rootx1 = (- num2 + math.sqrt(delta)) / (2 * num1)
    rootx2 = (- num2 - math.sqrt(delta)) / (2 * num1)

print("Two roots of x are : " + str(rootx1) + " & " + str(rootx2))