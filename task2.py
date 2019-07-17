def fizz_buzz(number):
    a = []
    if divmod(number, 3)[1] == 0:
        a.append("Fizz")
    if divmod(number, 5)[1] == 0:
        a.append("Buzz")

    return ''.join(a) if a else number


if __name__ == "__main__":
    number = int(input("Enter a Number : "))
    print(fizz_buzz(number))
