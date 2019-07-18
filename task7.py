import math
def primeNumbers(limit):
    for i in range(1, limit + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if divmod(i, j)[1] == 0:
                break
        else:
            print(i)


if __name__ == "__main__":
    limit = int(input("Enter a Number : "))
    primeNumbers(limit)
