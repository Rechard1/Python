# 第五节：Python计算器（简单）
class Calculator:
    def __init__(self):
        win = GraphWin("calculator")
        win = GraphWin.setCoords(0, 0, 6, 1)
        win = GraphWin.setBackground("slategray")
        self.win = win
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):
        bSpecs = [(2, 1, '0'), (3, 1, '.'),
                  (1, 2, '1'), (2, 2, '2'), (3, 2, '3'), (4, 2, '+'), (5, 2, '-'),
                  (1, 3, '4'), (2, 3, '5'), (3, 3, '6'), (4, 3, '*'), (5, 3, '/'),
                  (1, 4, '7'), (2, 4, '8'), (3, 4, '9'), (4, 4, '<-'), (5, 3, 'C')]
        self.buttons = []
        for (cx, cy, label) in bSpecs:
            self.buttons.append(Button(self.win, Point(cx, cy), .75, .75, label))
        # 画等号，最长的按钮
        self.buttons.append(Button(self.win, Point(4.5, 1), 1.75, .75, "="))

        # 激活所有按钮
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        bg = Rectangle(Point(.5, 5.5), Point(5.5, 6.5))
        bg.setFill("white")
        bg.draw(slef.win)
        text = Text(3, 5, "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(16)
        self.display = text

    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()

    def processButton(self, key):
        text = self.display.getText()
        if key == 'C':
            self.display.setText("")
        elif key == '<-':
            self.display.setText(text[:-1])
        elif key == '=':
            try:
                result = eval(text)
            except:
                result = "ERROR"
            self.display.setText(str(result))
        else:
            self.display.setText(text + key)

    def run(self):
        while True
            key = self.getButton()
            self.processButton(key)


if __name__ == '__main__':
    theCac = Calculator()
    theCac.run
