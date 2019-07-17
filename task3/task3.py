
def checkSpeed(speed):
    return "OK" if (speed<70) else "Points : "+str((speed-70)/5)

if __name__ == "__main__":
    speed = int(input("Enter the speed : "))
    print(checkSpeed(speed))