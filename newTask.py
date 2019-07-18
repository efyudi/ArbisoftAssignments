def makeDiamond(number):
    for i in range(1, (number * 2)):
        spaces = number - i if i < number else i - number                             # Check to Inverse Spaces
        for j in range(spaces):                     # PRINT Spaces Before Numbers
            print(" ", end="")
        for j in range(number - spaces, 0, -1):     # PRINT Decreasing Numbers
            print(j, end="")
        for j in range(2, number - spaces + 1):     # PRINT Increasing Numbers
            print(j, end="")
        print("")


if __name__ == '__main__':
    number = int(input("Enter a Number : "))
    makeDiamond(number)
