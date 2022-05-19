
# patten 0


def printPascal(n):
    arr = [[0 for x in range(n)]
           for y in range(n)]

    for line in range(0, n):

        for i in range(0, n):

            if i == 0 or i == line:
                arr[line][i] = 1
                print(arr[line][i], end=" ")


            else:
                arr[line][i] = (arr[line - 1][i - 1] +
                                arr[line - 1][i])
                print(arr[line][i], end=" ")
        print("\n", end="")
printPascal(3)

# pattern 1\
rows = 8
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")

    k = k - 1

    for j in range(0, i + 1):
        print("* ", end="")
    print("")
k = rows - 2


for i in range(rows, -1, -1):

    for j in range(k, 0, -1):
        print(end=" ")

    k = k + 1

    for j in range(0, i + 1):
        print("* ", end="")
    print("")

# pattern2

n = 5
for i in range(n):
    # printing spaces
    for j in range(n - i - 1):
        print(' ', end='')

    # printing stars
    for k in range(2 * i + 1):
        # print star at start and end of the row
        if k == 0 or k == 2 * i:
            print('*', end='')
        else:
            if i == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
    print()
# pattern3
print("pattern3")


# pattern 3
n = 5
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(i, n):
        if (j == i or i == 0 or j == n - 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()