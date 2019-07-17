
def maxNumber(numberA, numberB):
    if(numberA > numberB):
        return numberA
    else:
        return numberB

numberA = int(input("Enter 1st Number : "))
numberB = int(input("Enter 2nd Number : "))

print("Max Number is : ", maxNumber(numberA,numberB))