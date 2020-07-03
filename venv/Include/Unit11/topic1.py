# 第一节：输入数据，并获取输入数据的平均值
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


if __name__ == '__main__':
    getAverage()
