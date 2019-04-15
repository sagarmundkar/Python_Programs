import numpy as np

def get_two_d_arr(r, c):
    print("Enter a list : ")
    arr = np.zeros((r, c))
    for i in range(r):
        for j in range(c):
            arr[i][j] = int(input())
    return arr


def display_two_d_arr(arr):
    print(arr)

def main():
    r = int(input("Enter row value : "))
    c = int(input("Enter column value : "))
    arr = get_two_d_arr(r, c)
    display_two_d_arr(arr)


if __name__ == '__main__':
    main()