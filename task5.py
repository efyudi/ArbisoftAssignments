def multiplies(limit):
    sum = 0
    for i in range(0, limit + 1):
        if divmod(i, 3)[1] == 0 or divmod(i, 5)[1] == 0:
            sum += i
    return sum


if __name__ == "__main__":
    limit = int(input("Enter a Number : "))
    print("Sum of Multiplies : ", multiplies(limit))
