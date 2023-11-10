print("kbee")

def getdouled(*doubled):
    num = 2
    for number in doubled:
        num *= number
    return num

print(getdouled(234))