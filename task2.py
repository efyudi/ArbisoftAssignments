
def fizz_buzz(number):
    if(number%3 == 0 and number%5 == 0):
        return "FizzBuzz"
    elif(number%3 == 0):
        return "Fizz"
    elif(number%5 == 0):
        return "Buzz"
    else:
        return number


def main():
    number = int(input("Enter a Number : "))
    print(fizz_buzz(number))


if __name__ == "__main__":
    main()
