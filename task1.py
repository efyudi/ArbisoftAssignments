
def maxNumber(numberA, numberB):
    return numberA if numberA > numberB else numberB

if __name__ == "__main__":
    numberA = int(input("Enter 1st Number : "))
    numberB = int(input("Enter 2nd Number : "))

    print("Max Number is : ", maxNumber(numberA,numberB))
