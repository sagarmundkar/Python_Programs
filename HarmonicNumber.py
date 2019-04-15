N = int(input("Enter the number:"))
# def Harmonic(N):
value = 0.0
for i in range(1, N + 1):
    value = value + (1.0 / N)
print("Result of Nth harmonic value:", value)
