import math

power = int(input("Enter the power of value:"))

for i in range(power):
    if i <= 31:
        print(i, "is power of 2 is", int(math.pow(2, i)))
    else:
        print("Range Exceed")

