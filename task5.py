def multiplies(limit, divisors):
    sum = 0
    for i in range(0, limit + 1):
        for j in divisors:
            if divmod(i, j)[1] == 0:
                sum += i
                break
    return sum


if __name__ == "__main__":
    divisors = [2, 5, 10, 13, 11]
    limit = int(input("Enter a Number : "))
    print("Sum of Multiplies : ", multiplies(limit, divisors))
