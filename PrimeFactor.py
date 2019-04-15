N = int(input("Enter the number:"))


def prime(N):
    for i in range(2, N):
        if N % i == 0:
            return False

    return True


def prime_factor(n):
    print("Prime factor is : ")
    for i in range(2, n):
        if prime(i):
            if n % i == 0:
                print(i, " ")
