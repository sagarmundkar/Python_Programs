import random

n = int(input("Enter the goal gambler want to achieve: "))
doller = 1
win, loss = 0, 0

while True:
    n = int(input("Enter any number between 1 to 2"))
    g = random.randint(1, 3)
    if n == g:
        doller +=1
        win +=1
        print("You won the bet.")
    else:
        print("You loss the bet.")
        doller -=1
        loss +=1

    if doller == 0:
        print("You loss your doller.")
        break
    elif doller == n:
        print("You achieve your goal.")

print("toatl matches are:", (win+loss))
print("Percentage of win :", (win * 100)/(win + loss))
print("Percentage of loss :", (loss * 100)/(win - loss))