def getAverage():
    count = 0
    total = 0.0

    strX = input("input x to stop or continue >>")
    while (strX != ""):
        x = float(strX)
        total = total + x
        count += 1

        strX = input("input please: >>")
    print("The average number is ", total / count)

def getAverageEx():
    count=0;
    numList=[]

    strX = input("input x to stop or continue >>")
    while (strX != ""):
        numList.append(float)
        count+=1
        strX = input("input x to stop or continue >>")

    total=0.0
    for a in numList:
        total=total+a

    for i in range(len(numList)):
        if(numList[i]>numList[i+1])



if __name__ == '__main__':
    print("test")