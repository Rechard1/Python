from random import random

#壁球游戏
class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    # 比赛过程，是否胜利
    def winServe(self):
        return random() < self.prob

    # 胜局加分
    def incScore(self):
        self.score = self.score + 1

    def getScore(self):
        return self.score


class RBallGame:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        # 让A先发球
        self.server = self.playerA

    def play(self):
        if self.isOver():
            if self.playerA.winServe():
                self.playerA.incScore()
            else:
                self.changeServr()

    def isOver(self):
        a, b = self.getScores()
        return a == 15 or b == 15 or (a == 7 and b == 0) or (b == 7 and a == 0)

    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()

    # 交换发球
    def changeServr(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA


class SimStats:
    def __init__(self):
        self.winA = 0
        self.winB = 0
        self.shutA = 0
        self.shutB = 0

    def getInput(self):
        a = input(print("The win prob of player A:"))
        b = input(print("The win prob of player B:"))
        n = input(print("how many games to shut down"))
        return a, b, n


    def printIntru(self):
        print("this is a ball Game")

    def updateGame(self,aGame):
        a,b =aGame.getScores()
        if(a>b):
            self.winA=self.winA+1
            if b==0:
                self.shutA=self.shutA+1
        else:
            self.winB=self.win+1
            if a==0:
                self.shutB=self.shutB+1

    if __name__ == '__main__':
        printIntru()
        probA,probB,n=getInput()

        stats=SimStats
        for i in range(n):
            theGame=RBallGame(probA,probB)
            theGame.play()
            stats.updateGame(theGame)


