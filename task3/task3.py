def checkSpeed(speed):
    
    if speed <= 70:
        print("OK: "+str(speed))
        return 0
    else:
        return int((speed - 70) / 5)


if __name__ == "__main__":
    speedPoints = []
    speed = [24,80,70,44,90,100,20] 
    fine = 0
    for i in speed:
        fine += checkSpeed(i)
    
    if fine >= 12:
        print("Liscense Suspended!")

