import math

t = int(input("Enter the temperature:"))
v = int(input("Enter the speed:"))
if t < 50 or v < 120 or v > 3:
    w = 34.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
print('WindChill is:', w)
