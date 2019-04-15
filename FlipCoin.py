import random

n = int(input("Enter the no of flip:"))
for i in range(n):
    # to generate random number
    rand = random.random()
    if rand < 0.5:
        print("percentage of Heads:", int(rand * 100))
    else:
        print("Percentage of Tails:", int(rand * 100))
