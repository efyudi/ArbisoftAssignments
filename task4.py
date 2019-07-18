def showNumbers(limit):
    dictionary = {}
    for i in range(limit + 1):
        dictionary[i] = "EVEN" if divmod(i, 2)[1] == 0 else "ODD"
    print(dictionary)


if __name__ == "__main__":
    limit = int(input("Enter a Number : "))
    showNumbers(limit)
